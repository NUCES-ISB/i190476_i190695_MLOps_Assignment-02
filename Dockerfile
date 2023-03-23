FROM python:3.9.16 
# Set the working directory of the project
WORKDIR /
# Create a new folder for storing Flask webpages
RUN mkdir templates
# Create a new folder for Styles
RUN mkdir static && mkdir static/styles
# Copy the requirements
COPY requirements.txt ./requirements.txt
# Copy the Makefile for installation
COPY Makefile ./Makefile
# Copy the training file
COPY live_stream_training_data.csv ./live_stream_training_data.csv
# Copy the files required for Flask server
COPY templates/live.html ./templates/live.html
COPY templates/predict.html ./templates/predict.html
COPY static/styles/styles.css ./static/styles/styles.css
# Copy the Python files necessary for running the additional functionalities of the Flask server
COPY data_fetch.py ./data_fetch.py
COPY train.py ./train.py
COPY inference.py ./inference.py
# Finally, copy the Flask server execution file
COPY main.py ./main.py
# Install the dependencies
RUN make install
# Now, in order of appearance, run the train file and generate the models, then run the Flask server to initiate your own server
RUN python train.py
# Setting the environment variable for flask app
ENV FLASK_APP=main.py
# Command for running flask app
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]
