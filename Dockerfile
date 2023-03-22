FROM python:3.9.16
# Setting the working directory
WORKDIR /
# Copy the files
COPY requirements.txt ./requirements.txt
COPY Makefile ./Makefile
COPY live_stream_training_data.csv ./live_stream_training.csv
COPY train.py ./train.py
COPY inference.py ./inference.py
# Installation of the dependecies
RUN make install
RUN 
# training is executed while creating the docker image and the trained models are stored in the my-model directory
#RUN python train.py && python main.py
ENTRYPOINT ["/bin/bash"]
