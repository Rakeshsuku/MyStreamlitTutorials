# Configure Streamlit page

# Core packages
import streamlit as st


# Configuring the streamlit page must be the first activity in ur script:
st.set_page_config(layout="wide", page_title="Rakesh's App", page_icon=":smiley:")


def main():
    st.title("Hello Streamlit Lovers..!")
