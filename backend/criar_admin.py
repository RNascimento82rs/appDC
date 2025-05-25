from database import conectar

conn = conectar()
cur = conn.cursor()
cur.execute("INSERT INTO usuarios (nome, email, senha, perfil) VALUES (?, ?, ?, ?)",
            ("Administrador", "admin@exemplo.com", "123456", "Administrador"))
conn.commit()
conn.close()
print("Usuário admin criado!")