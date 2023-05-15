<h1>This code is severely outdated</h1>

# chatGPT-cracker
Crack chatGPT answers with ease*
*ease is relative to your will to try different values and outcomes, the best outcomes are already in the code
# Install
Simply clone the code and run it, use pip to install the required library
## NOTICE
don't try to install or download moonlander or moonhole, they will either not work or not download at ll
# Use
py funnygpt.py or curie.py
after that you will be able to ask questions to chatGPT 
You might not always be able to get a propper response due to the nature of the projects most values are set to provide unfiltered ansers and NOT answers that makes sense
# Deprecation
## - Engines
[https://api.openai.com/v1/engines](https://api.openai.com/v1/engines) https://api.openai.com/v1/engines/ {engine id}
## - Models
Models are currently overall better  and still supported
https://api.openai.com/v1/models
https://api.openai.com/v1/models/ {model id}
# Variables/Completion creation
- model
> The model used, look above
- prompt
>your text and stuff.
- suffix
> suffix after the completion of inserted text, don't ask me what it does I didn't use it.
- max_tokens
> max number of tokens (your answer), tokens are a set of words that stay between 2048 and 4096, in case of a crash lower to 2048 or even lower. https://platform.openai.com/tokenizer
- temperature
> higher values make the answers more random 0.8, and with lower values 0.2 it will be focused and deterministic
> goes from 0 to 2.
> NEVER USE 2 AS TEMPERATURE it will take over your computer.
-  top_p 
> use the tokens of your prompt to generate a "mass" value and will "analyze the phrase" based on that
> 0.4 -> it will analyze 40% of the mass
> this is a complex value
> RECOMMENDED do NOT alter top_p and temperature together unless you know what you are doing.
- n 
> number of generated prompts for your prompt
> WARNING keep it low to not exceed your token quota
- stream 
> as the name implies it's the presence prompt sent as it generated
- logprobs 
> the tokens and tokens chosen
- echo 
> sends you back your prompt
- stop 
> when sent the API will stop the current generation
- presence_penalty 
> -2 to 2
makes the next generated prompt different to the previous one
FOR NEW TOPICS
Keep it at 0 otherwise, you will get trash
- frequency_penalty 
> -2 to 2
makes the next generated prompt different to the previous one
FOR VERBATIM responses
Keep it at 0 otherwise, you will get trash
- best_of 
> the best SERVER-SIDE response
default set to 1
must be > n
WARNING USE WITH MAX_TOKEN AND STOP
- logit_bias 
> modify the likelihood of the specified tokens to appear (accepts a JSON object :D)
use the https://platform.openai.com/tokenizer to properly use this
- user 
> the funny string that will f**k you up if you behave improperly
