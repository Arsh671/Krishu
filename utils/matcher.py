from fuzzywuzzy import fuzz
from .learner import load_pairs

def find_best_reply(message, threshold=60):
    pairs = load_pairs()
    best_match = None
    best_score = 0
    for item in pairs:
        score = fuzz.ratio(message.lower(), item["message"].lower())
        if score > best_score and score >= threshold:
            best_match = item
            best_score = score
    return best_match["reply"] if best_match else None