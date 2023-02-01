# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import spacy

nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

AFAB = open('AFAB.txt', 'r', encoding='utf8')
words = AFAB.read()
wordstrings = str(words)
print(wordstrings)

AFAB = nlp(wordstrings)
for token in AFAB:
    # if token.pos_ == "VERB":
    print(token.text, "---->", token.pos_, ":::::", token.lemma_)



