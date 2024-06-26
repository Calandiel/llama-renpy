﻿# To use this script, you must first run a llama.cpp server:
# https://github.com/ggerganov/llama.cpp
# In a real project, the server and model binaries should be shipped with the game and started up when the game loads.
# Also, it's not async (it will hang the game). Making it so should be trivial so it's left as an exercise to the reader.

define e = Character('Eileen')

label start:

    scene bg room
    show eileen happy

    $ import requests

    e 'Making a request, please wait... {nw}'

    $ prompt = 'Text generated by the AI: '
    $ tokens_to_generate = 16

    $ reply = requests.post('http://localhost:8080/completion', json={'prompt': prompt, 'n_predict': tokens_to_generate}) # Call the endpoint
    $ reply = str(reply.json()["content"]) # Retrieve the generated text

    jump loop

label loop:

    e 'Prompt: [prompt]'
    e 'Reply: [reply]'

    jump loop
