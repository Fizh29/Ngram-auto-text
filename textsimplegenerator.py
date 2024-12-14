import nltk
from nltk.corpus import *
import random
import streamlit as st

nltk.download('brown')

sentences = nltk.corpus.brown.sents()

n_grams = {}

for sentence in sentences:
    words = [word for word in sentence if word[0].isalpha()]
    for ix in range(len(words) - 1):
        try:
            n_grams[words[ix]].append(words[ix + 1])
        except KeyError:
            n_grams[words[ix]] = []
            n_grams[words[ix]].append(words[ix + 1])

def generate_sentence_random_length(user_input="", min_words=10, max_words=25):
    target_length = random.randint(min_words, max_words)
    if user_input.strip():
        words = user_input.split()
    else:
        words = [random.choice(list(n_grams.keys()))]
    next_word = words[-1]
    while len(words) < target_length:
        try:
            next_word = random.choice(n_grams[next_word])
            words.append(next_word)
        except KeyError:
            break
    return " ".join(words)

st.title("Fancy Sentence Generator")
st.write("Generated sentences will have a random length between **10** and **25** words. \
          Type a few words to start your sentence, or leave it blank for a random one.")

user_input = st.text_input("Your starting words (leave blank for random):")

if st.button("Generate Sentence"):
    generated_sentence = generate_sentence_random_length(user_input)
    st.subheader("Generated Sentence:")
    st.write(generated_sentence)
