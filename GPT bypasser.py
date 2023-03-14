#63/1-03
import openai
from key import *
#import moonlander from moonhole

openai.api_key = API_KEY
model_engine = "text-davinci-003"
max_tokens = 1024
while True:
    prompt = input("Enter your text: ")
    completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0.2,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0
    )
    print(completion.choices[0].text)