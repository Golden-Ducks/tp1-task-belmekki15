# Number to word dictionary
number_map = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten"
}

# punctuation list
punctuation = ".,!?;:"


#convert numbers to words
def convert_numbers(text):
    words = text.split()
    result = []

    for word in words:
        # remove punctuation temporarily
        clean_word = word
        suffix = ""

        if len(word) > 0 and word[-1] in punctuation:
            clean_word = word[:-1]
            suffix = word[-1]

        # convert if number
        if clean_word in number_map:
            clean_word = number_map[clean_word]

        result.append(clean_word + suffix)

    return " ".join(result)


#remove punctuation
def remove_punctuation(text):
    result = ""

    for char in text:
        if char not in punctuation:
            result += char
        else:
            result += " "

    return result



def normalize(text):

    # lowercase
    text = text.lower()

    text = convert_numbers(text)
    text = remove_punctuation(text)

    # normalize spaces
    words = text.split()
    text = " ".join(words)

    return text



D1 = "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza."
D2 = "Five pizza were ready, but 3 bourak burned!"
D3 = "We only had 8 chamiyya, no pizza, and one tea."
D4 = "Is 6 too much? I ate nine bourak lol."



docs = [D1, D2, D3, D4]

for i, doc in enumerate(docs, 1):
    print("D", i, ":", normalize(doc))