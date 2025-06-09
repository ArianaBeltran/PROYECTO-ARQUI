import psycopg2

def get_connection():
    return psycopg2.connect(
        host='db',
        database='notasdb',
        user='postgres',
        password='postgres'
    )
