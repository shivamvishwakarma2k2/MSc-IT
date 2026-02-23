# Filename: cfg_parse_tree.py

# Define a grammar (CFG) and generate parse tree using NLTK

import nltk
from nltk.tree import *

# Function to define grammar and parse result
def definegrammar_parseresult():

    # Define a context-free grammar (CFG)
    Grammar = nltk.CFG.fromstring("""
        S -> NP VP
        PP -> P NP
        NP -> Det N | Det N PP | 'I'
        VP -> V NP | VP PP
        Det -> 'an' | 'my'
        N -> 'elephant' | 'pajamas'
        V -> 'shot'
        P -> 'in'
    """)

    # Tokenized sentence to be parsed
    sent = "I shot an elephant".split()

    # Initialize the parser with the grammar
    parser = nltk.ChartParser(Grammar)

    # Generate parse trees
    trees = list(parser.parse(sent))

    # Display parse trees
    if not trees:
        print("No parse tree found.")
    else:
        print("Parse Tree(s):\n")
        for tree in trees:
            tree.pretty_print()   # Print tree in text form
            tree.draw()           # Opens graphical tree window

# Run the function
definegrammar_parseresult()