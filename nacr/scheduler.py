# nacr/scheduler.py

import heapq

def build_processing_queue(chunks, compute_stats_fn):
    heap = []

    for chunk in chunks:
        stats = compute_stats_fn(chunk)

        score = stats["rank_score"]

        # max heap via negative score
        heapq.heappush(heap, (-score, chunk))

    ordered = []

    while heap:
        ordered.append(heapq.heappop(heap)[1])

    return ordered
