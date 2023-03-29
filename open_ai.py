import os
import openai


class OpenAIWrapper:

    def __init__(self):
        print("initialising openAI")
        openai.api_key = os.getenv("aikey")

    def ask(self, text):
        result= openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0,
                                        max_tokens=300)
        print(result)
        return result.choices[0].text
