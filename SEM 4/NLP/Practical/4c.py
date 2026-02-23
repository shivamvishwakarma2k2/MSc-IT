import nltk
from nltk.corpus import treebank
from nltk import pos_tag, ne_chunk
from nltk.tree import Tree

# Ensure necessary NLTK datasets are downloaded
nltk.download('treebank')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')

# Step 1: Load sentences from the treebank corpus
sentence = treebank.sents()[0] # Use the first sentence as an example

# Step 2: Part-of-Speech tagging
pos_tagged_sentence = pos_tag(sentence)

# Step 3: Perform Named Entity Recognition
named_entity_tree = ne_chunk(pos_tagged_sentence)

# Step 4: Display the named entity tree
print(named_entity_tree)

# Step 5: Draw the named entity tree (requires GUI support)
named_entity_tree.draw()