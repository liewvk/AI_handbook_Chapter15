import numpy as np

words = ["learn", "work", "play"]
logits = np.array([2.0, 1.0, 0.0])
shifted = logits - np.max(logits)
probabilities = np.exp(shifted) / np.exp(shifted).sum()
for word, probability in zip(words, probabilities):
    print(f"{word}: {probability:.3f}")

