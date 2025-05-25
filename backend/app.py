from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from database import criar_tabelas, conectar

app = Flask(__name__)
CORS(app)

# Cria as tabelas ao iniciar o app
criar_tabelas()

# --- Autenticação ---
@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    email = dados.get('email')
    senha = dados.get('senha')
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT nome, perfil FROM usuarios WHERE email=? AND senha=?", (email, senha))
    usuario = cur.fetchone()
    conn.close()
    if usuario:
        return jsonify({"status": "ok", "usuario": usuario[0], "perfil": usuario[1]})
    return jsonify({"status": "erro", "mensagem": "Credenciais inválidas"}), 401

# --- Municípios ---
@app.route('/municipios', methods=['GET'])
def listar_municipios():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, sci, responsavel FROM municipios")
    lista = [
        {"id": row[0], "nome": row[1], "sci": row[2], "responsavel": row[3]}
        for row in cur.fetchall()
    ]
    conn.close()
    return jsonify(lista)

@app.route('/municipios', methods=['POST'])
def adicionar_municipio():
    dados = request.json
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO municipios (nome, sci, responsavel) VALUES (?, ?, ?)",
                (dados['nome'], dados['sci'], dados['responsavel']))
    conn.commit()
    novo_id = cur.lastrowid
    conn.close()
    return jsonify({"id": novo_id, **dados}), 201

@app.route('/municipios/<int:id>', methods=['PUT'])
def editar_municipio(id):
    dados = request.json
    conn = conectar()
    cur = conn.cursor()
    cur.execute("UPDATE municipios SET nome=?, sci=?, responsavel=? WHERE id=?",
                (dados['nome'], dados['sci'], dados['responsavel'], id))
    conn.commit()
    conn.close()
    return jsonify({"id": id, **dados})

@app.route('/municipios/<int:id>', methods=['DELETE'])
def excluir_municipio(id):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM municipios WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

# --- Usuários ---
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, email, perfil FROM usuarios")
    lista = [
        {"id": row[0], "nome": row[1], "email": row[2], "perfil": row[3]}
        for row in cur.fetchall()
    ]
    conn.close()
    return jsonify(lista)

@app.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    dados = request.json
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO usuarios (nome, email, senha, perfil) VALUES (?, ?, ?, ?)",
                (dados['nome'], dados['email'], dados['senha'], dados['perfil']))
    conn.commit()
    novo_id = cur.lastrowid
    conn.close()
    return jsonify({"id": novo_id, **dados}), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario(id):
    dados = request.json
    conn = conectar()
    cur = conn.cursor()
    cur.execute("UPDATE usuarios SET nome=?, email=?, senha=?, perfil=? WHERE id=?",
                (dados['nome'], dados['email'], dados['senha'], dados['perfil'], id))
    conn.commit()
    conn.close()
    return jsonify({"id": id, **dados})

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM usuarios WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

# --- Rota de teste ---
@app.route('/')
def home():
    return jsonify({"mensagem": "Backend SCI rodando!"})

if __name__ == '__main__':
    app.run(debug=True)