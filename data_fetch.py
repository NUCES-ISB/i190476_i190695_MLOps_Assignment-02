# import required libraries
from psx import stocks
import datetime

# function to get live data from stream in .csv file for training of ML Model
def get_training_data():
    try:
        # getting the live data from the stocks of the given banks till 28/02/2023
        data = stocks(["SILK", "UBL", "AKBL", "HBL", "SNBL", "BIPL", "JSBL"],
                    start=datetime.date(2015, 1, 1), end=datetime.date(2023, 2, 28))
        # removing the null data
        data.dropna()
        # saving the data in .csv files
        data.to_csv("live_stream_training_data.csv", mode='w')
        # reading the data to do some initial
    except:
        print("Unable to get the data atm!")

# function to get the dataframe for testing the model
def get_dataframe_for_testing():
    try:
        # getting the live data from the stocks of the given banks till today
        data = stocks(["SILK", "UBL", "AKBL", "HBL", "SNBL", "BIPL", "JSBL"],
                        start=datetime.date(2023, 3, 1), end=datetime.date.today())
        # removing the null data
        data.dropna()
        # saving the data in .csv files
        data.to_csv("live_stream_test_data.csv", mode='w')
    except:
        print("Unable to get the data atm!")

# function to get the training data in .csv file
def main():
    get_training_data()

if __name__ == "__main__":
    main()