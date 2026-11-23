import numpy as np

embeddings = np.array([
    [0.2, 0.1, 0.7],
    [0.6, 0.0, 0.2],
    [0.1, 0.8, 0.3]
])
ids = [0, 2]
print("Embedding table shape:", embeddings.shape)
print("Selected vectors:")
print(embeddings[ids])

