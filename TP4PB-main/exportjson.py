import sqlite3
import json
import os


def exportar_dados_json(arquivo_json):
    # Exercício 9: Crie uma função em Python que exporte dados da tabela produtos para um arquivo JSON.
    if not arquivo_json.endswith('.json'):
        arquivo_json += '.json'

    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()

    lista_clientes = []
    for client in clientes:
        cliente_dict = {
            'id': client[0],
            'nome': client[1],
            'email': client[2],
            'idade': client[3]
        }
        lista_clientes.append(cliente_dict)

    with open(arquivo_json, 'w') as file:
        json.dump(lista_clientes, file, indent=4)

    conn.close()
    print(f"Dados exportados para o arquivo '{arquivo_json}'.")
