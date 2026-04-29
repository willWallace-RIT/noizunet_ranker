# nacr/features.py
import numpy as np
from scipy.fftpack import dct

def extract_features(chunk):
    img = chunk["data"]

    # Low-frequency structure (DCT)
    gray = img.mean(axis=2)
    dct_low = dct(dct(gray.T, norm='ortho').T, norm='ortho')[:8, :8].flatten()

    # Color distribution
    color_hist = np.histogram(img, bins=16, range=(0, 255))[0]
    color_hist = color_hist / (color_hist.sum() + 1e-6)

    # Edge energy (simple gradient)
    gx = np.gradient(gray, axis=0)
    gy = np.gradient(gray, axis=1)
    edge_energy = np.mean(np.sqrt(gx**2 + gy**2))

    return np.concatenate([dct_low, color_hist, [edge_energy]])
