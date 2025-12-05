import streamlit as st
import json
from streamlit_lottie import st_lottie
import requests
st.set_page_config(
    page_title="Future You",
    layout="wide"
)

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.imgur.com/pitcZU3.jpeg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

st.title("Welcome to :red[Future You] ")
st.subheader("To LOGIN/SIGNUP")
st.page_link("pages/LOGIN.py",icon='➡️')
st.subheader("To know about Future You")
st.page_link("pages/ABOUT.py", icon='🕵')
st.subheader("For Contact Details")
st.page_link("pages/CONTACT.py", icon='📞')
