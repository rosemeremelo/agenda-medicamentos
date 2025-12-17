from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def conectar_db():
    return sqlite3.connect("database.db")

@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = None

    if request.method == "POST":
        crianca = request.form["crianca"]
        remedio = request.form["remedio"]
        dosagem = request.form["dosagem"]
        quantidade = request.form["quantidade"]

        conn = conectar_db()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS medicamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                crianca TEXT,
                remedio TEXT,
                dosagem TEXT,
                quantidade TEXT
            )
        """)

        cursor.execute("""
            INSERT INTO medicamentos (crianca, remedio, dosagem, quantidade)
            VALUES (?, ?, ?, ?)
        """, (crianca, remedio, dosagem, quantidade))

        conn.commit()
        conn.close()

        mensagem = "Medicamento cadastrado com sucesso!"

    return render_template("index.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
