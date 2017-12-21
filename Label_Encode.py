'''
Created on 15-Dec-2017

@author: Korah
'''
import pandas as pd
from sklearn.externals import joblib 

def LabelEncodedTransform(data,datapath, label_encoder_name):
    le = joblib.load(datapath + label_encoder_name)
    data_le = pd.DataFrame()
    for col in le:
        le_d = le[col]
        data_le[col] = le_d.transform(data[col])
    data_le= pd.concat([data_le, data.Rating], axis = 1)
    return data_le