# Working with file downloads

# Core packages
import streamlit as st
import streamlit.components as stc

# Additional packages
import numpy as np
import pandas as pd
import base64
import time

timestr = time.strftime("%Y%m%d-%H%M%S")


# File downloads using a function
def text_downloader(raw_test):
    b64 = base64.b64encode(raw_test.encode()).decode()
    new_filename = "new_text_file_{}.txt".format(timestr)
    st.markdown("#### Download File ####")
    href = f'<a href="data:file/txt;base64, {b64}" download="{new_filename}">Click Here To Download!</a>'
    st.markdown(href, unsafe_allow_html=True)


def csv_downloader(data):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = "new_text_file_{}.csv".format(timestr)
    st.markdown("#### Download File ####")
    href = f'<a href="data:file/csv;base64, {b64}" download="{new_filename}">Click Here To Download!</a>'
    st.markdown(href, unsafe_allow_html=True)


# File downloads using a class


class FileDownloader:
    """docstring for FileDownloader
    >>> download = FileDownloader(data, filename, file_ext).download()
    """

    def __init__(self, data, filename="myfile", file_ext="txt"):
        self.data = data
        self.filename = filename
        self.file_ext = file_ext

    def download(self):
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = "{}_{}.{}".format(self.filename, timestr, self.file_ext)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/{self.file_ext};base64, {b64}" download="{new_filename}">Click Here To Download!</a>'
        st.markdown(href, unsafe_allow_html=True)


# Configuring the streamlit page must be the first activity in ur script:
st.set_page_config(
    layout="wide",
    page_title="Rakesh's App",
    page_icon=":smiley:",
    initial_sidebar_state="auto",
)


def main():
    menu = ["Home", "CSV", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home Page")
        my_text = st.text_area("Enter your text here:")
        if st.button("Save"):
            st.write(my_text)
            # text_downloader(my_text)
            FileDownloader(my_text, file_ext="txt").download()
    elif choice == "CSV":
        st.subheader("CSV Download Page")
        df = pd.read_csv(r"../data/iris.csv")
        st.dataframe(df)
        # csv_downloader(df)
        FileDownloader(df.to_csv(), file_ext="csv").download()
    else:
        st.subheader("About App")


if __name__ == "__main__":
    main()
