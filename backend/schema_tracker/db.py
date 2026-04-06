import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="schemasync",
        user="postgres",
        password="pk876232kdm@HNR"
    )