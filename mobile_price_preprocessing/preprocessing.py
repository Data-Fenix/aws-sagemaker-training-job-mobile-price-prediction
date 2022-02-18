import boto3
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)
import argparse
import os
import warnings
warnings.simplefilter(action='ignore')
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-test-split-ratio", type=float, default=0.3)
    args, _ = parser.parse_known_args()

    print("Received arguments {}".format(args))

    input_data_path = os.path.join("/opt/ml/processing/input", 'data.csv')

    print("Reading input data from {}".format(input_data_path))
    df = pd.read_csv(input_data_path)
    
    columns = ['Unnamed: 0', 'Brand me', 'Ratings', 'RAM', 'ROM', 
               'Mobile_Size', 'Primary_Cam', 'Selfi_Cam', 'Battery_Power', 'Price']

    df.columns = columns

    print("drop unnecessary columns")
    df.drop(['Unnamed: 0'], axis = 1, inplace = True)

    print("dealing with missing values")
    missing_var = ['Ratings', 'RAM', 'ROM', 'Mobile_Size', 'Selfi_Cam']

    df_missing= df[['Ratings', 'RAM', 'ROM', 'Mobile_Size', 'Selfi_Cam']]


    # If the variable has a missing value, this function will repalce that missing value by a random number (this random number will choose from the relavant variable) 
    def impute_nan_random(df,variable):
        df[variable+"_random"]=df[variable]
        ##It will have the random sample to fill the na
        random_sample=df[variable].dropna().sample(df[variable].isnull().sum(),random_state=0)
        ##pandas need to have same index in order to merge the dataset
        random_sample.index=df[df[variable].isnull()].index
        df.loc[df[variable].isnull(),variable+'_random']=random_sample

    for i in missing_var:
        impute_nan_random(df_missing,i)

    print('combining the datasets')
    df_new = pd.concat([df, df_missing[['Ratings_random', 'RAM_random', 'ROM_random', 'Mobile_Size_random',
           'Selfi_Cam_random']]], axis = 1)

    print("remove the unnecessary columns")
    df_new.drop(['Ratings', 'RAM', 'ROM', 'Mobile_Size','Selfi_Cam'], axis = 1, inplace = True)

    print("filtering the Brand me variable")
    df_new['Brand me'] = df_new['Brand me'].str.split(' ',1).str[0]

    df_new['Brand me'].value_counts()

    #Get the list of top 10 elements
    top10 = df_new['Brand me'].value_counts().index[:10]
    top10

    df_new['Brand me'] = np.where(df_new['Brand me'].isin(top10), df_new['Brand me'], 'Other')
    print(df_new['Brand me'].nunique())

    print("convert Brand me variable to categorical")
    df_new['Brand me'] = df_new['Brand me'].astype('category')

    print("rename the columns using a dictionary")
    df_new['Brand me'] = df_new['Brand me'].cat.rename_categories({'Apple': 11, 
                                                                   'Samsung': 10, 
                                                                   'Vivo': 9, 
                                                                   'OPPO': 8, 
                                                                   'Other': 7, 
                                                                   'Nokia': 6, 
                                                                   'Lava': 5,
                                                                   'Micax': 4, 
                                                                   'Karbonn': 3, 
                                                                   'I': 2,
                                                                   'Kechaoda':1
                                                                  })


    X = df_new[['Brand me', 'Primary_Cam', 'Battery_Power', 'Ratings_random',
           'RAM_random', 'ROM_random', 'Mobile_Size_random', 'Selfi_Cam_random']]
    y = df_new['Price']

    print("standarisation: We use the Standardscaler from sklearn library")
    
    scaler=StandardScaler()
    ### fit vs fit_transform
    X=scaler.fit_transform(X)

    print("split the dataset")
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
    
    print("Saving the outputs")
    X_train_output_path = os.path.join("/opt/ml/processing/train-x", "X_train.csv")   
        
    print("Saving output to {}".format(X_train_output_path))
    pd.DataFrame(X_train).to_csv(X_train_output_path, header=False, index=False)
    
    X_test_output_path = os.path.join("/opt/ml/processing/test-x", "X_test.csv")   
        
    print("Saving output to {}".format(X_test_output_path))
    pd.DataFrame(X_test).to_csv(X_test_output_path, header=False, index=False)

    y_train_output_path = os.path.join("/opt/ml/processing/train-y", "y_train.csv")   
        
    print("Saving output to {}".format(y_train_output_path))
    pd.DataFrame(y_train).to_csv(y_train_output_path, header=False, index=False)
    
    y_test_output_path = os.path.join("/opt/ml/processing/test-y", "y_test.csv")   
        
    print("Saving output to {}".format(y_test_output_path))
    pd.DataFrame(y_test).to_csv(y_test_output_path, header=False, index=False)

    print("successfully completed the dataset")
