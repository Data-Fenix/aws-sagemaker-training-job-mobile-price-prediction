#Import the neccessary libaries in here
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import argparse
import pickle
import boto3
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import numpy as np


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-test-split-ratio", type=float, default=0.3)
    args, _ = parser.parse_known_args()

    print("Received arguments {}".format(args))
    training_data_directory = '/opt/ml/input/data/train-x/'
    training_data_directory2 = '/opt/ml/input/data/train-y/'
    testing_data_directory = '/opt/ml/input/data/test-x/'
    testing_data_directory2 = '/opt/ml/input/data/test-y/'
    X_train_directory = os.path.join(training_data_directory, "X_train.csv")
    y_train_directory = os.path.join(training_data_directory2, "y_train.csv")
    X_test_directory = os.path.join(testing_data_directory, "X_test.csv")
    y_test_directory = os.path.join(testing_data_directory2, "y_test.csv")
    
    print("Reading input data")
    print("Reading input data from {}".format(X_train_directory))
    X_train = pd.read_csv(X_train_directory, header = None)
    
    print("Reading input data from {}".format(y_train_directory))
    y_train = pd.read_csv(y_train_directory, header = None)
    
    print("Reading input data from {}".format(X_test_directory))
    X_test = pd.read_csv(X_test_directory, header = None)
    
    print("Reading input data from {}".format(y_test_directory))
    y_test = pd.read_csv(y_test_directory, header = None)
    
    print("renaming columns")
    X_columns = ['Brand me', 'Primary_Cam', 'Battery_Power', 'Ratings_random',
           'RAM_random', 'ROM_random', 'Mobile_Size_random', 'Selfi_Cam_random']
    
    X_train.columns = X_columns
    X_test.columns = X_columns
    
    y_column = ['Price']
    
    y_train.columns = y_column
    y_test.columns = y_column
    
    print("Successfully rename the dataset")
    
    
    #############
    print("start the model training")
    reg = RandomForestRegressor()
    reg.fit(X_train,y_train.values.ravel())

    print("predicting the results")
    y_pred = reg.predict(X_test)

    print("training score")
    print("Training Accuracy:",reg.score(X_train,y_train)*100)

    print("testing score")
    print("Testing Accuracy:",reg.score(X_test,y_test)*100)

    print('MAE:', metrics.mean_absolute_error(y_test, y_pred))
    print('MSE:', metrics.mean_squared_error(y_test, y_pred))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    ########
    
    OUTPUT_DIR = "/opt/ml/model/"
    
    print("Saving model....")
            
    print("Saving model....")
    path = os.path.join(OUTPUT_DIR, "temp_dict.pkl")
    print(f"saving to {path}")
    with open(path, 'wb') as p_file:
        pickle.dump(reg, p_file)
            
    print('Training Job is completed.')
