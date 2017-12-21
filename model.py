'''
Created on 15-Dec-2017

@author: Korah
'''

from .convert_input_to_df import convert_input_to_df
from .Label_Encode import LabelEncodedTransform
from .One_Hot_Encode import OneHotTransform_test
from .rf_classifier_pred import rf_classifier_pred
datapath = 'C:\\Users\\Korah\\Documents\\Data Science\\PGDBA\\1st Sem\\Accubits\\Dress Sales\\Dresses_Attribute_Sales\\API\\'
label_encoder_name = 'label_encoder_dict.pkl'
one_hot_encoder_name = 'OneHotEncoder_dict.pkl'
column_names_ohe = 'column_names_ohe.pkl'
input_file = 'df10_only_features.csv'
model_name = 'rf_classifier.pkl'

def final_answer(data):

    X = convert_input_to_df(data)
    X_le = LabelEncodedTransform(X, datapath, label_encoder_name)
    X_ohe = OneHotTransform_test(X_le, datapath, one_hot_encoder_name, column_names_ohe)
    y_pred = rf_classifier_pred(X_ohe, datapath, model_name)
    return y_pred