from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json, os
import pandas as pd
from threading import Lock
from datetime import datetime
from inference import inference
from sklearn import preprocessing
from joblib import load
import statistics as stat

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
        # print(df)

        # Saving the data frame for later use
        final_frame = df.copy()

        df = df.drop(['Close'], axis=1)

        # dropping the "Date" column
        df = df.drop(['Date'], axis=1)
        df = df.drop(['Ticker'], axis=1)

        # dropping null values
        df = df.dropna()

        # Seperating the data for testing
        df = df.values

        # Data normalization (0,1)
        df = preprocessing.normalize(df, norm='l2')

        # Run model
        clf_LR = load("MODEL_LR")
        clf_SVR = load("MODEL_SVR")
        clf_RFR = load("MODEL_RFR")

        # clf_LR.score(X_test, y_test)
        pred_LR = clf_LR.predict(df)

        # clf_SVR.score(X_test, y_test)
        pred_SVR = clf_SVR.predict(df)

        # clf_RFR.score(X_test, y_test)
        pred_RFR = clf_RFR.predict(df)

        #Use majority voting for prediction
        predictions=pd.DataFrame([pred_LR, pred_SVR, pred_RFR])
        final = predictions.apply(stat.mode)

        # Recommendation
        # print("Based on my training, I recommend the following")
        # Python program to understand, how to print tables using pandas data frame
        data = {'Estimator 1':pred_LR,'Estimator 2':pred_SVR,'Estimator 3':pred_RFR, 'Predicted Close':final}
        data = pd.DataFrame(data)
        # print(data)

        final_frame = final_frame.join(data['Predicted Close'])



        # Now use that CSV to test the values, and send answer as CSV as well
        return render_template(
            'predict.html',
            tables=[final_frame.to_html(classes='data')],
            titles=final_frame.columns.values
        )

@app.route('/predict',methods=["GET","POST"])
def predict():
    return render_template('predict.html')

if __name__ == '__main__':
    # Do not use debug=True for production/deployment
    socketio.run(app, port=8090)
