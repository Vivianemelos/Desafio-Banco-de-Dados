import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).

# Criar a tabela 'alunos' (se ainda não foi criada)
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    curso TEXT NOT NULL
)
''')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

# Inserir dados na tabela 'alunos'
dados_alunos = [
    (1, "Ana Silva", 20, "Engenharia"),
    (2, "Bruno Souza", 22, "Medicina"),
    (3, "Carla Pereira", 19, "Engenharia"),
    (4, "Daniel Oliveira", 21, "Ciência da Computação"),
    (5, "Ester Fernandes", 23, "Engenharia")
]

# Inserir os dados
cursor.executemany('''
INSERT INTO alunos (id, nome, idade, curso)
VALUES (?, ?, ?, ?)
''', dados_alunos)

# 3. Consultas Básicas. Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecionar todos os registros da tabela "alunos".
print("a) Todos os registros da tabela 'alunos':")
cursor.execute('SELECT * FROM alunos')
todos_os_alunos = cursor.fetchall()
for aluno in todos_os_alunos:
    print(aluno)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
print("\nb) Nome e idade dos alunos com mais de 20 anos:")
cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
alunos_mais_de_20 = cursor.fetchall()
for aluno in alunos_mais_de_20:
    print(aluno)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
print("\nc) Alunos do curso de 'Engenharia' em ordem alfabética:")
cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
alunos_engenharia = cursor.fetchall()
for aluno in alunos_engenharia:
    print(aluno)

# d) Contar o número total de alunos na tabela
print("\nd) Número total de alunos na tabela:")
cursor.execute('SELECT COUNT(*) FROM alunos')
total_alunos = cursor.fetchone()[0]
print(total_alunos)

# 4. Atualização e Remoção

# a) Atualizar a idade de um aluno específico na tabela.
print("a) Atualizar a idade de um aluno específico:")
cursor.execute('''
UPDATE alunos SET idade = 25 WHERE id = 2
''')
cursor.execute('SELECT * FROM alunos WHERE id = 2')
aluno_atualizado = cursor.fetchone()
print(aluno_atualizado)

# b) Remover um aluno pelo seu ID.
print("\nb) Remover um aluno pelo seu ID:")
cursor.execute('''
DELETE FROM alunos WHERE id = 3
''')

# Confirmar as alterações e fechar a conexão
conexao.commit()
conexao.close()

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

# 5. Criar uma Tabela e Inserir Dados

# Criar a tabela 'clientes'
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    saldo REAL NOT NULL
)
''')

# Inserir dados na tabela 'clientes' (caso ainda não estejam inseridos)
dados_clientes = [
    (1, "Maria Joaquina", 30, 1500.75),
    (2, "Carlos Silva", 45, 2000.00),
    (3, "Fernanda Lima", 25, 320.50),
    (4, "Roberto Almeida", 50, 2500.00),
    (5, "Ana Beatriz", 28, 450.30)
]

cursor.executemany('''
INSERT OR IGNORE INTO clientes (id, nome, idade, saldo)
VALUES (?, ?, ?, ?)
''', dados_clientes)

# 6. Consultas e Funções Agregadas. Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecionar o nome e a idade dos clientes com idade superior a 30 anos.
print("a) Nome e idade dos clientes com idade superior a 30 anos:")
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
clientes_acima_30 = cursor.fetchall()
for cliente in clientes_acima_30:
    print(cliente)

# b) Calcular o saldo médio dos clientes.
print("\nb) Saldo médio dos clientes:")
cursor.execute('SELECT AVG(saldo) FROM clientes')
saldo_medio = cursor.fetchone()[0]
print(saldo_medio)

# c) Encontrar o cliente com o saldo máximo.
print("\nc) Cliente com o saldo máximo:")
cursor.execute('SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')
cliente_max_saldo = cursor.fetchone()
print(cliente_max_saldo)

# d) Contar quantos clientes têm saldo acima de 1000.
print("\nd) Número de clientes com saldo acima de 1000:")
cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
clientes_acima_1000 = cursor.fetchone()[0]
print(clientes_acima_1000)

# Consultar e imprimir todos os dados inseridos
print("\nTodos os dados da tabela 'clientes':")
cursor.execute('SELECT * FROM clientes')
dados = cursor.fetchall()
for cliente in dados:
    print(cliente)

# 7. Atualização e Remoção com Condições

# a) Atualizar o saldo de um cliente específico.
print("a) Atualizar o saldo de um cliente específico:")
cursor.execute('''
UPDATE clientes SET saldo = 1800.50 WHERE id = 2
''')
cursor.execute('SELECT * FROM clientes WHERE id = 2')
cliente_atualizado = cursor.fetchone()
print(cliente_atualizado)

# b) Remover um cliente pelo seu ID.
print("\nb) Remover um cliente pelo seu ID:")
cursor.execute('''
DELETE FROM clientes WHERE id = 3
''')

# 8. Junção de Tabelas
# Criar a tabela 'compras' (caso ainda não exista)
cursor.execute('''
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    produto TEXT NOT NULL,
    valor REAL NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
''')

# Inserir dados na tabela 'compras' (caso ainda não estejam inseridos)
dados_compras = [
    (1, 2, "Celular", 1500.00),
    (2, 4, "Notebook", 2500.00),
    (3, 1, "Tablet", 800.00),
    (4, 5, "Câmera", 500.00),
    (5, 3, "Smartwatch", 300.00)
]

cursor.executemany('''
INSERT OR IGNORE INTO compras (id, cliente_id, produto, valor)
VALUES (?, ?, ?, ?)
''', dados_compras)

# Consulta para exibir o nome do cliente, produto e valor de cada compra
cursor.execute('''
SELECT c.nome AS Cliente, co.produto AS Produto, co.valor AS Valor
FROM compras co
JOIN clientes c ON c.id = co.cliente_id
''')
dados_consulta = cursor.fetchall()

# Imprimir os resultados da consulta
print("Consulta - Nome do Cliente, Produto e Valor de Cada Compra:")
for linha in dados_consulta:
    print(linha)

# Confirmar as alterações e fechar a conexão
conexao.commit()
conexao.close()