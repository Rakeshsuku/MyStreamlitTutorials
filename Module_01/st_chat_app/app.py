# Streamlit Data Editor App and enabling downloads
# To retain historic chat we need to save the chat to session_state.

# Core packages
import streamlit as st

# Additional packages
from gpt4all import GPT4All

model = GPT4All(model_name="orca-mini-3b.ggmlv3.q4_0.bin")

# Configuring the streamlit page must be the first activity in ur script:
st.set_page_config(
    layout="wide",
    page_title="Rakesh's App",
    page_icon=":smiley:",
    initial_sidebar_state="auto",
)

# Create a storage for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
if st.session_state.messages:
    # st.write(st.session_state.messages)
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

prompt = st.chat_input("Ask Something")

# Display messages
if prompt:
    with model.chat_session():
        # Add user prompt to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            response = model.generate(prompt=prompt, top_k=1)
            st.write(response)
        # with st.chat_message("Happy", avatar="🤗"):
        #     # avatar can be an image
        #     st.write("I am HuggingFace!")
