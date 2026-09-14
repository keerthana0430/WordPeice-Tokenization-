from collections import Counter


word_freq = {
    "hug": 2,
    "hugs": 1,
    "pug": 1
}


splits = {
    "hug": ["h", "##u", "##g"],
    "hugs": ["h", "##u", "##g", "##s"],
    "pug": ["p", "##u", "##g"]
}


token_freq = Counter()
pair_freq = Counter()


for word, freq in word_freq.items():

    tokens = splits[word]

    for token in tokens:
        token_freq[token] += freq

   
    for i in range(len(tokens) - 1):
        pair = (tokens[i], tokens[i + 1])
        pair_freq[pair] += freq


print("Token Frequencies:")
print(token_freq)

print("\nPair Frequencies:")
print(pair_freq)
