# nacr/similarity.py
import numpy as np
from .features import extract_features
from .noise import add_noise

def stability_score(chunk, k=5):
    base = extract_features(chunk)
    diffs = []

    for _ in range(k):
        noisy = chunk.copy()
        noisy["data"] = add_noise(noisy["data"])
        nf = extract_features(noisy)
        diffs.append(np.linalg.norm(base - nf))

    return 1.0 - np.mean(diffs)


def noise_variance(chunk, k=5):
    feats = []

    for _ in range(k):
        noisy = chunk.copy()
        noisy["data"] = add_noise(noisy["data"])
        feats.append(extract_features(noisy))

    return np.var(feats)


def similarity_density(chunk, all_features, threshold=0.85):
    f = chunk["feature"]
    sims = []

    for other in all_features:
        sim = np.dot(f, other) / (np.linalg.norm(f) * np.linalg.norm(other) + 1e-6)
        if sim > threshold:
            sims.append(sim)

    return np.sum(sims)
