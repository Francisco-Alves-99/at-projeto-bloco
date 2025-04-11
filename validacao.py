from crud_db import *

def verifica_emprestimo_viavel(id_livro, id_usuario):
    resultado = verificar_livro_para_emprestimo_db(id_livro, id_usuario)

    match resultado:
        case "ja_possui_emprestimo":
            print("Você já possui este livro emprestado.")
            return False
        case "limite_emprestimos":
            print("Limite de 5 empréstimos ativos atingido.")
            return False
        case "erro":
            print("Erro ao verificar empréstimo.")
            return False
        case "ok":
            return True

def valida_devolucao(id_emprestimo):
    if verificar_devolucao_ja_realizada_db(id_emprestimo):
        print("Este livro já foi devolvido.")
        return False
    return True
