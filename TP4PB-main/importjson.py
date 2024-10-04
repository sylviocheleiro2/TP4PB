import sqlite3
import json


def importar_dados_json(arquivo_json):
    # Exercício 4: Inserir os dados do arquivo JSON na tabela clientes.
    # Exercício 8: Criar uma função em Python que importe dados de um arquivo JSON para a tabela clientes.

    with open(arquivo_json, 'r') as f:
        client_data = json.load(f)

    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    for client in client_data:
        cursor.execute('INSERT INTO clientes (nome, email, idade) VALUES (?, ?, ?)',
                       (client['nome'], client['email'], client['idade']))

    conn.commit()
    conn.close()
    print("Dados importados do arquivo JSON.")
