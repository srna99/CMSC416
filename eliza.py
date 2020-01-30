"""
Serena Cheng
CMSC 416 - PA 1: Eliza
1/30/2020
~~~~~
Problem:
This assignment was to make a program like Eliza. The program should respond as a psychotherapist to
user input, while sounding as human-like as possible with customized responses. Some responses should be
made from spotting certain keywords or changing statements to questions.

Usage:
The program begins by asking for a name, and the input should just be the name. In order to end the
program, the word "bye" should be inputted.
Ex. "I want to be a cat in my next life." -> "Why do you want to be a cat in your next life?"
    "I am not ready to be an adult." -> "Why are you not ready to be an adult?"
    "Blue marshmallows sound green." -> "I didn't quite understand. Can you explain further?"

Algorithm:
Regular expressions are used to search for keywords or specific structures in user input. If it matches,
parts of the user input are taken apart. Sections of the user input are added to the response and
pronouns are corrected. Then, the responses are printed. Default responses are also available for
unforeseen inputs.
"""

import re
import random
from typing import Match


def generate_specialized_response(parts: Match):
    # construct specialized response using regular expressions
    words = parts.group(len(parts.groups())).lower().split()

    # replace pronouns with correct ones
    for i, word in enumerate(words):
        if word in pronouns:
            words[i] = pronouns[word]

    # combine parts and print response
    component = " ".join(words)
    finished_resp = eliza_resp.replace("{}", component)
    print(re.sub(r'\s+', ' ', finished_resp))


def generate_default_response():
    # print from default responses for inputs that are not coded for and including name in some responses
    finished_resp = random.choice(default_resp)
    if random.randint(0, 10) < 7:
        print(finished_resp)
    else:
        if finished_resp[0] != 'I':
            print(f"{name},", finished_resp.lower())
        else:
            print(f"{name},", finished_resp)


# keywords and their responses
keywords = {r'\b(need)\b(.*)': ["Do you really need {}?", "What would you do if you got {}?"],
            r'\b(hate)\b(.*)': ["What part do you hate about {}?", "What made you hate {}?"],
            r'\b(love)\b(.*)': ["What do you love the most about {}?",
                                "When did you start loving {}?"],
            r'\b(crave)\b(.*)': ["Tell me more about your cravings.",
                                 "How did you develop your craving?"],
            r'\b(want)\b(.*)': ["Why do you want {}?", "What would you do if you got {}?"],
            r'\b(family)\b': ["Tell me more about your family.",
                              "What was your relationship with your family like?"],
            r'\b(school)\b': ["How are you doing at school?",
                              "What difficulties do you face in school?"]}
# possible patterns in input and their responses
re_patterns = {r'\b[Ii]\s(am)\s(.*)': "Why are you {}?",
               r'[Ii]\s(do not know)(.*)?': "Why don't you know {}?",
               r'[Ii]\s(will)\s(.*)': "How will you {}?",
               r'[Ii]\s(feel)\s(.*)': "When do you usually feel {}?",
               r'\b[Ii]\b(.*)': "Why do you {}?"}
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

    # "bye" ends conversation
    if re.search(r'\b(bye)\b', response.lower()):
        print(f"Bye, {name}!")
        break

    tokens = None
    eliza_resp = None

    # see if response includes a keyword
    for keyword in keywords:
        tokens = re.search(keyword, edited_resp)
        if tokens:
            eliza_resp = random.choice(keywords[keyword])
            break
    # or see if response has special structure
    else:
        for pattern in re_patterns:
            tokens = re.search(pattern, edited_resp)
            if tokens:
                eliza_resp = re_patterns[pattern]
                break

    # if response not considered in above collections, then print a default response
    if eliza_resp is None:
        generate_default_response()
    # else construct the specialized response
    else:
        generate_specialized_response(tokens)
