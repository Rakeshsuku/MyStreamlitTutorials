# Working with file uploads

# Core packages
import streamlit as st

# Additional packages
import numpy as np
import pandas as pd
from PIL import Image
import pandas as pd
import docx2txt
from pathlib import Path

# from PyPDF2 import PdfFileReader
# import pdfplumber

# import textract


# Load Image
@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img


# function to save uploaded file
def save_uploaded_file(file_obj, dir_path=r"./uploaded_files/"):
    dir_path = Path(dir_path)
    dir_path.mkdir(exist_ok=True)
    with open((dir_path / file_obj.name).as_posix(), "wb") as f:
        f.write(file_obj.getbuffer())
    st.success("File {} saved successfully!".format(file_obj.name))


def main():
    st.title("File Upload Tutorial.. 🤗🫶")
    menu = ["Home", "Dataset", "DocumentFile", "Upload Multiple Files", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Image:", type=["png", "jpg", "jpeg"])
        if image_file is not None:
            # Display image details
            # st.write(type(image_file))
            # st.write(dir(image_file))
            if st.button("Process"):
                file_details = {
                    "filename": image_file.name,
                    "filetype": image_file.type,
                    "filesize": image_file.size,
                }
                st.write(file_details)
                st.image(load_image(image_file), width=750)
                # Saving image file:
                with open(r"./uploaded_files/{}".format(image_file.name), "wb") as f:
                    f.write(
                        image_file.getbuffer(),
                    )
                    st.success("Image Saved!")
    elif choice == "Dataset":
        st.subheader("Dataset")
        csv_file = st.file_uploader(
            "Upload CSV",
            type=[
                "csv",
            ],
        )
        if csv_file is not None:
            file_details = {
                "filename": csv_file.name,
                "filetype": csv_file.type,
                "filesize": csv_file.size,
            }
            st.write(file_details)
            st.dataframe(pd.read_csv(csv_file))
    elif choice == "DocumentFile":
        st.subheader("DocumentFile")
        doc_file = st.file_uploader("Upload Document:", type=["pdf", "docx", "txt"])
        if doc_file is not None:
            if st.button("Process"):
                file_details = {
                    "filename": doc_file.name,
                    "filetype": doc_file.type,
                    "filesize": doc_file.size,
                }
                st.write(file_details)
                if doc_file.type == "text/plain":
                    # # Read as bytes
                    # raw_text = doc_file.read()
                    # st.write(raw_text)  # Displays the byte string.
                    # # st.text - does not work with byte string

                    # Read as text
                    text_data = doc_file.read().decode(encoding="utf-8")
                    st.text(text_data)
                elif doc_file.type == "application/pdf":
                    try:
                        with pdfplumber.open(doc_file) as pdf:
                            pages = pdf.pages[0]
                            st.write(pages.extract_text())
                    except:
                        st.write("Unable to open pdf file!")
                else:
                    raw_text = docx2txt.process(doc_file)
                    st.write(raw_text)
                save_uploaded_file(doc_file)
    elif choice == "Upload Multiple Files":
        st.subheader("Upload Multiple Files")
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
