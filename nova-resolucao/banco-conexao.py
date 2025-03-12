import sqlite3

conn = sqlite3.connect('banco-exercicios.db')
cursor = conn.cursor()

#cursor.execute('CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), idade INT, curso TEXT)')
#cursor.execute('DROP TABLE alunos')

#cursor.execute('CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), idade INTEGER, saldo REAL)')
#cursor.execute('DROP TABLE clientes')

cursor.execute('CREATE TABLE IF NOT EXISTS compras(id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER, produto TEXT, valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

conn.commit()
conn.close()