import streamlit as st
import openai
import base64
from openai import OpenAI

st.title(":blue[Assignment!]")
api_key = st.text_input(":blue[Api key!!]", type="password")
client = OpenAI(api_key=api_key)
prompt = st.text_input(":blue[Prompt!!!]", type="default")

if st.button(":blue[Generate!!!!]"):
    img = client.images.generate(
        model="gpt-image-1-mini",
        prompt=prompt
        )

    image_bytes = base64.b64decode(img.data[0].b64_json)
    st.image(image_bytes)

if prompt:
    response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
    )
    st.write(response.output_text)