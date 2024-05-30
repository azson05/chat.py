import streamlit as st
from openai import OpenAI

st.image("https://docs.streamlit.io/logo.svg")

st.divider()

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")

if st.button("실행하기"):
      openai.api_key = "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"
    assistant = openai.Assistant.create(
        instructions="You are a helpful assistant.",
        model='gpt-4o'
    )
    thread = openai.Thread.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]
    )
    run = openai.Thread.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    thread_messages = openai.Message.list(thread.id, limit=1)
    for msg in thread_messages.data:
        st.write(f"{msg.role}: {msg.content[0].text.value}")
  st.markdown(f"질문: {prompt}")

st.divider()

st.header("무엇이든 그려보세요.")

if st.button("Streamlit video"):
  st.video("https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4")
