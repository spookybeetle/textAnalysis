# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import spacy

nlp = spacy.cli.download("en_core_web_md")
nlp = spacy.load('en_core_web_md')
# 2023-02-06 ebb: So here we need to work with spaCy's medium (md) language model
# to get word vectors out of it. (The small model is lacking vector data.)
import os

workingDir = os.getcwd()
print("current working directory: " + workingDir)

CollPath = os.path.join(workingDir, 'python-lang')
print(CollPath)


def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        stringFile = str(readFile)
        # 2023-02-06 ebb: You need to convert the document into a string (text) for NLP to read it.
        lengthFile = len(readFile)
        print(lengthFile)
        # ebb: Here we need to keep an eye on indentation.
        # In Python, the indentation shows something depends on the context set above it.
        # Here everything depends on opening the file.
        # So these variables exist in the file opening "zone" of the Python script.

        tokens = nlp(stringFile)
        vectors = tokens.vector

        wordOfInterest = nlp(u'cat')
        # ebb: I corrected the line above because you need spaCy to pull NLP data on the word of interest,
        # It isn't just the word you want, but the data spaCy has attached to that word. 

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




