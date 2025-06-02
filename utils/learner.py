import json
import os

DATA_FILE = "data/pairs.json"

def load_pairs():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_pairs(pairs):
    with open(DATA_FILE, "w") as f:
        json.dump(pairs, f, indent=2)

def learn_pair(message, reply):
    if not message or not reply:
        return
    pairs = load_pairs()
    for item in pairs:
        if item["message"].lower() == message.lower() and item["reply"].lower() == reply.lower():
            item["score"] += 1
            break
    else:
        pairs.append({"message": message, "reply": reply, "score": 1})
    save_pairs(pairs)