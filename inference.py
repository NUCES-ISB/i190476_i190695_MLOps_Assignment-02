# importing the necessary libraries
import pandas as pd
import numpy as np
from joblib import load
from sklearn import preprocessing
from data_fetch import get_dataframe_for_testing
import statistics as stat

def inference():
    # Load, read and normalize training data
    get_dataframe_for_testing()
    testing = pd.read_csv("live_stream_test_data.csv")
    
    # dropping the "Date" column
    testing = testing.drop(['Date'], axis=1)
    testing = testing.drop(['Ticker'], axis=1)

    # dropping null values
    testing = testing.dropna()

    # Seperating the data for testing
    y_test = testing["Close"].values
    X_test = testing.drop(['Close'], axis=1)
    X_test = X_test.values

    # Data normalization (0,1)
    X_test = preprocessing.normalize(X_test, norm='l2')

    # Run model
    clf_LR = load("MODEL_LR")
    clf_SVR = load("MODEL_SVR")
    clf_RFR = load("MODEL_RFR")

    # clf_LR.score(X_test, y_test)
    pred_LR = clf_LR.predict(X_test)

    clf_SVR.score(X_test, y_test)
    pred_SVR = clf_SVR.predict(X_test)

    clf_RFR.score(X_test, y_test)
    pred_RFR = clf_RFR.predict(X_test)

    #Use majority voting for prediction
    predictions=pd.DataFrame([pred_LR, pred_SVR, pred_RFR])
    final = predictions.apply(stat.mode)

    # Recommendation
    print("Based on my training, I recommend the following")
    # Python program to understand, how to print tables using pandas data frame
    data = {'Estimator 1':pred_LR,'Estimator 2':pred_SVR,'Estimator 3':pred_RFR, 'Decision':final}
    data = pd.DataFrame(data)
    print(data)

    # Returning the dataframe for Using in FLASK
    return data

if __name__=="__main__":
    inference()
