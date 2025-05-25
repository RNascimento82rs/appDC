import sqlite3

def conectar():
    return sqlite3.connect('database.db')

def criar_tabelas():
    conn = conectar()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS municipios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sci TEXT,
            responsavel TEXT
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT UNIQUE,
            senha TEXT,
            perfil TEXT
        )
    ''')
    conn.commit()
    conn.close()