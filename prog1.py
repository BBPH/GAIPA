import streamlit as st
import openai
import base64
from openai import OpenAI

st.title(":blue[Assignment!]")
api_key = st.text_input(":blue[Api key!!]", type="password")
client = OpenAI(api_key=api_key)

