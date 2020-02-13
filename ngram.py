"""
Serena Cheng
CMSC 416 - PA 2: Ngrams
2/13/2020
~~~~~
Problem:


Usage:


Algorithm:

"""

import os
import re
import random
import sys

num_for_gram = 0
num_of_sentences = 0
text_files = []

for i in range(1, len(sys.argv)):
    if i == 1:
        num_for_gram = sys.argv[i]
    elif i == 2:
        num_of_sentences = sys.argv[i]
    else:
        text_files.append(sys.argv[i])

print(num_for_gram, num_of_sentences, text_files)

for txt_file in text_files:
    with open(txt_file, "r", encoding="utf8") as file:
        content = file.read().lower()

    content = re.sub(r'[,*\-_;:()"]', ' ', content)
    content = re.sub(r'[.!?]', '.', content)
    content = re.sub(r'\s+', ' ', content)

    print(content)













