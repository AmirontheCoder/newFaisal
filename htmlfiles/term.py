import spacy
nlp = spacy.load("en_core_web_sm")
with open('/home/amir/projects/helloworld/htmlfiles/us.txt') as f:
    text = f.read()
print(text)

doc1 = nlp(text)

  