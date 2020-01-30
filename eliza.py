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
def generate_default_response() -> str:
    return random.choice(default_resp)


# keywords and their responses
keywords = {r'\b(need)\b(.*)': ["Do you really need {}?", "What would you do if you got {}?"],
            r'\b(hate)\b(.*)': ["What part do you hate about {}?", "What made you hate {}?"],
            r'\b(love)\b(.*)': ["What do you love the most about {}?",
                                "When did you start loving {}?"],
            r'\b(crave)\b(.*)': ["Tell me more about your cravings.",
                                 "How did you develop your craving?"],
            r'\b(want)\b(.*)': ["Why do you want {}?", "What would you do if you got {}?"],
            r'\b(family)\b(.*)': ["Tell me more about your family.",
                                  "What was your relationship with your family like?"],
            r'\b(school)\b(.*)': ["How are you doing at school?",
                                  "What difficulties do you face in school?"]}
# possible patterns in input and their responses
re_patterns = {r'\b(i am)\s(.*)': "Why are you {}?",
               r'(i do not know)(.*)?': "Why don't you know {}?",
               r'(i will)\s(.*)': "How will you {}?",
               r'(i feel)\s(.*)': "When do you usually feel {}?",
               r'\b(i)\b(.*)': "Why do you {}?"}
# default responses
default_resp = ["I see.", "Tell me more.", "How does that make you feel?", "Why do you say that?",
                "Can you elaborate on that?", "I didn't quite understand. Can you explain further?"]
# edited pronouns
pronouns = {"i": "you", "am": "are", "my": "your", "was": "were", "we": "you all", "me": "you",
            "you": "me", "mine": "yours"}

# greetings and get name
print("E: Hi, I am the psychotherapist. What is your name?")
name = input("YOU: ")

print(f"E: Hi, {name}. How can I help you today?")

# conversation loop
while True:

    # user's responses
    response = input("YOU: ")
    edited_resp = re.sub(r'\s+', ' ', response).strip(".!")
    print(edited_resp)

    tokens = None
    eliza_resp = None

    for keyword in keywords:
        tokens = re.search(keyword, edited_resp)
        if tokens:
            eliza_resp = random.choice(keywords[keyword])
            break
    else:
        for pattern in re_patterns:
            tokens = re.search(pattern, edited_resp)
            if tokens:
                eliza_resp = re_patterns[pattern]
                break

    if eliza_resp is None:
        eliza_resp = generate_default_response()
    else:
        words = tokens.group(len(tokens.groups())).lower().split()
        for word in words:
            if word in pronouns:
                word = pronouns[word]

    # "bye" ends conversation
    if re.search(r'\b(bye)\b', response.lower()):
        print(f"Bye, {name}!")
        break
