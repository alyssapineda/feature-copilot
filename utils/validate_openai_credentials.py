import streamlit as st
import openai
import os

openai.api_key = st.secrets["OPENAI_API_KEY"]

completion = openai.ChatCompletion.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "user", "content": "What is Streamlit?"}
  ]
)

st.write(completion.choices[0].message.content)