import os
from abc import ABC, abstractmethod
from typing import Dict, List

from openai import OpenAI

class AbstractSimplifier(ABC):
    CLIENT = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def __init__(self, model: str, prompt: str):
        self.model = model
        self.prompt = prompt

    def simplify(self, text: str) -> str:
        try:
            response = AbstractSimplifier.CLIENT.chat.completions.create(
                model=self.model,
                messages=self.build_chat_messages(text),
                temperature=0.1,
                top_p=0.2,
                max_tokens=4095,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stream=False,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(e)
            raise Exception("Failed to simplify text")
        

    @abstractmethod
    def build_chat_messages(self, text: str) -> List[Dict[str, str]]:
        pass
