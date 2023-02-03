# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import spacy

nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

import os

workingDir = os.getcwd()
print("current working directory: " + workingDir)

CollPath = os.path.join(workingDir, 'python-lang')
print(CollPath)


def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        stringFile = (readFile)
        lengthFile = len(readFile)
        print(lengthFile)

tokens = nlp(stringFile)
vectors = tokens.vector

wordOfInterest = "cat"

highSimilarityDict = {}
for token in tokens:
        if(token and token.vector_norm):
            if wordOfInterest.similarity(token) > .3:
                    highSimilarityDict[token] = wordOfInterest.similarity(token)

highSimilarityReduced = {}
for key, value in highSimilarityDict.items():
        if value not in highSimilarityReduced.values():
                highSimilarityReduced[key] = value
        print(highSimilarityReduced)
        print(len(highSimilarityReduced.items()), " vs ", len(highSimilarityDict.items()))

for file in os.listdir(CollPath):
    if file.endswith(".txt"):
        filepath = f"{CollPath}/{file}"
        print(filepath)
        readTextFiles(filepath)




