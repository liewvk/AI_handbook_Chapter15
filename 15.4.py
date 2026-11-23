import numpy as np

def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

a = np.array([1.0, 0.0])
b = np.array([0.8, 0.6])
print(f"Cosine similarity: {cosine_similarity(a, b):.2f}")

