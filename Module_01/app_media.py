# Working with media files

# Core packages
import streamlit as st

# Additional packages
from PIL import Image

img = Image.open(r"../data/tiger.jpg")
st.image(img, use_column_width=True)

# from url
st.image(
    "https://media.istockphoto.com/id/108348088/photo/red-eyed-tree-frog.jpg?s=1024x1024&w=is&k=20&c=9uITWNlQ7R7_Wf6njqbQSsxiBE82uzJP5mekRDTYgco="
)

# Display video
# video_file = open(<path-to-video-file.mp4>, "rb").read()
# st.video(video_file)


# # Add audio file
# # audio_file = open(<path-to-audio_file.mp3>, "rb").read()
# st.audio(audio_file)
