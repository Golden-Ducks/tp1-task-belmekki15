
# simple text processing + kmeans

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

# first time only
nltk.download('stopwords')


texts = [
"Muslims are praying and giving charity today",
"People are fasting and praying during Ramadan",
"The community gathers to pray and help the needy",
"Customers are buying and giving feedback today",
"People are shopping and giving reviews online",
"The community gathers to buy and help new clients"
]

# not used in clustering
labels = [0,0,0,1,1,1]   # 0 muslim , 1 = commercial
#text preprocessing
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

clean_texts = []

for text in texts:

    # lowercase
    text = text.lower()

    # pas de punctuation
    text = re.sub(r'[^a-z\s]', '', text)

    # tokenization
    words = text.split()

    # enleverstopwords
    words = [w for w in words if w not in stop_words]

    #normalization
    words = [stemmer.stem(w) for w in words]

    # join again
    clean = " ".join(words)

    clean_texts.append(clean)

print("clean texts:")
for t in clean_texts:
    print(t)

#3- bag of words (one gram)


vectorizer = CountVectorizer(ngram_range=(1,1))

X = vectorizer.fit_transform(clean_texts)

print("\nvocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBOW matrix:")
print(X.toarray())

# 4) K-means clustering
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)
clusters = kmeans.labels_

print("\nclusters result:")
print(clusters)



#text avec cluster
print("\ntext + predicted cluster:\n")

for i in range(len(texts)):
    print("text:", texts[i])
    print("cluster:", clusters[i])
    print()



#problem with one gram BOW: model only looks at words, not the meaning or context.that's why the code doesnt work so well (i hope)
#example: word 'help' appears in religious and commercial texts, so sometimes clustering can confuse
