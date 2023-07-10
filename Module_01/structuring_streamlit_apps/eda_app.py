import streamlit as st

import pandas as pd


@st.cache_data
def read_data(path):
    return pd.read_csv(path)


def eda_applet():
    st.subheader("EDA Applet")
    # Read data
    df = read_data(path=r"../data/iris.csv")
    st.success("Input data read")
    st.dataframe(df)
