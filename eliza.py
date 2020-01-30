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


# keywords and their responses
keywords = {r'\b(need)\b': ["Do you really need {0}?", "What would you do if you got {0}?"],
            r'\b(hate)\b': ["What part do you hate about {0}?", "What made you hate {0}?"],
            r'\b(love)\b': ["What do you love the most about {0}?", "When did you start loving {0}?"],
            r'\b(crave)\b': ["Tell me more about your cravings.", "How did you develop your craving?"],
            r'\b(want)\b': ["Why do you want {0}?", "What would you do if you got {0]?"],
            r'\b(family)\b': ["Tell me more about your family.",
                              "What was your relationship with your family like?"],
            r'\b(school)\b': ["How are you doing at school?",
                              "What difficulties do you face in school?"]}
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

    match = None
    eliza_resp = None
    for pattern in re_patterns:
        match = re.match(pattern, edited_resp)

        if match:
            eliza_resp = re_patterns[pattern]
            break

    if eliza_resp:
        for i in range(len(match.groups())):
            # token =
            pass

    # "bye" ends conversation
    if re.search(r'\b(bye)\b', response.lower()):
        print(f"Bye, {name}!")
        break
