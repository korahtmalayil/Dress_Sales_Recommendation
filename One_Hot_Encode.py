'''
Created on 15-Dec-2017

@author: Korah
'''
import pandas as pd
from sklearn.externals import joblib 

def OneHotTransform_test(X, datapath, one_hot_encoder_name, column_names_encoded):    
    one_hot_dict = joblib.load(datapath + one_hot_encoder_name) 
    column_name = joblib.load(datapath + column_names_encoded)     
    X_df = pd.DataFrame()  
    for col in one_hot_dict:    
        one_hot_encoding = one_hot_dict[col]
        temp = one_hot_encoding.transform(X_test[[col]])
        temp = pd.DataFrame(temp.toarray())
        temp = temp.set_index(X.index.values)
        X_df = pd.concat([X_df, temp], axis=1) 
    X_df = pd.concat([X_df, X.Rating], axis = 1)
    X_df.columns = column_name
    return X_df