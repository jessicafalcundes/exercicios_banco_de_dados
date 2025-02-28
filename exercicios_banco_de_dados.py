import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# 1. Criar a tabela "alunos"
# Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    curso TEXT
);
''')

# 2. Inserir registros na tabela "alunos"
# Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
alunos = [
    (1, "Ana", 22, "Engenharia"),
    (2, "Bruno", 19, "Medicina"),
    (3, "Carlos", 21, "Engenharia"),
    (4, "Diana", 23, "Direito"),
    (5, "Eduardo", 20, "Administração")
]
cursor.executemany("INSERT INTO alunos VALUES (?, ?, ?, ?)", alunos)

# 3. Consultas Básicas
# a) Selecionar todos os registros da tabela "alunos".
cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
cursor.execute("SELECT nome, idade FROM alunos WHERE idade > 20")
print(cursor.fetchall())

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
cursor.execute("SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome")
print(cursor.fetchall())

# d) Contar o número total de alunos na tabela.
cursor.execute("SELECT COUNT(*) FROM alunos")
print(cursor.fetchone()[0])

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
cursor.execute("UPDATE alunos SET idade = 25 WHERE id = 1")

# b) Remova um aluno pelo seu ID.
cursor.execute("DELETE FROM alunos WHERE id = 2")

# 5. Criar tabela "clientes"
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    saldo REAL
);
''')

# Inserindo registros na tabela "clientes"
# Insira alguns registros de clientes na tabela.
clientes = [
    (1, "Lucas", 35, 1500.50),
    (2, "Mariana", 28, 750.00),
    (3, "João", 40, 2000.75),
    (4, "Clara", 32, 300.00),
    (5, "Roberto", 29, 1250.00)
]
cursor.executemany("INSERT INTO clientes VALUES (?, ?, ?, ?)", clientes)

# 6. Consultas e Funções Agregadas
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
cursor.execute("SELECT nome, idade FROM clientes WHERE idade > 30")
print(cursor.fetchall())

# b) Calcule o saldo médio dos clientes.
cursor.execute("SELECT AVG(saldo) FROM clientes")
print(cursor.fetchone()[0])

# c) Encontre o cliente com o saldo máximo.
cursor.execute("SELECT nome FROM clientes ORDER BY saldo DESC LIMIT 1")
print(cursor.fetchone()[0])

# d) Conte quantos clientes têm saldo acima de 1000.
cursor.execute("SELECT COUNT(*) FROM clientes WHERE saldo > 1000")
print(cursor.fetchone()[0])

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.
cursor.execute("UPDATE clientes SET saldo = saldo + 500 WHERE id = 1")

# b) Remova um cliente pelo seu ID.
cursor.execute("DELETE FROM clientes WHERE id = 3")

# 8. Criar a tabela "compras"
# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real).
cursor.execute('''
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    produto TEXT,
    valor REAL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
''')

# Inserindo registros na tabela "compras"
# Insira algumas compras associadas a clientes existentes na tabela "clientes".
compras = [
    (1, 1, "Notebook", 3500.00),
    (2, 2, "Celular", 2000.00),
    (3, 4, "Fone de ouvido", 250.00)
]
cursor.executemany("INSERT INTO compras VALUES (?, ?, ?, ?)", compras)

# Consulta com junção de tabelas
# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
cursor.execute('''
SELECT clientes.nome, compras.produto, compras.valor 
FROM compras 
JOIN clientes ON compras.cliente_id = clientes.id
''')
print(cursor.fetchall())

# Commit e fechar conexão
conn.commit()
conn.close()
