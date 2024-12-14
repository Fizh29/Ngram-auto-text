import nltk
from nltk.corpus import *
import random

# Download the Brown corpus if not already available
nltk.download('brown')

# Load sentences from the Brown corpus
sentences = nltk.corpus.brown.sents()

# Initialize the n-grams dictionary
n_grams = {}

# Build the n-grams dictionary
for sentence in sentences:
    words = [word for word in sentence if word[0].isalpha()]
    for ix in range(len(words) - 1):
        try:
            n_grams[words[ix]].append(words[ix + 1])
        except KeyError:
            n_grams[words[ix]] = []
            n_grams[words[ix]].append(words[ix + 1])

# Function to generate a sentence based on n-grams
def generate_sentence(nb=7):
    words = []
    next_word = random.choice(list(n_grams.keys()))
    words.append(next_word)
    while len(words) < nb:
        next_word = random.choice(n_grams[next_word])
        words.append(next_word)
    
    return " ".join(words)
