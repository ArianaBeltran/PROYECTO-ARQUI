from flask import Flask, request, jsonify
import psycopg2
from db import get_connection
from db import init_db
app = Flask(__name__)
init_db()
@app.route('/')
def home():
    return 'Hola, el backend está vivo y funcionando 💖✨'

@app.route('/notas', methods=['GET'])
def get_notas():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, titulo, contenido FROM notas")
    notas = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{'id':n[0],'titulo': n[1],'contenido':n[2]} for n in notas])

@app.route('/notas', methods=['POST'])
def add_nota():
    data = request.get_json()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO notas (titulo, contenido) VALUES (%s, %s)", (data['titulo'], data['contenido']))
    conn.commit()
    cur.close()
    conn.close() 
    return jsonify({'message':'Nota guardada'}), 201

if __name__=='__main__':
    app.run(host='0.0.0.0')
