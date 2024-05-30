import streamlit as st
from openai import OpenAI
client = OpenAI(api_key="")
assistant = client.beta.assistants.create(
  instructions="my chatbot",
  model="gpt-4o"
)

st.image("https://docs.streamlit.io/logo.svg")

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")

if st.button("실행하기"):
  st.markdown(f"질문: {prompt}")

st.divider()

st.header("무엇이든 그려보세요.")

if st.button("Streamlit video"):
  st.video("https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4")
