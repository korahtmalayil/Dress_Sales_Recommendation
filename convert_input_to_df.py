'''
Created on 21-Dec-2017

@author: Korah
'''
import pandas as pd

def convert_input_to_df(text):   
    label_dict = 'Style,Price,Rating,Size,Season,NeckLine,SleeveLength,WaistLine,Material,Pattern Type'
    label_dict_split = label_dict.split(',')
    text_split = text.split(',')        
    df_dict = {label_dict_split[i]:text_split[i] for i in range(0,len(label_dict_split))} 
    df = pd.DataFrame.from_dict(df_dict, orient='index')
    return df.transpose()
    