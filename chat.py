import streamlit as st
from openai import OpenAI
st.header("OpenAI API Key를 적어주세요.")
api = st.text_input("API Key?")

if st.button("확인"):
  client = OpenAI(api_key=f"{api}")
  assistant = client.beta.assistants.create(
    instructions = "You are a helpful assistant.",
    model='gpt-3.5-turbo'
  )
st.divider()
st.image("https://docs.streamlit.io/logo.svg")

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")

if st.button("실행하기"):
  st.markdown(f"질문: {prompt}")

st.divider()

st.header("무엇이든 그려보세요.")

if st.button("Streamlit video"):
  st.video("https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4")
