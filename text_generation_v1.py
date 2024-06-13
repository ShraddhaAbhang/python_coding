import nltk
nltk.download('wordnet')
import random
from nltk.corpus import wordnet


# Function to find similar words using WordNet
def get_similar_words(word):
    similar_words = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            similar_words.add(lemma.name())
    similar_words = list(similar_words)
    if word in similar_words:
        similar_words.remove(word)  # Remove the input word itself
    return similar_words

def sentence_generator(input_sentence):
    # Tokenize the input sentence
    input_words = input_sentence.split()
   
    # Extract the first word from the input sentence to use as the context
    input_word = input_words[0].lower()  # Use lowercase for consistency
   
    # Find similar words for the input word
    similar_words = get_similar_words(input_word)
   
    # Replace each word in the input sentence with a similar word (if available)
    generated_sentence = []
    for word in input_words:
        input_word = word.lower()
        similar_words = get_similar_words(input_word)
        # Use a similar word for the context word
        similar_word = random.choice(similar_words) if similar_words else word
        generated_sentence.append(similar_word)
        # Keep other words unchanged
        # generated_sentence.append(word)
   
    # Join the words back into a sentence
    generated_sentence = ' '.join(generated_sentence)
   
    return generated_sentence

# Example usage:
input_sentence = "The scientist created a new invention in the laboratory."
print("Input Sentence:", input_sentence)
print("Generated Sentence:", sentence_generator(input_sentence))
