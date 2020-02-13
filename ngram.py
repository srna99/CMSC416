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

    content = re.sub(r'[,*\-_;:()"]', ' ', content)
    content = re.sub(r'[.!?]', ' .', content)
    content = re.sub(r'\s+', ' ', content)

    tokens = content.split()

    for i in range(0, 2000):
        print(i)
        if i == 0 or tokens[i-1] == ".":
            for j in range(1, num_for_gram):
                ngram.append("<s>")

            word = tokens[i]
            key = " ".join(map(str, ngram))

            if key in history.keys():
                if word in history[key]:
                    history[key][word] += 1
                    print("here")
                else:
                    history[key][word] = 1
                    print("no here")
            else:
                history[key] = {word: 1}
                print("no no here")

            print(history)

            ngram.clear()











