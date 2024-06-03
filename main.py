# Importa as funções criadas anteriormente
from view import *
import datetime

# Define a função para exibir o menu e receber a entrada do usuário
def mostrar_menu():
    print("\nSelecione uma opção:")
    print("1. Inserir um novo livro")
    print("2. Inserir um novo usuário")
    print("3. Realizar um empréstimo")
    print("4. Atualizar a data de devolução de um empréstimo")
    print("5. Exibir todos os livros CADASTRADOS no sistema")    
    print("6. Exibir todos os livros DISPONIVEIS no sistema")
    print("7. Exibir todos os livros EMPRESTADOS no momento")
    print("8. Exibir usuários cadastrados no sistema")
    print("0. Sair")

    choice = input("\nDigite o número da opção desejada: ")
    return choice

# Loop principal do programa
while True:
    choice = mostrar_menu()

    if choice == "1":
        titulo = input("\nDigite o título do livro: ")
        autor = input("Digite o nome do autor do livro: ")
        editora = input("Digite o nome da editora do livro: ")
        ano_publicacao = input("Digite o ano de publicação do livro: ")
        isbn = input("Digite o ISBN do livro: ")

        cadastrar_livro(titulo, autor, editora, ano_publicacao, isbn)
        print("\nLivro inserido com sucesso!")

    elif choice == "2":
        nome = input("\nDigite o primeiro nome do usuário: ")
        sobrenome = input("Digite o sobrenome do usuário: ")
        endereco = input("Digite o endereço do usuário: ")
        email = input("Digite o endereço de e-mail do usuário: ")
        telefone = input("Digite o número de telefone do usuário: ")

        cadastrar_usuario(nome, sobrenome, endereco, email, telefone)
        print("\nUsuário inserido com sucesso!")

    elif choice == "3":
        id_usuario = input("\nDigite o ID do usuário: ")
        id_livro = input("Digite o ID do livro: ")
        data_emprestimo = datetime.datetime.now()

        cadastrar_emprestimo(id_usuario, id_livro, data_emprestimo, None)

    elif choice == "4":
        id_emprestimo = input("Digite o ID do empréstimo: ")
        data_devolucao = input("Digite a data de devolução (formato: DD/MM/AAAA): ")

        devolver_emprestimo(id_emprestimo, data_devolucao)
        print("\nData de devolução atualizada com sucesso!")

    elif choice == "5":
        exibir_livros()

    elif choice == "6":
        exibir_disponiveis()

    elif choice == "7":
        exibir_emprestimos()

    elif choice == "8":
        exibir_usuarios()

    elif choice == "0":
        break
    else:
        print("\nOpção inválida. Por favor, selecione uma opção válida.")