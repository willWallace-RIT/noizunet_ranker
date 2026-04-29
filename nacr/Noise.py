# nacr/noise.py
import numpy as np

def add_noise(image, sigma=0.05):
    noise = np.random.normal(0, sigma, image.shape)
    return np.clip(image + noise * 255, 0, 255)
