# Documents
D1 = "I love cats"
D2 = "Cats are chill"
D3 = "I am late"

# Your Task: implement context window vectorization
# with window size = 1 (so each window is 3 tokens wide)
# Use <s> and </s> padding flags


def add_padding(tokens):
    return ["<s>"] + tokens + ["</s>"]


def extract_windows(tokens, window_size=1):

    tokens = add_padding(tokens)
    windows = []

    for i in range(window_size, len(tokens)-window_size):
        window = tuple(tokens[i-window_size:i+window_size+1])
        windows.append(window)

    return windows


def build_vocab(all_windows):

    unique_windows = sorted(set(all_windows))
    vocab = {w:i for i,w in enumerate(unique_windows)}

    return vocab


def vectorize_doc(doc_windows, vocab):

    vector = [0]*len(vocab)

    for w in doc_windows:
        if w in vocab:
            vector[vocab[w]] = 1

    return vector


# Run
all_docs = [D1, D2, D3]

docs_windows = []
all_windows = []

for doc in all_docs:

    tokens = doc.lower().split()
    windows = extract_windows(tokens)

    docs_windows.append(windows)
    all_windows.extend(windows)

vocab = build_vocab(all_windows)

vectors = [vectorize_doc(w, vocab) for w in docs_windows]


print("Vocabulary:")
for k,v in vocab.items():
    print(v, ":", k)

print("\nVectors:")
for i,v in enumerate(vectors):
    print(f"D{i+1}:", v)