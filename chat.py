import streamlit as st
from openai import OpenAI

st.image("https://docs.streamlit.io/logo.svg")

st.header("OpenAI API Key를 적어주세요.")
api = st.text_input("API Key?")

if st.button("확인"):
  client = OpenAI(api_key=f"{api}")
  assistant = client.beta.assistants.create(
    instructions = "You are a helpful assistant.",
    model='gpt-4o'
  )
  assistant = client.beta.assistants.create(
      instructions = "당신은 수학 선생님입니다",
      model = "gpt-4-turbo",
      tools = tools
  )
  thread = client.beta.threads.create(
    messages=[
      {
          "role":"user",
          "content": "다음 이차방정식의 해를 구해줘: 15x^2 - 2x+1.2=0"
      }
    ]
  )
  run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
  )
st.divider()

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")

if st.button("실행하기"):
  thread = client.beta.threads.create(
    messages=[
      {
        "role": "user",
        "content": f"{prompt}",
      }
    ]
  )
  run = client.beta.threads.runs.create_and_poll(
      thread_id=thread.id,
      assistant_id=assistant.id
  )
  run
  thread_messages = client.beta.threads.messages.list(thread.id, run_id=run.id)
  for msg in thread_messages.data:
    print(f"{msg.role}: {msg.content[0].text.value}")
  st.markdown(f"질문: {prompt}")

st.divider()

st.header("무엇이든 그려보세요.")

if st.button("Streamlit video"):
  st.video("https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4")
