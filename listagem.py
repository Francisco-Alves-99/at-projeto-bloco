from database import *

from crud_db import *

def exibir_usuarios_listagem():
    df = listar_usuarios_db()
    print(df)
    print("-" * 20)

def exibir_livros_listagem():
    df = listar_livros_db()
    print(df)
    print("-" * 20)

def exibir_emprestimos_listagem():
    df = listar_emprestimos_db()
    print(df)
    print("-" * 20)
  

def exibir_emprestimos_usuario_listagem(id_usuario):
    df = listar_emprestimos_usuario_db(id_usuario)
    print(df)
    print("-" * 20)    