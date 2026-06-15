import dotenv

from agents.answer_agent import AgentAnswerProvider
from core.llm_factory import llms


def test_answer_agent():
    dotenv.load_dotenv()
    question = "Explain transpiration in terms of environment"
    agent = AgentAnswerProvider(llms.get_ollama_chat_model())
    answer = agent.provide_answer(question)
    assert answer is not None
    assert answer.answer is not None
    assert answer.subject is not None
    assert answer.chapter is not None
    assert question in answer.question
    print(f'Answer - {answer.answer}')