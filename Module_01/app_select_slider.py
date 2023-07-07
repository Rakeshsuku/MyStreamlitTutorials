# Working with Select/Multiselect, Sliders and Select sliders

# Core packages
import streamlit as st

# Select/Multiselects
my_langs = ["Python", "Julia", "Go", "Rust"]

choice = st.selectbox("Language", my_langs)
st.write(f"You selected {choice}!")

# Multi select
spoken_langs = ("English", "Hindi", "Tamil", "Malayalam")
my_spoken_langs = st.multiselect("Spoken Languages", spoken_langs, default="English")

# Slider
age = st.slider("Age", 18, 100, 23)

# Select Slider
colors = st.select_slider(
    "Choose Colors:",
    options=["red", "yellow", "blue", "green"],
    value=["red", "yellow"],
)
