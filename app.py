# from langchain_openAi import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
#langsmith trace
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##prompt templete
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assesstent.please respond to user queires"),
        ("user","Question{question}")
    ]
)

st.title("your chatbot(kulonni) :")
query=st.text_input("search your question :")

#llm
llm=ChatGroq(model="llama-3.3-70b-versatile")
#As of now, Groq provides access to Mistral and LLaMA family models. Common ones include:

# mistral-saba-24b — recommended replacement for mixtral-8x7b-32768. 

# llama-3.3-70b-versatile — another production model. 

# llama-3.1-8b-instant — smaller, faster for less demanding scenarios

# "llama2-70b-4096" → LLaMA 2 70B (good general-purpose)

# "llama2-13b-4096" → LLaMA 2 13B (lighter, faster)

# "gemma-7b-it" → Google Gemma 7B Instruct


outputparse=StrOutputParser()

#now chain

chain=prompt|llm|outputparse

if query:
    st.write(chain.invoke({"question":query}))