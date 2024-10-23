import streamlit as st

import pandas as pd

import plotly.express as px

import matplotlib.pyplot as plt

st.title(" Ahoj Svet a Streamlit")

st.write(

    "Toto je moja prvá aplikácia v Streamlite"

)

data = pd.DataFrame({

    "Kategorie" : ["A", "B", "C", "D"],
    "Hodnoty" : [25, 40, 35, 30]

})

st.write("Tabuľka s dátami:")

st.dataframe(data)

fig = px.bar(

    data, x ="Kategorie", 
    y = "Hodnoty", 
    title = "Stlpcovy graf plotly"

)

st.plotly_chart(fig)

if st.button("Infomacne okno"):
    st.info("Toto je informacne okno")

if st.button("Upozornovacie okno"):
    st.warning("Toto je upozornovacie okno")

if st.button("Chybove okno"):
    st.error("Toto je chybove okno")




