import sqlite3
import json


# ==================== CREATE  ==================== #
def criar_tabela():
    # Exercício 3: Criar um banco de dados SQLite com uma tabela chamada clientes.
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS clientes')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    ''')
    conn.commit()
    print("Tabela 'clientes' criada com sucesso.")
    conn.close()

# ==================== READ  ==================== #


def calcular_media_idade(arquivo_json):
    # Exercício 2: Ler o arquivo JSON que você criou e calcular a média de idade de todos os clientes.
    with open(arquivo_json, 'r') as file:
        client_data = json.load(file)

    if not client_data:
        print("Nenhum cliente encontrado no arquivo.")
        return

    soma_idades = 0
    for cliente in client_data:
        soma_idades += cliente['idade']

    total_clientes = len(client_data)
    media_idade = soma_idades / total_clientes

    print(f"A média de idade dos clientes é: {media_idade:.0f} anos")


def listar_idade(idade):
    # Exercício 5: Fazer uma consulta para retornar todos os clientes com idade superior a um determinado valor.
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes WHERE idade > ?', (idade,))
    idade_maior = cursor.fetchall()
    print(f"\nClientes com idade superior a {idade}:")
    for client in idade_maior:
        print(f"ID: {client[0]}, Nome: {
              client[1]}, E-mail: {client[2]}, Idade: {client[3]}")
    conn.close()


def listar_clientes_e_idades():
    # Exercício 10: Criar uma função que liste todos os clientes e suas respectivas idades.
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome, idade FROM clientes')
    clientes = cursor.fetchall()
    print("\nLista de Clientes e Idades:")
    for client in clientes:
        print(f"Nome: {client[0]}, Idade: {client[1]}")
    conn.close()


# ==================== UPDATE  ==================== #
def novo_email(email, id):
    # Exercício 6: Atualizar o e-mail de um cliente específico na tabela.
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE clientes SET email = ? WHERE id = ?', (email, id))
    conn.commit()
    conn.close()
    print(f"E-mail do cliente com ID {id} atualizado para {email}.")


# ==================== DELETE  ==================== #
def excluir_cliente(nome):
    # Exercício 7: Excluir um cliente específico da tabela com base no nome
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clientes WHERE nome = ?', (nome,))
    conn.commit()
    conn.close()
    print(f"Cliente '{nome}' excluído com sucesso.")
