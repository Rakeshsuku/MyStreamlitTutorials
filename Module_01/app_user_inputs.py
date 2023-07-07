# Working with inouts

# Core packages
import streamlit as st

# Text input
fname = st.text_input(
    "Enter filename:",  # max_chars=10
)
st.title(fname)

# Text Area
msg = st.text_area("Write a message:", height=200, max_chars=300)
st.write(msg)

# Numbers
num = st.number_input("Enter Number:", min_value=1, max_value=50, step=2, value=10)
st.text(f"Provided number is {num}")

# Float
fnum = st.number_input("Enter float:", min_value=10.0, max_value=25.0)

# Date Input
myappointment = st.date_input("Appointment Date")
st.text(f"Appointment date: {myappointment}")

# Time Input
myappointmenttime = st.time_input("Appointment Time")
st.text(f"Appointment date: {myappointmenttime}")

pswd = st.text_input("Enter password:", type="password")

# Color picker
color = st.color_picker("Select Color:")
