# Basics and Fundamentals

# Core packages
import streamlit as st

# Working with Text files
st.text("Hello World from Module_01!")
st.text("This is super cool!")

# Header
st.header("This is a header.")
st.subheader("This is a sub-header.")

# Title
st.title("This is a title.")

# Markdown
st.markdown("This is markdown for a link to [index file](index.html).")

# Displaying colored text
st.success("Successful!")
st.warning("Danger")
st.info("This is information")
st.error("This is an Error!")
st.exception("This is an Exception")


# Super function
st.write("This is a text written by st.write")
st.write("## This is markdown with st.text")
st.write(1 + 2)

import math

st.write(math.pow(5, 3))

st.help(range)

st.write(dir(st))
