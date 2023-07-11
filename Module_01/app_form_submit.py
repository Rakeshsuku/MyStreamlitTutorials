# Working with Streamlit Forms

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
    st.title("Streamlit Forms and Salary Calculator")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Forms Tutorial")
        # Salary Calculator
        with st.form(key="salary_calc"):
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                hourly_rate = st.number_input("Enter hourly wage rate:")
            with col2:
                hrs_per_week = st.number_input(
                    "Enter weekly working hours:",
                    min_value=1,
                    max_value=100,
                    value=40,
                    step=1,
                )
            with col3:
                st.text("Salary")
                submit_salary = st.form_submit_button(label="Calculate")
        if submit_salary:
            with st.expander("Results:"):
                daily = hourly_rate * hrs_per_week / 5
                weekly = hourly_rate * hrs_per_week
                monthly = weekly * 4
                df = pd.DataFrame(
                    {
                        "hourly": hourly_rate,
                        "daily": daily,
                        "weekly": weekly,
                        "monthly": monthly,
                    },
                    index=["Salary (in $)"],
                )
                st.dataframe(df.T)
        # Method 1: Using Context Manager
        with st.form(key="form1"):
            firstname = st.text_input("First Name:")
            lastname = st.text_input("Last Name:")
            dob = st.date_input("Date of Birth")
            # Add submit button
            submit_button = st.form_submit_button(label="Sign Up!")
        # Results can be either inside the with context or outside it.
        if submit_button:
            st.success("Hello {} you have created an account.".format(firstname))
        # Method 2
        form2 = st.form(key="form2")
        username = form2.text_input("Username:")
        jobtype = form2.selectbox("Job", ["Developer", "Data Scientist", "Doctor"])
        submit_button2 = form2.form_submit_button(label="Login")
        if submit_button2:
            st.text("Hi {}\nYou are now logged-in!".format(username))
    else:
        st.subheader("About App")
    pass


if __name__ == "__main__":
    main()
