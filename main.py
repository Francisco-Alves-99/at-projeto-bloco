from menu import *
from crud import *
from listagem import *

if __name__ == "__main__":
    def menu():
        while True:
            escolha = exibir_menu()

            match escolha:
                case 1:
                    cadastrar_usuario()
                case 2:
                    adquirir_livro()
                case 3:
                    devolver_livro()
                case 4:
                    exibir_usuarios_listagem()
                case 5:
                    exibir_livros_listagem()
                case 6:
                    exibir_emprestimos_listagem()
                case 7:
                    exibir_emprestimos_usuario()    
                case 8:
                    print("Encerrando...")
                    break
                case _:
                    print("Opção inválida.")
    menu()
