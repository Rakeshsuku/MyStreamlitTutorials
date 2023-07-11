# Clearing forms on submit

# Core packages
import streamlit as st

# Additional packages
import numpy as np
import pandas as pd

# Configuring the streamlit page must be the first activity in ur script:
st.set_page_config(
    layout="wide",
    page_title="Rakesh's App",
    page_icon=":smiley:",
    initial_sidebar_state="auto",
)


def main():
    st.subheader("Home")
    with st.form(key="form1", clear_on_submit=True):
        first_name = st.text_input("First Name:")
        last_name = st.text_input("Last Name:")
        msg = st.text_area("Message:")
        submit_btn = st.form_submit_button("Submit")
        if submit_btn:
            st.success(
                'Hi {} {}\n\nYour message:\n\n"{}"'.format(first_name, last_name, msg)
            )


if __name__ == "__main__":
    main()
