from fastapi import FastAPI
from schema_tracker.tracker import get_schema
from diff_engine.diff import compare_schema
from compatibility_checker.checker import check_compatibility
from schema_tracker.version_store import save_schema
from migrations.llm_generator import generate_sql   # 👈 NEW

app = FastAPI()

old_schema = {}

@app.get("/")
def home():
    return {"message": "SchemaSync Running"}

@app.get("/schema")
def schema():
    return get_schema()

@app.get("/compare")
def compare():
    global old_schema

    # First call → save old schema
    if not old_schema:
        old_schema = get_schema()
        filename = save_schema(old_schema)
        return {
            "message": "Old schema saved",
            "file": filename
        }

    # Second call → compare + generate SQL
    new_schema = get_schema()
    diff = compare_schema(old_schema, new_schema)
    compatibility = check_compatibility(diff)

    filename = save_schema(new_schema)

    sql_queries = generate_sql(diff)   # 👈 NEW

    return {
        "diff": diff,
        "compatibility": compatibility,
        "migration_sql": sql_queries,   # 👈 NEW
        "saved_file": filename
    }