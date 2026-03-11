import numpy as np
import re
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score
from collections import Counter


# Class 1: Sports & Athletics (Context: Winning/Medals)
doc1 = "The gold medal price is high effort"
doc2 = "Winning a gold medal needs a high jump"
doc3 = "Market for a gold medal is a trade of sweat"
doc4 = "The athlete will trade all for a gold medal"

# Class 2: Finance & Economy (Context: Market/Investment)
doc5 = "The gold bars price is high today"
doc6 = "Investing in gold bars needs a high rate"
doc7 = "Market for gold bars is a trade of money"
doc8 = "The bank will trade all for gold bars"

# Training / Clustering

all_docs = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]


true_labels = [0,0,0,0,1,1,1,1]

# Preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  
    tokens = text.split()
    return tokens



# N-gram creation
def generate_ngrams(tokens, n):
    return [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]



# Vectorization

def vectorize(docs, n_gram_size=1):

    processed_docs = []
    vocab = set()

    for doc in docs:
        tokens = preprocess_text(doc)
        ngrams = generate_ngrams(tokens, n_gram_size)
        processed_docs.append(ngrams)
        vocab.update(ngrams)

    vocab = sorted(list(vocab))
    vocab_index = {word:i for i,word in enumerate(vocab)}

    X = np.zeros((len(docs), len(vocab)))

    for i, doc in enumerate(processed_docs):
        counts = Counter(doc)
        for term, freq in counts.items():
            j = vocab_index[term]
            X[i][j] = freq

    return X



# 1-gram Experiment
X1 = vectorize(all_docs, n_gram_size=1)

km1 = KMeans(n_clusters=2, random_state=42)
labels1 = km1.fit_predict(X1)

# 2-gram Experiment
X2 = vectorize(all_docs, n_gram_size=2)
km2 = KMeans(n_clusters=2, random_state=42)
labels2 = km2.fit_predict(X2)



# regler cluster label ambiguity
def best_accuracy(true, pred):
    acc1 = accuracy_score(true, pred)
    acc2 = accuracy_score(true, 1-np.array(pred))
    return max(acc1, acc2)


def best_precision(true, pred):
    p1 = precision_score(true, pred)
    p2 = precision_score(true, 1-np.array(pred))
    return max(p1, p2)

print(f"1-gram clusters: {km1.labels_}")
print(f"2-gram clusters: {km2.labels_}")

print("\n1-gram Accuracy:", best_accuracy(true_labels, labels1))
print("1-gram Precision:", best_precision(true_labels, labels1))

print("\n2-gram Accuracy:", best_accuracy(true_labels, labels2))
print("2-gram Precision:", best_precision(true_labels, labels2))