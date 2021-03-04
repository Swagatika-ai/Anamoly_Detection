import streamlit as st
import os
import pandas as pd
import numpy as np
#import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

#from keras.models import load_model
#model = load_model('model.h5')
def main():
    st.title("Robust IOT-Based Predictive Maintenance Solution")
    #st.subheader("High Level Analysis")
    html_temp = """ 
    <div style="background.color:tomato;padding:15px;">
    <h2>An IoT-based Predictive Maintenance Architecture</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)


main()

from PIL import Image
image = Image.open("arch.png") 
st.image(image)

st.title("Process Manufacturing Dashboard")
image = Image.open("Dashboard1.png") 
st.image(image)

st.title("Predictive Maintenance App")
image = Image.open("Dashboard2.png") 
st.image(image)







Date_column="date"
DATA_PATH="processed_data1.csv"


@st.cache
def load_data(nrows):
    df = pd.read_csv(DATA_PATH,nrows=nrows)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    df["date"]=pd.to_datetime(df[Date_column],infer_datetime_format=True)
    return df

#data_load_state= st.text("loading...")
df = load_data(5000)




image = Image.open("states1.png") 
st.image(image)



 
