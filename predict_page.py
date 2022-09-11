
import streamlit as st
import pickle  
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data=load_model()


def show_predict_page():
    st.title("Cardiovascular Detection")
    st.write("""We need some information to predict the disease""")
    st.write("""So please enter some information about you""")


    # gender={
    # "male",
    # "Female",
    # }

    # cholestrol={
    #     "Normal",
    #     "Above Normal",
    #     "Well Above Normal",
    # }

    # glucose={
    #     "Normal",
    #     "Above Normal",
    #     "Well Above Normal",
    # }
    gender=(1,2)
    cholestrol=(1,2,3)
    glucose=(1,2,3)
    Smoke=(0,1)
    alco=(0,1)
    active=(0,1)
    age=st.number_input("Enter your age")
    Gender=st.selectbox("Gender",gender)
    weight=st.number_input("Enter your weight in(KG)")
    api_hi=st.number_input("Systolic Blood Pressure")
    api_lo=st.number_input("Dystolic Blood Pressure")
    Chol=st.selectbox("Enter your Cholestrol level",cholestrol)
    Glucose=st.selectbox("Enter your Glucose level",glucose)
    smoke=st.selectbox("Smoking",Smoke)
    Alco=st.selectbox("Alchole intake",alco)
    Active=st.selectbox("Physical Activity",active)



    ok=st.button("Prediction")
    if ok:
        X=data[[age,Gender,api_hi,api_lo,Chol,Glucose,smoke,Alco,Active]]
    