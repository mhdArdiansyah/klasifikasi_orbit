#import library

import streamlit as st
from web_functions import load_data

from Tabs import home, predict, visualise

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualisation" : visualise
}

#sidebar
st.sidebar.title("Navigasi")

#option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

#load dataset
df, x, y = load_data()

#kondisi
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df,x,y)
else:
    Tabs[page].app()