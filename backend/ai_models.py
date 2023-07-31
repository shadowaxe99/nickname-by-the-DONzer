```python
import openai
from openai import GPT3Model, CodexModel

class AIModels:
    def __init__(self):
        self.gpt3_model = GPT3Model()
        self.codex_model = CodexModel()

    def generate_nickname(self, name):
        prompt = f"Generate a Donald Trump style nickname for {name}"
        response = self.gpt3_model.complete(prompt)
        generated_nickname = response.choices[0].text.strip()
        return generated_nickname

    def generate_response(self, statement):
        prompt = f"If Donald Trump were to respond to the statement '{statement}', what would he say?"
        response = self.gpt3_model.complete(prompt)
        generated_response = response.choices[0].text.strip()
        return generated_response

    def simulate_debate(self, statement, political_figure):
        prompt = f"Simulate a debate between Donald Trump and {political_figure} on the statement '{statement}'"
        response = self.gpt3_model.complete(prompt)
        debate_simulation = response.choices[0].text.strip()
        return debate_simulation
```