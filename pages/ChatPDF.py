import streamlit as st
import openai
import base64
from openai import OpenAI
#https://3amtgxmdtwyym69bwahkyv.streamlit.app/

st.title(":blue[ChatPDF!]")
client = st.session_state.get("client", None)

if client is None:
    st.stop()

file = st.file_uploader("Upload a pdf file", type=['pdf'], accept_multiple_files=False)
if file is not None:
    vector_store = client.vector_stores.create(name="PDF_alpha")
    file_batch = client.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id,
        files=[file]
    )
    st.session_state.vector_store = vector_store

if 'vector_store' not in st.session_state:
    st.markdown(":red[Upload PDF file!!]")
    st.stop()

@st.cache_data
def gpt(prompt):
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt,
        tools=[{
            "type": "file_search",
            "vector_store_ids": [vector_store.id]}]
    )
    return response.output_text

def s_m(m):
    with st.chat_message(m['role']):
        st.markdown(m["content"])

if "record3" not in st.session_state:
    st.session_state["record3"] = [{"role": "developer", "content": "주어진 PDF자료를 기반으로 대답하세요. 모르면 모른다고 답하세요."}]

if st.button("Chat Clear!!!"):
    del st.session_state["record3"]

if st.button(":rainbow[PDF Clear!!!!]"):
    del file
    st.session_state["record3"] = [{"role": "developer", "content": "주어진 PDF자료를 기반으로 대답하세요. 모르면 모른다고 답하세요."}]

for m in st.session_state["record3"][1:]:
    s_m(m)

if prompt := st.chat_input("Say something!!!"):
    p1 = {"role":"user", "content": prompt}
    st.session_state["record3"].append(p1)
    s_m(p1)
    response = gpt(st.session_state["record3"])
    p2 = {"role":"assistant", "content": response}
    st.session_state["record3"].append(p2)
    s_m(p2)