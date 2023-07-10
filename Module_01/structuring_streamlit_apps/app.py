import streamlit as st
from eda_app import eda_applet
from ml_app import ml_applet
import logging

# # Display logs in terminal
# # Format Option
# LOGS_FORMAT = "%(levelname)s %(asctime)s.%(msecs)03d - %(message)s"
# logging.basicConfig(level=logging.DEBUG, format=LOGS_FORMAT)
# logger = logging.getLogger(__name__)

# Save logs to a file and also display in terminal
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s %(asctime)s.%(msecs)03d - %(message)s")
# Log file
file_handler = logging.FileHandler("activity.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def main():
    st.title("Adding logging to streamlit App")
    st.text("Track all activities/pages visited of the App!")
    menu = ["Home", "EDA", "ML", "Analytics", "About"]
    choice = st.sidebar.selectbox(label="Menu", options=menu)
    if choice == "Home":
        st.subheader("Home Page")
        logger.info("Home Section")
    elif choice == "EDA":
        eda_applet()
        logger.info("EDA Section")
    elif choice == "ML":
        ml_applet()
        logger.info("ML Section")
    elif choice == "Analytics":
        st.subheader("Analytics Page")
        logger.info("Analytics Section")
    else:
        st.subheader("About App")
        logger.info("About Section")


if __name__ == "__main__":
    main()
