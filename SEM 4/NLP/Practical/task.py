import spacy
nlp = spacy.load("en_core_web_sm")
from spacy import displacy

news_article = """Summary of Operation SINDOOR
On 22 April, Pakistan based terrorist group “The Resistance Front” (TRF) perpetrated a devastating attack in Pahalgam, India.  In this attack 26 innocent tourists were killed in cold blood after segregating them based on their religion.  TRF is an offshoot of the well known Pakistan backed terrorist organisation Lashkar-e-Taiba.  Post the attack, TRF claimed the responsibility for this attack not once but twice within a few hours.  Pakistan’s subsequent refusal to acknowledge or curb these terrorist networks compelled India to take a responsible but resolute action. In response, on  the night of 7–8 May 2025, the Government of India executed “Operation Sindoor,”.  The response was non escalatory, precise and targeted terrorist training camps at nine different locations within Pakistan and Pakistan Occupied Kashmir.  No military targets were engaged.  However, in the early hours of 8 May, Pakistan, in an escalated response launched coordinated drone and missile strikes targeting over a dozen Indian military installations across the Northern and Western theatres, including Srinagar, Jammu, Pathankot, Amritsar, Ludhiana, Bathinda and Bhuj. India’s robust Integrated Counter-drone Grid and layered Air Defence systems intercepted these attacks, recovering debris conclusively traced to Pakistani origin.
Following these provocations, India conducted precision strikes against Pakistani Air Defence systems at a number of locations in Pakistan.   These strikes were deliberately confined to the neutralization of systems that had facilitated the earlier Pakistani assault and were executed under the guiding principle of “equal intensity in the same domain.” By targeting only those installations directly involved in the aggression, India balanced the imperative of deterrence with its overarching commitment to de-escalation. Concurrently, along the Line of Control in Jammu & Kashmir, Pakistan escalated to unprovoked mortar and heavy-calibre artillery fire into civilian areas in which sixteen innocent lives were lost, including three women and five children.  Here too, India was compelled to respond in equal proportion with mortar and artillery fire.  Indian Armed forces reiterate their commitment to non-escalation, however, any attempts by Pakistan to escalate will be responded firmly. 
"""
doc = nlp(news_article)

# Sentence tokenization
sentences = [sent.text for sent in doc.sents]
print("Sentence tokenization: \n", sentences)

# POS tagging
pos_tags = [(token.text, token.pos_) for token in doc]
print("\nPOS tagging: \n", pos_tags)

# Named Entity Recognition
entities = [(ent.text, ent.label_) for ent in doc.ents]
print("\nNamed Entity Recognition: \n", entities)

# Most common noun phrases
noun_phrases = [chunk.text for chunk in doc.noun_chunks]  
print("\nMost common noun phrases: \n", noun_phrases)


# All named entities (Person, Location, Organization)
persons = []
locations = []
organizations = []

for ent in doc.ents:
    if ent.label_ == "PERSON":
        persons.append(ent.text)
    elif ent.label_ == "ORG":
        organizations.append(ent.text)
    elif ent.label_ == "GPE":
        locations.append(ent.text)

print("\nPersons:", persons)
print("Organizations:", organizations)
print("Locations:", locations)

# Visualize a parse tree for at least 5 sentences.
sentences = list(doc.sents)[:5]
for sent in sentences:
    displacy.serve(sent, style="dep")