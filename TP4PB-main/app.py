from crud import *
from importjson import *
from importjson import *
from exportjson import *


def menu():
    while True:
        print("\nMenu:")
        print("1. Criar Tabela")
        print("2. Listar Clientes com Idade Superior a um Valor")
        print("3. Listar Todos os Clientes e Suas Idades")
        print("4. Calcular a média de idade de todos os clientes")
        print("5. Atualizar E-mail de um Cliente")
        print("6. Excluir um Cliente pelo Nome")
        print("7. Importar Dados de um Arquivo JSON para a tabela")
        print("8. Exportar Dados para um Arquivo JSON")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_tabela()
        elif escolha == '2':
            idade = int(input("Digite a idade: "))
            listar_idade(idade)
        elif escolha == '3':
            listar_clientes_e_idades()
        elif escolha == '4':
            arquivo_json = input(
                "Digite o nome do arquivo JSON para calcular a média de idade: ")
            calcular_media_idade(arquivo_json)
        elif escolha == '5':
            id = int(input("Digite o ID do cliente: "))
            email = input("Digite o novo e-mail: ")
            novo_email(email, id)
        elif escolha == '6':
            nome = input("Digite o nome do cliente a ser excluído: ")
            excluir_cliente(nome)
        elif escolha == '7':
            arquivo_json = input(
                "Digite o nome do arquivo JSON para importar: ")
            importar_dados_json(arquivo_json)
        elif escolha == '8':
            arquivo_json = input(
                "Digite o nome do arquivo JSON para exportar: ")
            exportar_dados_json(arquivo_json)
        elif escolha == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
