import logging

import dotenv
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
logger = logging.getLogger()

def get_open_ai_chat_model(model : str = "gpt-5.4-nano"):
    try:
        return ChatOpenAI(model=model)
    except Exception as e:
        raise

def get_ollama_chat_model(model: str = "qwen3.5:9b"):
    try:
        return ChatOllama(model=model) #"gpt-oss:20b"
    except Exception as e:
        raise