```python
import openai

class CodexModel:
    def __init__(self):
        self.model = "text-davinci-002"
        self.api_key = "your_openai_api_key"
        openai.api_key = self.api_key

    def generate_code(self, prompt):
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            temperature=0.5,
            max_tokens=100
        )
        return response.choices[0].text.strip()

codex_model = CodexModel()
```