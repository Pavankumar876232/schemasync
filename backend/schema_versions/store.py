import json
import os
from datetime import datetime

HISTORY_FILE = "schema_history.json"

def save_schema(schema, diff, user_id):
    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)

    entry = {
        "user_id": user_id,
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "schema": schema,
        "diff": diff
    }

    history.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)