from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os

app = FastAPI()

# ✅ CORS (IMPORTANT for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ DB connection
def get_connection():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

# ✅ Home route
@app.get("/")
def home():
    return {"message": "SchemaSync Running"}

# ✅ Get current DB schema
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

# ✅ Compare schema (FIXED → POST)
@app.post("/compare")
async def compare_schema(request: Request):
    new_schema = await request.json()

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

    # --- DIFF LOGIC ---
    added = []
    removed = []
    modified = []

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

    # --- COMPATIBILITY ---
    compatibility = []

    for col in added:
        compatibility.append({
            "column": col,
            "status": "SAFE",
            "message": "New column added"
        })

    for col in removed:
        compatibility.append({
            "column": col,
            "status": "BREAKING",
            "message": "Column removed"
        })

    for col in modified:
        compatibility.append({
            "column": col,
            "status": "WARNING",
            "message": "Column type changed"
        })

    # --- MIGRATION SQL ---
    migration_sql = []

    for table in new_schema:
        for col, dtype in new_schema[table].items():
            if table not in current_schema or col not in current_schema.get(table, {}):
                migration_sql.append(
                    f"ALTER TABLE {table} ADD COLUMN {col} {dtype};"
                )

    return {
        "diff": diff,
        "compatibility": compatibility,
        "migration_sql": migration_sql
    }