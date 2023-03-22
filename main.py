from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json, os
import pandas as pd
from threading import Lock
from datetime import datetime
from inference import inference

app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app, cors_allowed_origins='*')

thread = None
thread_lock = Lock()

def get_current_datetime():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

def daemon_thread():
    while True:
        #dummy_sensor_value = round(random() * 100, 3)
        data = inference()
        socketio.emit(
            'updateData',
            {'value': data['Decision'].iloc[len(data)-1],
            'date': get_current_datetime()}
        )
        socketio.sleep(60)

@socketio.on('connect')
def connect():
    global thread
    print()
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(daemon_thread)

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected', request.sid) 
    

@app.route('/',methods=["GET","POST"])
def homepage():
    return render_template('live.html')

@app.route('/test',methods=["GET","POST"])
def test():
    if request.method == 'POST':
        # Check if file is CSV
        extension = request.files['file'].filename.split('.').pop()
        if (extension != 'csv'):
            # throw error
            pass
        # Then extract information
        data = str(
            request.files['file'].read(),
            'utf-8'
        )
        file = open('temp.csv', 'w')
        file.write(data)
        file.close()
        df = pd.read_csv('temp.csv')
        os.remove('temp.csv')
        print(df)
        # Now use that CSV to test the values, and send answer as CSV as well
        return render_template(
            'predict.html',
            tables=[df.to_html(classes='data')],
            titles=df.columns.values
        )

@app.route('/predict',methods=["GET","POST"])
def predict():
    return render_template('predict.html')

if __name__ == '__main__':
    socketio.run(app, debug=True, port=8090)