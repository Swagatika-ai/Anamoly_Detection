import streamlit as st
import joblib ,os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# from keras.models import load_model
# model = load_model('model.h5')
def main():
    st.title("Anamoly Detecion")
    st.subheader("High Level Analysis")
    html_temp = """ 
    <div style="background.color:tomato;padding:15px;">
    <h2>Predicting Machines failures</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)


main()

Date_column="date"
DATA_PATH="processed_data1.csv"


@st.cache
def load_data(nrows):
    df = pd.read_csv(DATA_PATH,nrows=nrows)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    df["date"]=pd.to_datetime(df[Date_column],infer_datetime_format=True)
    return df

data_load_state= st.text("loading...")
df = load_data(5000)

from PIL import Image


image = Image.open("s.png") 
st.image(image)
st.subheader("As can be seen there are a pattern being captured by the sensors")

# filter = st.slider('hour',0,23,15)
# filtered_data = df[df["date"].dt.hour == filter]
# #st.subheader("all anamolies %s:00" %filter)
# st.line_chart(filtered_data)

image = Image.open("states1.png") 
st.image(image)

#st.write(df.head())
fig, ax = plt.subplots()
sns.heatmap(df.corr(), ax=ax)
st.write(fig)
st.text("We can see strongly correlated group of sensors - from sensor_18 to sensor_26. There also some other correlated groups but not as strong as the mentioned one!!!") 



