import gpt4all
import os

if not os.listdir("models/"):
    gptj = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy", "models/")