#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun oct 23 15:02:29 2022

@author: Shaheer
"""
#Software Development
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('classifer.pkl', 'rb')
classifer = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(AGE,CUS_Month_Income,CUS_Gender,CUS_Marital_Status,YEARS_WITH_US,total_debit_amount,total_credit_amount,CUS_Target,TAR_Desc):  
   
    prediction = classifer.predict(
        [[AGE,CUS_Month_Income, CUS_Gender, CUS_Marital_Status,YEARS_WITH_US,total_debit_amount,total_credit_amount,CUS_Target,TAR_Desc]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("BANK Preduction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:white;padding:13px">
    <h1 style ="color:black;text-align:center;">BEPEC July Batch Classifier ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    AGE = st.text_input("AGE", "Type Here")
    CUS_Month_Income= st.text_input("CUS_Month_Income", "Type Here")
    CUS_Gender = st.text_input("CUS_Gender", "Type Here")
    CUS_Marital_Status = st.text_input("CUS_Marital_Status", "Type Here")
    YEARS_WITH_US=st.text_input("YEARS_WITH_US","Type Here")
    total_debit_amount=st.text_input("total debit amount","Type Here")
    total_credit_amount=st.text_input("total credit amount","Type Here")
    CUS_Target=st.text_input("CUS_Target","Type Here")
    TAR_Desc=st.text_input("TAR_Desc","Type Here")
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(AGE,CUS_Month_Income,CUS_Gender,CUS_Marital_Status,YEARS_WITH_US,total_debit_amount,total_credit_amount,CUS_Target,TAR_Desc)
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()