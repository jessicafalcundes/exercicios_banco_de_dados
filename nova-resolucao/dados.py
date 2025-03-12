import sqlite3

conn = sqlite3.connect('banco-exercicios.db')
cursor = conn.cursor()

#inserir dados
alunos = [
    (1, "Jessica", 27, "Engenharia"),
    (2, "Guilherme", 26, "Análise e Desenvolvimento de Sistemas"),
    (3, "Bianca", 26, "Enfermagem"),
    (4, "Thiago", 25, "Educação Física"),
    (5, "Matheus", 22, "Gestão Empresarial")
]

#cursor.executemany('INSERT INTO alunos VALUES (?, ?, ?, ?)', alunos)
#cursor.execute('INSERT INTO alunos(nome, idade, curso) VALUES ("Guilherme", 26, "Análise e Desenvolvimento de Sistemas")')

# consulta de todos os registros
#tabela = cursor.execute('SELECT * FROM alunos')
#for aluno in tabela:
    #print(aluno)


# selecionar nome e a idade dos alunos com mais de 20 anos
#tabela = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
#for aluno in tabela:
    #print(aluno)


# selecionar os alunos do curso de "Engenharia" em ordem alfabética
#tabela = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
#for aluno in tabela:
    #print(aluno)


# contar o número total de alunos na tabela
#tabela = cursor.execute('SELECT COUNT(*) FROM alunos')
#for aluno in tabela:
    #print(aluno)


# atualização e remoção
# atualize a idade de um aluno específico na tabela

#cursor.execute('UPDATE alunos SET idade=26 WHERE nome="Thiago"')

# remova um aluno pelo seu ID
#cursor.execute('DELETE FROM alunos WHERE id=2')


# inserindo registros na tabela "clientes"
# insira alguns registros de clientes na tabela

clientes = [
    (1, "Rogério", 56, 15000.50),
    (2, "Vanessa", 45, 20000.35),
    (3, "Sérgio", 50, 500.30),
    (4, "Paulo", 24, 5000.28),
    (5, "Thais", 30, 100.99)
]
#cursor.executemany('INSERT INTO clientes VALUES (?, ?, ?, ?)', clientes)


# selecione o nome e a idade dos clientes com idade superior a 30 anos.
#tabela = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
#for cliente in tabela:
    #print(cliente)


# calcule o saldo médio dos clientes
#tabela = cursor.execute('SELECT AVG(saldo) FROM clientes')
#for cliente in tabela:
    #print(f"Saldo médio dos clientes: {cliente[0]:.2f}")


# encontre o cliente com o saldo máximo
#tabela = cursor.execute('SELECT nome FROM clientes ORDER BY saldo DESC LIMIT 1')
#for cliente in tabela:
    #print(f"Cliente com maior saldo: {cliente}")



# conte quantos clientes têm saldo acima de 1000.
#tabela = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
#for cliente in tabela:
    #print(f"Quantidade de clientes com saldo acima de 1000: {cliente[0]}")


# atualize o saldo de um cliente específico.
#cursor.execute('UPDATE clientes SET saldo = saldo + 300 WHERE nome="Thais"')

# remova um cliente pelo seu ID
#cursor.execute('DELETE FROM clientes WHERE id = 5')



# insira algumas compras associadas a clientes existentes na tabela "clientes"

compras = [
    (1, 1, "Câmera fotográfica", 5300.00),
    (2, 3, "Vinho", 565.23),
    (3, 4, "Disco de vinil", 360.45)
]
#cursor.executemany('INSERT INTO compras VALUES (?, ?, ?, ?)', compras)

# escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra

#tabela = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id')
#for compra in tabela:
    #print(f"nome do cliente, o produto e o valor de cada compra: {compra}")



conn.commit()
conn.close()