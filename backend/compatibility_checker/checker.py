def check_compatibility(diff):
    result = []

    for col in diff["added"]:
        result.append({
            "column": col,
            "status": "SAFE",
            "message": "New column added"
        })

    for col in diff["removed"]:
        result.append({
            "column": col,
            "status": "BREAKING",
            "message": "Column removed may break system"
        })

    for col in diff["modified"]:
        result.append({
            "column": col,
            "status": "RISKY",
            "message": "Column type changed"
        })

    return result