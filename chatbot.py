import streamlit as st
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyCQimncR-u0uG4C1FRT-2Yp4xYpAxAV7hY"

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="question answers")
st.header("Chatbot")
input=st.text_input("Input: ",key="input")
submit=st.button("give a question or prompt")

if submit:
  response=get_gemini_response(input)
  st.subheader("The Response is")
  st.write(response)