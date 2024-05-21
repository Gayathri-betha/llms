import os
from constants import openai_key 

from langchain.llms import OpenAI 

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

st.title('OpenAI Demo with LangChain')

input_text = st.text_input('Search any topic')


llm = OpenAI(temperature=0.8)

if input_text:
    response = llm(input_text)
    
    st.write(response)

