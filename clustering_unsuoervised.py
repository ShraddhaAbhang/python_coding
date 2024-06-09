import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# # Sample text data
# documents = [
#     "Text mining is the process of deriving useful information from text.",
#     "Natural Language Processing is a field of artificial intelligence.",
#     "Machine learning can be applied to text data for various tasks.",
#     "Clustering algorithms group similar documents together.",
#     "Text clustering is an unsupervised learning technique.",
#     "Deep learning models can process large amounts of text data.",
#     "Feature extraction converts text into numerical representations.",
#     "Tokenization splits text into words or tokens.",
#     "Stopwords are common words that are often removed from text data.",
#     "Stemming and lemmatization reduce words to their base forms."
# ]

# Sample text data
# Sample text data
documents = [
    "I enjoy going for a run every morning.",
    "Cooking healthy meals is important for maintaining good health.",
    "Spending time with family during weekends is very relaxing.",
    "I love reading books in my free time.",
    "Gardening is a great way to connect with nature.",
    "It's essential to manage stress effectively at work.",
    "Watching movies with friends is a fun activity.",
    "Practicing yoga helps improve mental and physical well-being.",
    "Traveling to new places broadens our perspectives.",
    "Playing musical instruments can be a soothing hobby.",
    "Regular exercise is key to staying fit and healthy.",
    "Volunteering for community service is very fulfilling.",
    "Taking a walk in the park is a refreshing break.",
    "Photography allows me to capture beautiful moments.",
    "Learning new languages can be very enriching.",
    "Cycling is an excellent way to explore the neighborhood.",
    "Attending workshops and seminars helps in professional growth.",
    "Painting is a wonderful way to express creativity.",
    "Meditation helps in achieving inner peace and calm.",
    "Spending time with pets can be very comforting."
]


# Text preprocessing function
def preprocess_text(text):
    text = text.lower()  # Lowercase the text
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = nltk.word_tokenize(text)  # Tokenize the text
    stopwords = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tokens if word not in stopwords]  # Remove stopwords
    return ' '.join(tokens)

# Preprocess all documents
processed_docs = [preprocess_text(doc) for doc in documents]

# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_docs)

# Perform K-Means clustering
num_clusters = 10
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Assign each document to a cluster
labels = kmeans.labels_
print(labels)

# Print the documents in each cluster
for i in range(num_clusters):
    print(f"Cluster {i}:")
    for j, label in enumerate(labels):
        if label == i:
            print(f" - {documents[j]}")

# Dimensionality reduction using PCA
pca = PCA(n_components=2)
reduced_X = pca.fit_transform(X.toarray())

# Visualize the clusters
plt.figure(figsize=(10, 7))
sns.scatterplot(x=reduced_X[:, 0], y=reduced_X[:, 1], hue=labels, palette='viridis', s=100)
plt.title('Text Clustering Visualization')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend(title='Cluster')
plt.show()
