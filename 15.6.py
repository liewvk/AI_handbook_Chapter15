import numpy as np

logits = np.array([2.0, 1.0, 0.0])
for temperature in (0.5, 1.0, 2.0):
    scaled = logits / temperature
    scores = np.exp(scaled - np.max(scaled))
    probs = scores / scores.sum()
    print(f"T={temperature:.1f}: {np.round(probs, 3)}")

