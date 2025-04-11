from util import *

def exibir_menu() -> int:
    while True:
        print("\n" + "-" * 30)
        print("MENU DA BIBLIOTECA")
        print("1. Cadastrar usuário")
        print("2. Adquirir livro")
        print("3. Devolver livro")
        print("4. Listar usuários")
        print("5. Listar livros")
        print("6. Listar empréstimos")
        print("7. Listar empréstimos do usuário")
        print("8. Sair")
        print("-" * 30)

        escolha = input_numero("Escolha uma opção: ")
        return escolha
