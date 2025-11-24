import streamlit as st
import openai
import base64
from openai import OpenAI
#https://3amtgxmdtwyym69bwahkyv.streamlit.app/

st.title(":blue[Chat!]")
client = st.session_state.get("client", None)

if client is None:
    st.stop()

@st.cache_data
def gpt(prompt):
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )
    return response.output_text


if "record" not in st.session_state:
    st.session_state["record"] = []

if st.button("Clear!!"):
    del st.session_state["record"]

if prompt := st.chat_input("Say something!!!"):
    st.session_state["record"].append({"role":"user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    response = gpt(st.session_state["record"])
    st.session_state["record"].append({"role":"assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)