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
history_freq_dict = {}
tokens = []
ngram = []
sentences = []

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

for txt_file in text_files:
    with open(txt_file, "r", encoding="utf-8-sig") as file:
        content = file.read().lower()

    start_tags = ""
    for _ in range(1, num_for_gram):
        start_tags += "<s> "

    content = re.sub(r'[,*\-_;:()\'\"]', ' ', content)

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
    history_freq_dict[history] = sum(word_dict.values())

ngram.clear()
sentence_count = 0
index = 0
while sentence_count != num_of_sentences:
    if len(sentences) == 0:
        begin_tag = ""
        for _ in range(1, num_for_gram):
            begin_tag += "<s> "

        sentences.extend(begin_tag.split())
        ngram.extend(sentences)

        index += (len(sentences) - 1)

    history = " ".join(map(str, ngram))

    possible_words = []
    probabilities = []

    for k, v in ngram_dict[history].items():
        possible_words.append(k)

        probability = round(v / history_freq_dict[history], 10)
        probabilities.append(probability)

    selected_word = random.choices(possible_words, probabilities)
    selected_word = re.sub(r'[\[\]\'\"]', '', str(selected_word))

    if selected_word == "<e>":
        sentence_count += 1

    sentences.append(selected_word)
    ngram.append(selected_word)
    ngram.pop(0)

    index += 1








