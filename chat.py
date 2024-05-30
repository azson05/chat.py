import streamlit as st

st.header("OpenAI API Key를 적어주세요.")
api = st.text_input("API Key?")

if st.button("확인"):
  from openai import Openai
  client = OpenAI(api_key=f"{api}")
  assistant = client.beta.assistants.create(
    instructions = "You are a helpful assistant.",
    model='gpt-3.5-turbo'
  )
st.divider()
