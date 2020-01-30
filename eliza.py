"""
Serena Cheng
CMSC 416 - PA 1: Eliza
1/30/2020
~~~~~
TYPE INTRO HEREEEE!!!
"""

import re
import random


# pick from default responses for inputs that are not coded for
def generate_default_response():
    print(random.choice(default_resp))


# possible patterns in input and their responses
re_patterns = {r'\b(I)\b(.*)[^,.!?]': "Why do you {0}?", r'\b(I am)\s(.*)[^,.!?]': "Why are you {0}?",
               r'(I do not know)(.*)?[^,.!?]': "Why don't you know {0}?"}

# default responses
default_resp = ["I see.", "Tell me more.", "How does that make you feel?", "Why do you say that?",
                "Can you elaborate on that?", "I didn't quite understand. Can you explain further?"]

# edited pronouns
pronouns = {"i": "you", "am": "are", "my": "your", "was": "were", "we": "you all", "me": "you"}

# greetings and get name
print("E: Hi, I am the psychotherapist. What is your name?")
name = input("YOU: ")

print(f"E: Hi, {name}. How can I help you today?")

# conversation loop
while True:

    # user's responses
    response = input("YOU: ")
    edited_resp = re.sub(r'\s+', ' ', response)
    print(edited_resp)

    # "bye" ends conversation
    if re.match(r'\b(bye)\b', response.lower()):
        print(f"Bye, {name}!")
        break
