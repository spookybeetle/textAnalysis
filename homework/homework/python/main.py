import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')


doc = nlp("I cannot get it to open my text files. Am I missing something?")
for token in doc:
    print(token.text, token.pos_, token.dep_)

