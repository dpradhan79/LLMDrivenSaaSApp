from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


from core.llm_factory import llms
from prompts.answer import get_system_prompt_to_answer_questions
from schemas.answer import Answer


class AgentAnswerProvider:
    def __init__(self, llm = llms.get_open_ai_chat_model()):
        self.llm = llm

    def provide_answer(self, question):
        # Use the language model to generate an answer to the question
        model = self.llm
        agent = create_agent(
            model = model,
            system_prompt=get_system_prompt_to_answer_questions(),
            response_format=Answer
        )
        answer = agent.invoke(
            {"messages":[HumanMessage(content=question)]}
        )
        return answer["structured_response"]