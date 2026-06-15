from typing import Optional

from pydantic import BaseModel, Field
class Answer(BaseModel):
    subject: str = Field(default_factory=str, description="The subject of the answer")
    chapter: str = Field(default_factory=str, description="The chapter of the answer")
    question: str = Field(default_factory=str, description="The question for which the answer is provided")
    answer: str = Field(default_factory=str, description="The answer to the question")
    diagram: str = Field(default=None, description="A diagram related to the answer, if question is related to Mathematics and Science")
    example: Optional[str] = Field(default=None, description="A example related to the answer, if applicable")
    specialNote: Optional[str] = Field(default=None, description="A special note related to the answer, if applicable")
