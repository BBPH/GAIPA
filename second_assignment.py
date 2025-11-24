import streamlit as st
import openai
import base64
from openai import OpenAI
#https://3amtgxmdtwyym69bwahkyv.streamlit.app/

if 'api_key' not in st.session_state:
    st.session_state["api_key"] = ''

st.title(":blue[Assignment!]")
api_key = st.text_input(":blue[Api key!!]", type="password", value=st.session_state["api_key"])

if api_key:
    st.session_state["api_key"] = api_key
    client = OpenAI(api_key=api_key)
    st.session_state["client"] = client
    st.write("Input complete!!!")

prompt = st.text_input(":blue[Prompt!!!!]")

@st.cache_data
def gpt(prompt):
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )
    return response.output_text

if st.button(":blue[Generate!!!!!]"):
    if prompt.strip()=="":
        st.warning(":red[Write Properly.]")
    else:
        answer = gpt(prompt)
        st.write(answer)