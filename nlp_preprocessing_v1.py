
# Importing necessary libraries
from nltk.tokenize import word_tokenize, sent_tokenize
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from textblob import TextBlob
import re
from gensim.models import Word2Vec
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler



# 2.1 Tokenization
## 2.1.1 Word Tokenization
# Example text
text = "This is an example sentence."

# Tokenizing the text into words
tokens = word_tokenize(text)

# Output the tokens
print("Word Tokenization:", tokens)  # Output: ['This', 'is', 'an', 'example', 'sentence', '.']


######################################################################################################################


## 2.1.2 Sentence Tokenization
# Example text
text = "Hello world. This is a second sentence."

# Tokenizing the text into sentences
sentences = sent_tokenize(text)

# Output the sentences
print("Sentence Tokenization:", sentences)  # Output: ['Hello world.', 'This is a second sentence.']


######################################################################################################################


# 2.2 Lowercasing
# Example text
text = "Hello World!"

# Converting text to lowercase
lowercased_text = text.lower()

# Output the lowercased text
print("Lowercasing:", lowercased_text)  # Output: 'hello world!'


######################################################################################################################


# 2.3 Removing Punctuation
# Example text
text = "Hello, world!"

# Removing punctuation
clean_text = text.translate(str.maketrans('', '', string.punctuation))

# Output the cleaned text
print("Removing Punctuation:", clean_text)  # Output: 'Hello world'


######################################################################################################################


# 2.4 Removing Stop Words
# Function to remove stop words from a list of tokens
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

# Example tokens
tokens = ["this", "is", "an", "example", "sentence"]

# Removing stop words
filtered_tokens = remove_stopwords(tokens)

# Output the filtered tokens
print("Removing Stop Words:", filtered_tokens)  # Output: ['example', 'sentence']


######################################################################################################################


# 2.5 Stemming and Lemmatization
## 2.5.1 Stemming
# Initialize the stemmer
stemmer = PorterStemmer()

# Example tokens
tokens = ["running", "jumps", "easily"]

# Applying stemming
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Output the stemmed tokens
print("Stemming:", stemmed_tokens)  # Output: ['run', 'jump', 'easili']


######################################################################################################################


## 2.5.2 Lemmatization
# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Example tokens
tokens = ["running", "jumps", "easily"]

# Applying lemmatization
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

# Output the lemmatized tokens
print("Lemmatization:", lemmatized_tokens)  # Output: ['running', 'jump', 'easily']


######################################################################################################################


# 2.6 Handling Negations
# Function to handle negations in text
def handle_negations(text):
    tokens = word_tokenize(text)
    negations = {"not", "no", "never"}
    negated_tokens = []
    negate = False
    for token in tokens:
        if token in negations:
            negate = not negate
        elif negate:
            negated_tokens.append("not_" + token)
            negate = False
        else:
            negated_tokens.append(token)
    return negated_tokens

# Example text
text = "I do not like this movie."

# Handling negations
handled_negations = handle_negations(text)

# Output the tokens with handled negations
print("Handling Negations:", handled_negations)  # Output: ['I', 'do', 'not_like', 'this', 'movie', '.']


######################################################################################################################


# 2.7 Spelling Correction
# Example text with spelling error
text = "I hav a speling error."

# Correcting the spelling
corrected_text = str(TextBlob(text).correct())

# Output the corrected text
print("Spelling Correction:", corrected_text)  # Output: 'I have a spelling error.'


######################################################################################################################


# 2.8 Removing Special Characters
# Example text
text = "Hello @world! #amazing"

# Removing special characters
clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

# Output the cleaned text
print("Removing Special Characters:", clean_text)  # Output: 'Hello world amazing'


######################################################################################################################


# 3.1 Word Embeddings
# Example sentences
sentences = [["this", "is", "a", "sentence"], ["this", "is", "another", "sentence"]]

# Training a Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Getting the vector for the word 'sentence'
vector = model.wv['sentence']

# Output the vector for 'sentence'
print("Word Embeddings (vector for 'sentence'):", vector)


######################################################################################################################


# 3.2 Handling Imbalanced Data
## 3.2.1 Oversampling
# Example data
X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

# Applying Random Oversampling
ros = RandomOverSampler()
X_resampled, y_resampled = ros.fit_resample(X, y)

# Output the resampled data
print("Oversampling - X_resampled:", X_resampled)  # Output: [[1], [2], [3], [4], [5], [4], [5]]
print("Oversampling - y_resampled:", y_resampled)  # Output: [0, 0, 0, 1, 1, 1, 1]


######################################################################################################################


## 3.2.2 Undersampling
# Applying Random Undersampling
rus = RandomUnderSampler()
X_resampled, y_resampled = rus.fit_resample(X, y)

# Output the resampled data
print("Undersampling - X_resampled:", X_resampled)  # Output: [[3], [4], [5], [4], [5]]
print("Undersampling - y_resampled:", y_resampled)  # Output: [0, 1, 1, 1, 1]


######################################################################################################################


## 3.2.3 Synthetic Data Generation
# Applying SMOTE for synthetic data generation
smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X, y)

# Output the resampled data
print("Synthetic Data Generation (SMOTE) - X_resampled:", X_resampled)  # Example output: [[1], [2], [3], [4], [5], [1.2], [3.4]]
print("Synthetic Data Generation (SMOTE) - y_resampled:", y_resampled)  # Example output: [0, 0, 0, 1, 1, 0, 1]
