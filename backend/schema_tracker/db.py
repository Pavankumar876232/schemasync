import psycopg2

def get_connection():
    return psycopg2.connect(
        host="db.xxdgfjmnjdhcxkihyuzk.supabase.co",
        database="schemasync",
        user="postgres",
        password="pk876232kdm@HNR",
        port=5432,
        sslmode="require"
    )