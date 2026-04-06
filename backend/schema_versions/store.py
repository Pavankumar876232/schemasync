import json
import os
from datetime import datetime

FOLDER = "schema_versions"

def save_schema(schema):
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{FOLDER}/schema_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(schema, f, indent=4)

    return filename


def get_all_versions():
    if not os.path.exists(FOLDER):
        return []

    files = os.listdir(FOLDER)

    # ✅ filter only schema json files
    schema_files = [f for f in files if f.endswith(".json")]

    schema_files.sort(reverse=True)
    return schema_files