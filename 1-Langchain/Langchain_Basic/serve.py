from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
from langserve import add_routes
groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)


# 1. Create Chat prompt template

system_template = "translate into the following {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [("system",system_template),
     ("user","{text}")]
)

parser = StrOutputParser()


# 2. creating Chain

chain = prompt_template|model|parser

# App Definition

app = FastAPI(title="Langchain Server",
              version="1.0",
              description="A Simple API server using langchain runnable interfaces")


# Adding chain routes
add_routes(
    app,
    chain,
    path= "/chain"
)


if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost", port = 8000)