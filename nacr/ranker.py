# nacr/ranker.py

import numpy as np

def compute_rank(chunk, stats):
    return (
        0.35 * stats["stability"]
        + 0.25 * stats["density"]
        + 0.20 * stats["confidence"]
        - 0.15 * stats["variance"]
        - 0.05 * stats["ambiguity"]
    )
