import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


##langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system"," You are a helpful assistant. Please response to the question asked"),
        ("user","Question:{question}")
    ]
)

# Streamlit framework
st.title("Langchain Demo with Gemma model")
input_text = st.text_input("What is your question?")

#Ollama Llama2 model 
llm = Ollama(model="gemma:2b")
output_str = StrOutputParser()
chain = prompt|llm|output_str

if input_text:
    st.write(chain.invoke({"question":input_text}))