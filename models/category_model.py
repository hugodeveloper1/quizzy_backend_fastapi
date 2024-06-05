from typing import List, Optional
from pydantic import BaseModel
from typing import List


class Answer(BaseModel):
    answer: str
    is_answer: bool
    _id: str = None


class Question(BaseModel):
    question: str
    answers: List[Answer]
    answer_id: str = None


class Category(BaseModel):
    name: str
    questions: List[Question]


class NewQuestion(BaseModel):
    category_id: str
    question: str
    answers: List[Answer]
