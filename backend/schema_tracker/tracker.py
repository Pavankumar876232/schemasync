from schema_tracker.db import get_connection

def get_schema():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public';
    """)

    rows = cur.fetchall()

    schema = {}

    for table, col, dtype in rows:
        if table not in schema:
            schema[table] = {}
        schema[table][col] = dtype

    cur.close()
    conn.close()

    return schema