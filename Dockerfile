FROM python:3.9.16
# Set the working directory of the project
WORKDIR /
# Create a new folder for storing Flask webpages
RUN mkdir templates
# Copy the requirements
COPY requirements.txt ./requirements.txt
# Copy the Makefile for installation
COPY Makefile ./Makefile
# Copy the training file
COPY live_stream_training_data.csv ./live_stream_training.csv
# Copy the HTML files for Flask server
COPY templates/live.html ./templates/live.html
COPY templates/predict.html ./templates/predict.html
# Copy the Python files necessary for running the additional functionalities of the Flask server
COPY data_fetch.py ./data_fetch.py
COPY train.py ./train.py
COPY inference.py ./inference.py
# Finally, copy the Flask server execution file
COPY main.py ./main.py
# Install the dependencies
RUN make install
# Now, in order of appearance, run the train file and generate the models, then run the Flask server to initiate your own server
RUN python train.py && python main.py
ENTRYPOINT ["/bin/bash"]
