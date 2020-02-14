"""
Serena Cheng
CMSC 416 - PA 2: Ngrams
2/13/2020
~~~~~
Problem:


Usage:


Algorithm:

"""

import re
import random
import sys

history = {}
probabilities = {}
ngram = []

num_for_gram = 0
num_of_sentences = 0
text_files = []

for i in range(1, len(sys.argv)):
    if i == 1:
        num_for_gram = int(sys.argv[i])
    elif i == 2:
        num_of_sentences = int(sys.argv[i])
    else:
        text_files.append(sys.argv[i])

print(num_for_gram, num_of_sentences, text_files)

for txt_file in text_files:
    with open(txt_file, "r", encoding="utf-8-sig") as file:
        content = file.read().lower()

    start_tags = ""
    for _ in range(1, num_for_gram):
        start_tags += "<s> "

    content = re.sub(r'[,*\-_;:()"]', ' ', content)

    content = start_tags + content
    content = re.sub(r'[.!?]', ' .', content)
    edit = content.split(".")
    end_start_tags = ". " + start_tags
    content = end_start_tags.join(map(str, edit))

    content = re.sub(r'\s+', ' ', content)

    tokens = content.split()

    index = 0
    while index < 100:
        ngram.append(tokens[index])

        if len(ngram) == num_for_gram:
            word = ngram.pop()
            key = " ".join(map(str, ngram))

            if key in history.keys():
                if word in history[key]:
                    history[key][word] += 1
                else:
                    history[key][word] = 1
            else:
                history[key] = {word: 1}

            index -= (num_for_gram - 2)
            ngram.clear()
        else:
            index += 1











