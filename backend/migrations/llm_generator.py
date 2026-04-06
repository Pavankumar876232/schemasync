def generate_sql(diff):
    queries = []

    # Handle added columns
    for col in diff["added"]:
        queries.append(f"ALTER TABLE users ADD COLUMN {col} VARCHAR(255);")

    # Handle removed columns
    for col in diff["removed"]:
        queries.append(f"-- WARNING: Column {col} removed. Consider backup before dropping.")

    # Handle modified columns
    for col in diff["modified"]:
        queries.append(f"-- WARNING: Column {col} type changed. Manual migration needed.")

    return queries