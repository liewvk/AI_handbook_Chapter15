vocab = {"AI": 10, "helps": 22, "students": 35, ".": 7}
reverse_vocab = {value: key for key, value in vocab.items()}
tokens = ["AI", "helps", "students", "."]
ids = [vocab[token] for token in tokens]
decoded = " ".join(reverse_vocab[i] for i in ids)
print("IDs:", ids)
print("Decoded:", decoded)

