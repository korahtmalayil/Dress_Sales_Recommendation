'''
Created on 15-Dec-2017

@author: Korah
'''
from sklearn.externals import joblib 

def rf_classifier_pred(X, datapath, model_name):
    rf_classifier = joblib.load(datapath + model_name)
    y_pred = rf_classifier.predict(X)
    return y_pred