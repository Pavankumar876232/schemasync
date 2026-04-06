import psycopg2

def get_connection():
    return psycopg2.connect(
        "postgresql://postgres:[YOUR-PASSWORD]@db.xxdgfjmnjdhcxkihyuzk.supabase.co:5432/postgres"
    )