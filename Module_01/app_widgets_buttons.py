# Working with Widgets
# Buttons, radio, select and checkbox

# Core packages
import streamlit as st

# working with buttons
name = "Rakesh"
if st.button("Say Hello"):
    st.write(f"Hello {name}!")

if st.button("Say Hello", key="world"):
    st.write(f"Hello World!")

# Working with radio buttons
status = st.radio("What is your status?", ("Active", "Inactive", "Sleep"))
if status == "Active":
    st.success("You are active!")
elif status == "Inactive":
    st.warning("You are inactive!")
else:
    st.error("You are sleeping")

# Working with checkboxes
if st.checkbox("Show/Hide"):
    st.write("Showing hidden content!")

# Working with expander
with st.expander("Python", expanded=False):
    st.write("Showing expanded text:")
    st.success("Hello Python!")

st.help(st.expander)
