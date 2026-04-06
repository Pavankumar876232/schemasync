from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os

from schema_versions.store import save_schema
from llm.migration import generate_migration

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_connection():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

@app.get("/")
def home():
    return {"message": "SchemaSync Running"}

# 🔹 GET SCHEMA
@app.get("/schema")
def get_schema():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public';
    """)

    rows = cursor.fetchall()
    conn.close()

    schema = {}
    for table, column, dtype in rows:
        if table not in schema:
            schema[table] = {}
        schema[table][column] = dtype

    return schema

# 🔹 COMPARE
@app.post("/compare")
async def compare_schema(request: Request):
    data = await request.json()

    new_schema = data.get("schema")
    user_id = data.get("user_id")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public';
    """)

    rows = cursor.fetchall()
    conn.close()

    current_schema = {}
    for table, column, dtype in rows:
        if table not in current_schema:
            current_schema[table] = {}
        current_schema[table][column] = dtype

    added, removed, modified = [], [], []

    for table in new_schema:
        if table not in current_schema:
            added.append(table)
        else:
            for col in new_schema[table]:
                if col not in current_schema[table]:
                    added.append(col)
                elif new_schema[table][col] != current_schema[table][col]:
                    modified.append(col)

            for col in current_schema[table]:
                if col not in new_schema[table]:
                    removed.append(col)

    diff = {
        "added": added,
        "removed": removed,
        "modified": modified
    }

    compatibility = []

    for col in added:
        compatibility.append({"column": col, "status": "SAFE"})

    for col in removed:
        compatibility.append({"column": col, "status": "BREAKING"})

    for col in modified:
        compatibility.append({"column": col, "status": "WARNING"})

    migration_sql = []
    for table in new_schema:
        for col, dtype in new_schema[table].items():
            if table not in current_schema or col not in current_schema.get(table, {}):
                migration_sql.append(
                    f"ALTER TABLE {table} ADD COLUMN {col} {dtype};"
                )

    # ✅ SAVE USER DATA
    save_schema(new_schema, diff, user_id)

    # ✅ AI
    llm_output = generate_migration(diff)

    return {
        "diff": diff,
        "compatibility": compatibility,
        "migration_sql": migration_sql,
        "llm_suggestion": llm_output
    }

# 🔹 USER HISTORY
@app.post("/history")
async def get_history(request: Request):
    data = await request.json()
    user_id = data.get("user_id")

    import json

    if not os.path.exists("schema_history.json"):
        return {"history": []}

    with open("schema_history.json", "r") as f:
        all_data = json.load(f)

    user_data = [item for item in all_data if item["user_id"] == user_id]

    return {"history": user_data}