import json
from datetime import datetime

def save_schema(schema):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"schema_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(schema, f, indent=4)

    return filename