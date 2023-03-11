# chatGPT-cracker
Crack chatGPT answers with ease*

*ease is relative to your will to try different values and outcomes, best outcomes are already in the code

The engines are deprecated
https://api.openai.com/v1/engines
https://api.openai.com/v1/engines/{engine id}

Model are currently overall better
https://api.openai.com/v1/models
https://api.openai.com/v1/models/{model}

Copletion creation
model = model used look above.

prompt = your text and stuff.

suffix = suffix after the completion of iserted text, don't ak me what it does I didn't use it.

max_tokens = max number of tokens (your answer), tokens are set of words stay between 2048 and 4096, in case of crash lower to 2048 or even lower. https://platform.openai.com/tokenizer

temeprature = higher valeus makes the answers more random 0.8, and with lower values 0.2 it will be focused and determinstic, goes from 0 to 2.
NEVER USE 2 AS TEMPERATURE it wil take over your computer.

top_p = use the tokens of your prompt to generate a "mass" value and will "analyze the phrase" based on that
0.4 -> it will analyze the 40% of the mass
this is a really complex value
RECCOMENDED do NOT alter top_p and temperature toghether unless you know what you are doing.

n = number of generate prompt for your prompt
WARNING keep it low to not exced you token quota

stream = as the name implies it's the presonse prompt send as its generated

logprobs = the tokens and tokens chosen

echo = sends you back your own prompt

stop = when sent the API will stop the current generation

presence_penalty = -2 to 2 
makes the next generated prompt different to the previous one
FOR NEW TOPICS
Keep it at 0 otherwise you will get trash

frequency_penalty = -2 to 2 
makes the next generated prompt different to the previous one
FOR VERBATIM responses
Keep it at 0 otherwise you will get trash

best_of = the best SERVER-SIDE response
default set to 1
must be > n
WARNING USE WITH MAX_TOKEN AND STOP

logit_bias = modify the likelihood of the specifed tokens to appear (accepts a JSON object :D) 
use the https://platform.openai.com/tokenizer to propperly use this

user = the funny string that will f**k you up if you behave really impropperly


Yep I'm lazy and I don't want to do anything sice it takes time
-Ranged
