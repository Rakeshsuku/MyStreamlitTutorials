# Basics and Fundamentals

# Core packages
import streamlit as st

# Additional packages
import pandas as pd
import numpy as np

# Display Data
df = pd.read_csv(r"../data/iris.csv")
# display as pandas dataframe
# st.dataframe(df)

# adding a color style from pandas dataframe
# st.dataframe(df.style.highlight_max(axis=0))

# display as static table
# st.table(df)

# using st.write
st.write(df.head())

# Display JSON Data
st.json({"data": "name", "values": [1, 2, 3, 4, 5]})

# Display code
mycode = """
def say_hello(name):
    st.text(f"Hello {name}!")
"""

st.code(mycode, language="python")

mycode1 = """
def say_hello(name):
    st.text(f"Hello {name}!")
end
"""
st.code(mycode1, language="ruby")
