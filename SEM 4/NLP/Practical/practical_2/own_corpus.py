# Import required libraries
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist

nltk.download('punkt_tab')

print("\nPlaintext Corpus Example")

# Create a folder named 'mycorpus' and place doc1.txt,.... inside it
# Define the corpus root folder
corpus_root = './mycorpus'

# 3. Load the corpus using PlaintextCorpusReader
my_corpus = PlaintextCorpusReader(corpus_root, '.*\.txt')

# 4. a. Display all file IDs
print("\nFile IDs in Corpus ")
print(my_corpus.fileids())

# 4. b. Display raw content of a selected file
selected_file = 'doc1.txt'
print("\nRaw Content of Selected File ")
print(my_corpus.raw(selected_file))

# 4. c. Display word tokens
print("\nFirst 30 Word Tokens ")
print(my_corpus.words()[:30])

# 4. d. Display sentence tokens
print("\nFirst 5 Sentences ")
for sent in my_corpus.sents()[:5]:
    print(sent)

# 5. a. Count total number of files
total_files = len(my_corpus.fileids())
print("\nTotal Number of Files ")
print(total_files)

# 5. b. Count total number of words
total_words = len(my_corpus.words())
print("\nTotal Number of Words ")
print(total_words)

# 5. c. Count total number of sentences
total_sentences = len(my_corpus.sents())
print("\nTotal Number of Sentences ")
print(total_sentences)

# 6. Display most frequent 10 words
freq_dist = FreqDist([w.lower() for w in my_corpus.words()])
print("\nMost Frequent 10 Words ")
print(freq_dist.most_common(10))