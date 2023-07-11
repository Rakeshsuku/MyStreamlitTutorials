# Streamlit Data Editor App and enabling downloads

# Core packages
import streamlit as st

# Additional packages
import numpy as np
import pandas as pd
import time

time_str = time.strftime("%Y%m%d_%H%M%S")

# Configuring the streamlit page must be the first activity in ur script:
st.set_page_config(
    layout="wide",
    page_title="Rakesh's App",
    page_icon=":smiley:",
    initial_sidebar_state="auto",
)


# Load data
def load_data(data_file):
    return pd.read_csv(data_file)


def main():
    st.title("Streamlit Data Editor")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Data Editor")
        data_file = st.file_uploader("Upload CSV file:", type=["csv"])
        if data_file is not None:
            df = load_data(data_file)
            with st.form(key="editor_form"):
                edited_df = st.data_editor(df)
                save_button = st.form_submit_button("Save Data")
                # st.write(type(data_file))
                # st.write(time_str)
            if save_button:
                new_file_name = f"{data_file.name}_{time_str}.csv"
                final_df = edited_df.to_csv()
                st.download_button(
                    label="Download Data as CSV",
                    data=final_df,
                    file_name=new_file_name,
                    mime="text/csv",
                )
    else:
        st.subheader("About App")


if __name__ == "__main__":
    main()
