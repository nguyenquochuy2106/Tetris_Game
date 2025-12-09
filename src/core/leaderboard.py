import json
import os

DATA_PATH = "data/leaderboard.json"

class Leaderboard:
    def __init__(self, path=DATA_PATH):
        self.path = path
        os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)

    def load(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return []

    def save(self, records):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)

    def add_score(self, name, score):
        rec = self.load()
        rec.append({"name": name, "score": score})
        rec = sorted(rec, key=lambda r: -r["score"])[:10]  # top 10
        self.save(rec)

