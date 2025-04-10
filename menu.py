from models import cadastrar_usuario, adquirir_livro, devolver_livro

def exibir_menu():
    while True:
        print("\n" + "-" * 30)
        print("MENU DA BIBLIOTECA")
        print("1. Cadastrar usuário")
        print("2. Adquirir livro")
        print("3. Devolver livro")
        print("4. Sair")
        print("-" * 30)

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        match escolha:
            case 1:
                cadastrar_usuario()
            case 2:
                adquirir_livro()
            case 3:
                devolver_livro()
            case 4:
                print("Encerrando...")
                break
            case _:
                print("Opção inválida.")
