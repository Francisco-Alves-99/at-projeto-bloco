from datetime import date
from crud_db import *
from listagem import *
from validacao import *
from util import *

def cadastrar_usuario():
        nome = input("Digite o seu nome: ")
        sobrenome = input("Digite o seu sobrenome: ")
        data_nascimento = input("Digite a sua data de nascimento (DD/MM/AAAA): ")

        cadastrar_usuario_db(nome, sobrenome, data_nascimento)
        print("Usuário cadastrado com sucesso!")

def adquirir_livro():
        exibir_livros_listagem()
        id_livro = input_numero("Digite o ID do livro desejado: ")
        livro = consultar_livro_db(id_livro)
        if not livro:
              print("Erro: Livro não existe!")
              return
        if livro[0] < 1:
            print("Erro: Sem exemplares disponíveis.")
            return
        
        id_usuario = input_numero("Digite o seu ID de usuário: ")
        usuario = consultar_usuario_db(id_usuario)
        if not usuario:
             print ("Erro: Usuário não existe!")
             return

        if verifica_emprestimo_viavel(id_livro, id_usuario):
            data_emprestimo = date.today().isoformat()
            
            realizar_emprestimo(id_livro, id_usuario, data_emprestimo)
            print("Empréstimo realizado com sucesso.")

def devolver_livro():

        id_usuario = input_numero("Digite o seu ID de usuário: ")
        usuario = consultar_usuario_db(id_usuario)
        if not usuario:
             print ("Erro: Usuário não existe!")
             return
        
        exibir_emprestimos_usuario_listagem(id_usuario)

        id_emprestimo = input_numero("Digite o ID do empréstimo a devolver: ")
        emprestimo = consultar_emprestimo_db(id_emprestimo)
        if not emprestimo:
             print ("Erro: Empréstimo não existe!")
             return
        
        if valida_devolucao(id_emprestimo):
            data_devolucao = date.today().isoformat()
        
            realizar_devolucao(data_devolucao, id_emprestimo)

            print("Livro devolvido com sucesso.")

def exibir_emprestimos_usuario():
    id_usuario = input_numero("Digite o seu ID de usuário: ")
    usuario = consultar_usuario_db(id_usuario)
    if not usuario:
            print ("Erro: Usuário nao existe!")
            return
    return exibir_emprestimos_usuario_listagem(id_usuario)               
