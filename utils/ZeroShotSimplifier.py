from typing import Dict, List
from utils.AbstractSimplifier import AbstractSimplifier


class ZeroShotSimplifier(AbstractSimplifier):

    def __init__(self, model: str, prompt: str):
        super().__init__(model, prompt)

    def build_chat_messages(self, text: str) -> List[Dict[str, str]]:
        return [
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": text},
        ]