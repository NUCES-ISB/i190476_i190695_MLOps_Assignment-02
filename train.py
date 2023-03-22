# importing the required libraries
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from sklearn.svm import SVR
from joblib import dump
import pandas as pd

# reading the data from .csv into dataframe
df = pd.read_csv("live_stream_training_data.csv")

# dropping the "Date" column
df = df.drop(['Date'], axis=1)
df = df.drop(['Ticker'], axis=1)

# dropping null values
df = df.dropna()

# Seperating the data for training
y_train = df["Close"].values
X_train = df.drop(['Close'], axis=1)
X_train = X_train.values

 # Data normalization (0,1)
X_train = preprocessing.normalize(X_train, norm='l2')

# Linear Regression algorithm
clf_LR = LinearRegression()
clf_LR.fit(X_train, y_train)
dump(clf_LR, "MODEL_LR")
print("Training LR score and regression:")
print(clf_LR.score(X_train, y_train))
predicted = clf_LR.predict(X_train)
print(predicted)

# Support Vector Regressor(SVR) algorithm
clf_SVR = SVR(kernel='rbf')
clf_SVR.fit(X_train, y_train)
dump(clf_SVR, "SVR_MODEL")
print("Training SVR score and regression:")
print(clf_SVR.score(X_train, y_train))
predicted = clf_SVR.predict(X_train)
print(predicted)

# Random Forest Regressor algorithm
clf_rfr = RandomForestRegressor()
clf_rfr.fit(X_train, y_train)
dump(clf_rfr, "RFR_MODEL")
print("Training RFR score and regression:")
print(clf_rfr.score(X_train, y_train))
predicted = clf_rfr.predict(X_train)
print(predicted)

