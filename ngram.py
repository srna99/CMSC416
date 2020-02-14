"""
Serena Cheng
CMSC 416 - PA 2: Ngrams
2/13/2020
~~~~~
Problem:


Usage:


Algorithm:

"""

import random
import re
import sys

ngram_dict = {}
probabilities = {}
tokens = []
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

    content = re.sub(r'[,*\-_;:()\"]', ' ', content)

    content = start_tags + content
    content = re.sub(r'[.!?]', ' .', content)
    edit = content.split(".")
    end_start_tags = "<e> " + start_tags
    content = end_start_tags.join(map(str, edit))

    content = re.sub(r'\s+', ' ', content)

    tokens.extend(content.split())
    # print(len(tokens))

index = 0
while index < len(tokens):
    ngram.append(tokens[index])

    if len(ngram) == num_for_gram:
        word = ngram.pop()
        key = " ".join(map(str, ngram))

        if key in ngram_dict.keys():
            if word in ngram_dict[key]:
                ngram_dict[key][word] += 1
            else:
                ngram_dict[key][word] = 1
        else:
            ngram_dict[key] = {word: 1}

        index -= (num_for_gram - 2)
        ngram.clear()
    else:
        index += 1

for history, word_dict in ngram_dict.items():
    n_minus_1_freq = sum(word_dict.values())

    for word, n_freq in word_dict.items():
        probability = round(n_freq / n_minus_1_freq, 10)

        if history in probabilities.keys():
            probabilities[history][word] = probability
        else:
            probabilities[history] = {word: probability}

# print(ngram_dict)
# print(probabilities)








