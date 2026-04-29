# nacr/chunking.py
import numpy as np

def chunk_image(image, chunk_size=32):
    h, w, c = image.shape
    chunks = []

    for y in range(0, h, chunk_size):
        for x in range(0, w, chunk_size):
            patch = image[y:y+chunk_size, x:x+chunk_size]
            if patch.shape[0] == chunk_size and patch.shape[1] == chunk_size:
                chunks.append({
                    "data": patch,
                    "pos": (y, x)
                })

    return chunks
