import streamlit as st
from openai import OpenAI

st.image("https://docs.streamlit.io/logo.svg")

st.header("OpenAI API Key를 적어주세요.")
api = st.text_input("API Key?")

if 'questions' not in st.session_state:
    st.session_state.questions = []

if st.button("확인"):
  client = OpenAI(api_key=f"{api}")
  assistant = client.beta.assistants.create(
    instructions = "You are a helpful assistant.",
    model='gpt-4o'
  )
  
st.divider()

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")

if st.button("실행하기"):
  st.session_state.questions.append(prompt)
    st.success('질문이 저장되었습니다!')
  thread = client.beta.threads.create(
    messages=[
      {
          "role":"user",
          "content": f"{prompt}"
      }
    ]
  )
  run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
  )
  st.markdown(f"질문: {prompt}")

st.divider()

st.header("무엇이든 그려보세요.")

if st.button("Streamlit video"):
  st.video("https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4")
