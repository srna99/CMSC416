"""
Serena Cheng
CMSC 416 - PA 1: Eliza
1/30/2020
~~~~~
TYPE INTRO HEREEEE!!!
"""

import re
import random

# re_patterns = [r'^(.*?)\s(crave)\s(.*?)$':""]
default_resp = ["I see.", "Tell me more.", "How does that make you feel?", "Why do you say that?", "Can you elaborate on that?"]

print("E: Hi, I am the psychotherapist. What is your name?")
name = input("YOU: ")

print(f"E: Hi, {name}. How can I help you today?")

while True:
    response = input("YOU: ")
    print(response)

    if re.match(r'\b(bye)\b', response.lower()):
        print(f"Bye, {name}!")
        break
