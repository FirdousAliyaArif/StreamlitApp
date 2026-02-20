import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import matplotlib.pyplot as plt
import numpy as np


st.title("ML Model")
st.header("Preddiction System")
st.subheader("Enter input below")
st.write("This app demonstrates Ml model deployment")
name = st.text_input("Enter Customer name")
age = st.number_input("Enter customer age")
salary =  st.slider("Select salary", 10000, 100000)
gender = st.selectbox("select user gender", ["Male","Female"])
education =  st.radio("education Level", ["UG", "PG", "PHD"])
agree = st.checkbox("I AGREE TO THE HEREBY AFORE MENTIONED TERMS AND CONDITIONS")
uploaded_files = st.file_uploader("upload Image", type=["jpg","png"])
if st.button("predict"):
        st.success("Prediction Successful")
        st.warning("Warning")
        st.error("Error enter valid input")

df = pd.DataFrame({"A": [1,2], "B": [3,4]})
st.dataframe(df)
appointment = st.date_input("Select Appointment date")
st.write("Appointment date:", appointment)

import streamlit as st

time = st.time_input("Select Appointment Time")
st.write("Appointment Time:", time)

st.metric("Accuracy", "92%", "+2%")
st.image("peacockk.jpeg", caption = "Peacock")
#st.audio("<audo file name>")
#st.video("<video file name>")
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose page", ["Home", "Prediction"])

#Layout Control
col1, col2 = st.columns(2)
with col1:
    st.write("Left")
with col2:
    st.write("Right")

#Progress & spinners (ML/DL mopdels)
with st.spinner("processing......"):
    st.progress(50)

#catching model
#prevents reloading the model
#@st.cache_resource

#def load_model():
#    return joblib.load("model.pkl")

#model  = load_model()

#Displaying a dataframe
data = {
    'Name': ['cheongmyung', 'baekcheon','yoo iseol', 'yunjong', 'jogeol'],
    'Age': [80, 30, 28, 20, 19],
    'City': ['Third-grade disciple(Senior disciple)', 'Second-grade disciple', 'Second-grade disciple', 'Third-grade disciple', 'Third-grade disciple']
}
df = pd.DataFrame(data)
st.dataframe(df)

rand = np.random.normal(1, 2, size = 20)
fig, ax = plt.subplots()
ax.hist(rand, bins = 15,color = "blue")
st.pyplot(fig)





