import logging
import os
from pathlib import Path

from fastapi import APIRouter, Query, Request

from starlette.responses import HTMLResponse

from core.llm_factory import llms
from agents.answer_agent import AgentAnswerProvider
from fastapi.templating import Jinja2Templates
import markdown

from schemas.answer import Answer

router_answer = APIRouter(prefix="/Exam Expert", tags=["Exam Expert"])
templates = Jinja2Templates(directory="templates")
logger = logging.getLogger()
# Register a custom filter
def markdown_filter(text: str) -> str:
    if not text:
        return ""
        # If it looks like ASCII art (lots of arrows or spacing), wrap in <pre>
    if "->" in text or "│" in text or "⟶" in text:
        return f"<pre>{text}</pre>"
        # Otherwise, render as Markdown
    return markdown.markdown(text)

templates.env.filters["markdown"] = markdown_filter

@router_answer.post("/answer/json")
def answer_json(question:str = Query(default="What's Diffusion?", description="Class 10th Exam Expert will answer the question based on subject and chapter. It will also provide diagram, example and special note as and when required.")):
    """
    This endpoint will answer the question based on subject and chapter. It will also provide diagram, example and special note as and when required.
    :param question:
    :return:
    """
    try:
        if os.getenv("DEPLOYMENT").strip().lower() == "local":
            agent = AgentAnswerProvider(llms.get_ollama_chat_model(model="qwen3.5:9b"))
        else:
            agent = AgentAnswerProvider(llms.get_open_ai_chat_model(model="gpt-5.4-nano"))

        resp : Answer = agent.provide_answer(question)
        return resp
    except Exception as e:
        logger.error(f"Error in answering the question - {str(e)}")
        return {"error": str(e)}

@router_answer.post("/answer/html")
def answer_html(request: Request, question:str = Query(default="What's Diffusion?", description="Class 10th Exam Expert will answer the question based on subject and chapter. It will also provide diagram, example and special note as and when required.")):
    """
    This endpoint will answer the question based on subject and chapter. It will also provide diagram, example and special note as and when required.
    :param request:
    :param question:
    :return:
    """
    try:
        if os.getenv("DEPLOYMENT").strip().lower() == "local":
            agent = AgentAnswerProvider(llms.get_ollama_chat_model(model="qwen3.5:9b"))
        else:
            agent = AgentAnswerProvider(llms.get_open_ai_chat_model(model="gpt-5.4-nano"))
        resp:Answer = agent.provide_answer(question)
        return templates.TemplateResponse(request = request,
                                   name="answer.html",
                                   context = {"request": request, "answer": resp},
                                   media_type='html'
                                   )
    except Exception as e:
        logger.error(f"Error in answering the question - {str(e)}")
        return {"error": str(e)}



