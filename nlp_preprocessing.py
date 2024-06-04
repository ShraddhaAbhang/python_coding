import re
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Data Preprocessing and Text Cleaning

def preprocess_text(text):
    """
    Preprocess the input text by performing several cleaning steps:
    1. Convert the text to lowercase.
    2. Remove URLs.
    3. Remove HTML tags.
    4. Remove punctuation characters.
    5. Remove extra whitespace.
    
    Parameters:
    text (str): The input text to be preprocessed.
    
    Returns:
    str: The cleaned and preprocessed text.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\s+', ' ', text)
    
    # Remove HTML tags
    text = re.sub(r'<.*?>', ' ', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text

# Example usage of preprocess_text
raw_text = "Here's an example text with a URL: https://example.com and some <b>HTML</b> tags!"
cleaned_text = preprocess_text(raw_text)
print("Cleaned Text:", cleaned_text)



####################################################################################################
####################################################################################################

# Tokenization and Stemming/Lemmatization

# Sample text for tokenization, stemming, and lemmatization
text = "This is a sample text for tokenization."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)
# Output: ['This', 'is', 'a', 'sample', 'text', 'for', 'tokenization', '.']

sentences = sent_tokenize(text)
print("Sentences:", sentences)
# Output: ['This is a sample text for tokenization.']

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in tokens]
print("Stemmed Tokens:", stemmed_tokens)
# Output: ['thi', 'is', 'a', 'sampl', 'text', 'for', 'token', '.']

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
print("Lemmatized Tokens:", lemmatized_tokens)
# Output: ['This', 'is', 'a', 'sample', 'text', 'for', 'tokenization', '.']
