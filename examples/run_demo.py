# examples/run_demo.py

from nacr.chunking import chunk_image
from nacr.scheduler import build_processing_queue

def compute_stats(chunk):
    # placeholder pipeline hook
    return {
        "stability": 0.8,
        "density": 0.6,
        "confidence": 0.7,
        "variance": 0.2,
        "ambiguity": 0.3,
        "rank_score": 0.75
    }

def main(image):
    chunks = chunk_image(image, 32)
    ordered = build_processing_queue(chunks, compute_stats)

    for i, chunk in enumerate(ordered):
        print(f"Processing chunk {i} at {chunk['pos']}")

if __name__ == "__main__":
    import numpy as np
    img = np.random.randint(0, 255, (256, 256, 3))
    main(img)
