# spaCy is a modern library for NLP that focuses on 
# performance and ease of use

import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("Hello, world. Here are two sentences.")

# Print the entities in the document
print("Entities:")
for entity in doc.ents:
    print(f"{entity.text}: {entity.label_}")
    
# Print the parts of speech for each token
print("\nParts of Speech:")
for token in doc:
    print(token.text, ":", token.pos_)
    

    