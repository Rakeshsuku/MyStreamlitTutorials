# Working with plots usings Plotly

# Core packages
import streamlit as st

# Additional packages
import numpy as np
import pandas as pd
import plotly.express as px

# Configuring the streamlit page must be the first activity in ur script:
st.set_page_config(
    layout="wide",
    page_title="Rakesh's App",
    page_icon=":smiley:",
    initial_sidebar_state="auto",
)


def main():
    st.title("Plottin in Streamlit with Plotly 🤗🫶")
    df = pd.read_csv(r"data/prog_languages_data.csv")
    st.dataframe(df, width=300, height=300)
    # Pie Chart
    fig = px.pie(
        df, values="Sum", names="lang", title="Pie Chart of Programming Languages"
    )
    st.plotly_chart(fig)
    # Bar Chart
    fig2 = px.bar(df, x="lang", y="Sum", title="Bar chart of Programming Languages")
    st.plotly_chart(fig2)


if __name__ == "__main__":
    main()
