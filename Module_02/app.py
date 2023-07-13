# Plotting in Streamlit``

# Core package
import streamlit as st

# Additional packages
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mpl.use("Agg")


# Configuring the streamlit page must be the first activity in ur script:
st.set_page_config(
    layout="wide",
    page_title="Rakesh's App",
    page_icon=":smiley:",
    initial_sidebar_state="auto",
)


def main():
    """All your code goes here"""
    st.title("Plotting with st.pyplot")
    df = pd.read_csv("../Module_01/data/iris.csv")

    st.dataframe(df.head())

    # # Previous method - Not thread safe
    # df["species"].value_counts().plot(kind="bar")
    # st.pyplot()

    # Recommended method
    fig, ax = plt.subplots(2, 1)
    df["species"].value_counts().plot(kind="bar", ax=ax[0])
    ax[1].scatter(df.sepal_length, df.sepal_width)
    st.pyplot(fig)

    st.subheader("Using plt.gcf() to get current figure.")
    df["species"].value_counts().plot(kind="bar")
    st.pyplot(plt.gcf())

    st.subheader("Using seaborn.")
    fig = plt.figure()
    sns.countplot(x=df["species"])
    st.pyplot(fig)

    st.subheader("Using st.bar_chart which uses altair.")
    st.bar_chart(df[["sepal_length", "sepal_width"]])

    st.subheader("Using st.line_chart which uses altair.")
    df2 = pd.read_csv("../Module_01/data/lang_data.csv")
    st.dataframe(df2.head())
    lang_choice = st.selectbox("Programming Language", df2.columns[1:])
    st.line_chart(data=df2, x="Week", y=lang_choice)


if __name__ == "__main__":
    main()
