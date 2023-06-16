
from typing import List
from dataclasses import dataclass

@dataclass
class Quiz:
    questions: List[str]
    answers: List[str]

    def generate_questions(self, terms_of_service: str) -> None:
        pass

    def check_answers(self, user_answers: List[str]) -> bool:
        pass