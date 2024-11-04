from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    connection = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("POSTGRES_DB", "sql_dev"),
        user=os.getenv("POSTGRES_USER", "aleira"),
        password=os.getenv("POSTGRES_PASSWORD", "shifta20")
    )
    return connection

@app.route('/mujeres', methods=['GET'])
def listar_mujeres():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT nombre, apellido, documento FROM personas WHERE sexo = 'F'")
    mujeres = cur.fetchall()
    cur.close()
    conn.close()
    
    # Cambiamos aquí para asegurar que los tres campos se devuelvan
    return jsonify([{"Nombre": nombre, "apellido": apellido, "documento": documento}for nombre, apellido, documento in mujeres])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
