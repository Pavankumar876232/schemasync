def compare_schema(old, new):
    added = []
    removed = []
    modified = []

    for table in new:
        if table in old:
            for col in new[table]:
                if col not in old[table]:
                    added.append(col)
                elif old[table][col] != new[table][col]:
                    modified.append(col)

    for table in old:
        if table in new:
            for col in old[table]:
                if col not in new[table]:
                    removed.append(col)

    return {
        "added": added,
        "removed": removed,
        "modified": modified
    }