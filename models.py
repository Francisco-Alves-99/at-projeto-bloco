from datetime import date
from database import get_connection
import pandas as pd

def cadastrar_usuario():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        nome = input("Digite o seu nome: ")
        sobrenome = input("Digite o seu sobrenome: ")
        data_nascimento = input("Digite a sua data de nascimento (DD/MM/AAAA): ")

        cursor.execute("""
            INSERT INTO Usuario (nome, sobrenome, data_nascimento)
            VALUES (?, ?, ?)
        """, (nome, sobrenome, data_nascimento))
        conn.commit()
        print("Usuário cadastrado com sucesso!")

    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        conn.close()

def adquirir_livro():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
            SELECT id_livro, titulo, exemplares_disponiveis FROM Livro
        """
        df_livro = pd.read_sql_query(query, conn)
        print(df_livro)
        print("-" * 20)

        id_livro = input("Digite o ID do livro desejado: ")

        cursor.execute("SELECT exemplares_disponiveis FROM Livro WHERE id_livro = ?", (id_livro,))
        livro = cursor.fetchone()

        if not livro:
            print("Livro não encontrado.")
            return

        if livro[0] < 1:
            print("Sem exemplares disponíveis.")
            return

        id_usuario = input("Digite o seu ID de usuário: ")

        cursor.execute("""
            SELECT COUNT(*) FROM Emprestimo
            WHERE id_usuario = ? AND id_livro = ? AND data_devolucao IS NULL
        """, (id_usuario, id_livro))
        if cursor.fetchone()[0] > 0:
            print("Você já possui este livro emprestado.")
            return

        cursor.execute("""
            SELECT COUNT(*) FROM Emprestimo
            WHERE id_usuario = ? AND data_devolucao IS NULL
        """, (id_usuario,))
        if cursor.fetchone()[0] >= 5:
            print("Limite de 5 empréstimos ativos atingido.")
            return

        data_emprestimo = date.today().isoformat()
        cursor.execute("""
            INSERT INTO Emprestimo (id_usuario, id_livro, data_emprestimo)
            VALUES (?, ?, ?)
        """, (id_usuario, id_livro, data_emprestimo))
        cursor.execute("""
            UPDATE Livro
            SET exemplares_disponiveis = exemplares_disponiveis - 1
            WHERE id_livro = ?
        """, (id_livro,))
        conn.commit()
        print("Empréstimo realizado com sucesso.")

    except Exception as e:
        print(f"Erro ao adquirir livro: {e}")
    finally:
        conn.close()

def devolver_livro():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        id_usuario = input("Digite o seu ID de usuário: ")
        
        query = """
            SELECT * FROM Emprestimo
            WHERE id_usuario = ?
        """
        df_emprestimo = pd.read_sql_query(query, conn, params=(id_usuario,))
        print(df_emprestimo)
        print("-" * 20)

        id_emprestimo = input("Digite o ID do empréstimo a devolver: ")

        cursor.execute("""
            SELECT COUNT(*) FROM Emprestimo
            WHERE id_emprestimo = ? AND data_devolucao IS NOT NULL
        """, (id_emprestimo,))
        if cursor.fetchone()[0] > 0:
            print("Este livro já foi devolvido.")
            return

        data_devolucao = date.today().isoformat()
        cursor.execute("""
            UPDATE Emprestimo
            SET data_devolucao = ?
            WHERE id_emprestimo = ?
        """, (data_devolucao, id_emprestimo))

        cursor.execute("SELECT id_livro FROM Emprestimo WHERE id_emprestimo = ?", (id_emprestimo,))
        id_livro = cursor.fetchone()[0]

        cursor.execute("""
            UPDATE Livro
            SET exemplares_disponiveis = exemplares_disponiveis + 1
            WHERE id_livro = ?
        """, (id_livro,))

        conn.commit()
        print("Livro devolvido com sucesso.")

    except Exception as e:
        print(f"Erro ao devolver livro: {e}")
    finally:
        conn.close()
