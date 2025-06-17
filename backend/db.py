import psycopg2

def get_connection():
    return psycopg2.connect(
        host='db',
        database='notasdb',
        user='postgres',
        password='postgres'
    )
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notas (
            id SERIAL PRIMARY KEY,
            titulo TEXT NOT NULL,
            contenido TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
