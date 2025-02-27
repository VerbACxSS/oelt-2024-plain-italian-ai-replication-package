from typing import Dict, List, Tuple
from utils.AbstractSimplifier import AbstractSimplifier


class FewShotSimplifier(AbstractSimplifier):

    def __init__(self, model: str, prompt: str, examples: List[Tuple[str, str]]):
        super().__init__(model, prompt)
        self.examples = examples

    def build_chat_messages(self, text: str) -> List[Dict[str, str]]:
        messages = [
            {"role": "system", "content": self.prompt},
        ]
        for example in self.examples:
            messages.append({"role": "user", "content": example[0]})
            messages.append({"role": "system", "content": example[1]})
        
        messages.append({"role": "user", "content": text})
        return messages