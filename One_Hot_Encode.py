'''
Created on 15-Dec-2017

@author: Korah
'''
import pandas as pd
from sklearn.externals import joblib 

def OneHotTransform_test(X_test, datapath, one_hot_encoder_name, column_names_ohe):    
    ohe_dict = joblib.load(datapath + one_hot_encoder_name) 
    column_name = joblib.load(datapath + column_names_ohe)     
    X_test_1 = pd.DataFrame()  
    for col in ohe_dict:    
        ohe = ohe_dict[col]
        temp = ohe.transform(X_test[[col]])
        temp = pd.DataFrame(temp.toarray())
        temp = temp.set_index(X_test.index.values)
        X_test_1=pd.concat([X_test_1,temp],axis=1) 
    X_test_1 = pd.concat([X_test_1, X_test.Rating], axis = 1)
    X_test_1.columns = column_name
    return X_test_1