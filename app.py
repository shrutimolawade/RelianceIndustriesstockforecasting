# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:25:18 2023

@author: Tushar
"""

import pickle
import streamlit as st
import datetime
import pandas as pd
import numpy as np


st.title("Reliance Industries Stock Prediction :chart_with_upwards_trend:")

load = open('model.pkl','rb')
model = pickle.load(load)

    
Start_Date = st.sidebar.date_input("Start Date", datetime.date(2023,1,1))
End_Date = st.sidebar.date_input("End Date", datetime.date(2023,12,31))
Date = pd.date_range(Start_Date,End_Date)
Time = np.arange(5755,5755+len(Date))
    
    
data = {
        'Date' : Date,
        't' : Time
        }
    
features = pd.DataFrame(data)
st.write(features)
    

st.subheader('Press below to get predicted prices')
if st.button('Predict'):
    result = model.predict(features['t'])
    result = round(np.exp(result))
    features['Pred_Adj_Close'] = result
    st.write(features)
    st.line_chart(data=(features), x=('Date'), y=('Pred_Adj_Close'))

    