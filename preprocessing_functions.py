import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

import joblib


# Individual pre-processing and training functions
# ================================================

def load_data(df_path):
    # Function loads data for training
    return pd.read_csv(df_path)



def divide_train_test(df, target):
    # Function divides data set in train and test
    X_train, X_test, y_train, y_test = train_test_split(df.drop('survived', axis=1),  # predictors
    					data[target],  # target
    					test_size=0.2,  # percentage of obs in test set
    					random_state=0)  # seed to ensure reproducibility

    



def extract_cabin_letter(df, var):
    # captures the first letter
    return df[var].str[0]
    



def add_missing_indicator(df, var):
    # function adds a binary missing value indicator
    return np.where(df[var].isnull(), '1','0')


    
def impute_na(df,var):
    # function replaces NA by value entered by user
    # or by string Missing (default behaviour)
    return data[var].replace(np.nan,'Missing')



def remove_rare_labels(df,var,frequent_ls):
    # groups labels that are not in the frequent list into the umbrella
    # group Rare
    return np.where(df[var].isin(frequent_ls), df[var], 'Rare')



def encode_categorical(df, var):
    # adds ohe variables and removes original categorical variable
    
    df = df.copy()
    
    pass



def check_dummy_variables(df, dummy_list):
    
    # check that all missing variables where added when encoding, otherwise
    # add the ones that are missing
    df = pd.concat([df,
                    pd.get_dummies(df[var], prefix=var, drop_first=True)
                    	], axis=1)
    
    df.drop(labels=[var], axis=1, inplace=True)

    return df
    

def train_scaler(df, output_path):     
    scaler = StandardScaler()
    scaler.fit(df)
    joblib.dump(scaler, output_path)
    return scaler
    

def scale_features(df, output_path):
    # load scaler and transform data
    scaler = joblib.load(scaler) # with joblib probably
    return scaler.transform(df)



def train_model(df, target, output_path):
    # initialise the model
    lr =  LogisticRegression(C=0.0005, random_state=0)
    
    # train the model
    lr.fit(df, target)
    
    # save the model
    joblib.dump(lr, output_path)
    
    return None




def predict(df, model):
    # load model and get predictions
    model = joblib.load(model)
    return model.predict(df)

