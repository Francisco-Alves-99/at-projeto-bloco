from database import *
import pandas as pd
def consultar_usuario_db(id_usuario):
    try:
        conn, cursor = get_connection_all()
        cursor.execute("SELECT id_usuario FROM Usuario WHERE id_usuario = ?", (id_usuario,))
        usuario = cursor.fetchone()
        return usuario
    except Exception as ex:
        print(ex)
    finally:        
        disconnect(conn, cursor)

def consultar_emprestimo_db(id_emprestimo):
    try:
        conn, cursor = get_connection_all()
        cursor.execute("SELECT id_emprestimo FROM Usuario WHERE id_usuario = ?", (id_emprestimo,))
        emprestimo = cursor.fetchone()
        return emprestimo
    except Exception as ex:
        print(ex)
    finally:        
        disconnect(conn, cursor)        

def consultar_livro_db(id_livro):
    try:
        conn, cursor = get_connection_all()
        cursor.execute("SELECT exemplares_disponiveis FROM Livro WHERE id_livro = ?", (id_livro,))
        livro = cursor.fetchone()
        return livro
    except Exception as ex:
        print(ex)
    finally:        
        disconnect(conn, cursor)        

def cadastrar_usuario_db(nome, sobrenome, data_nascimento):
    try:
        conn, cursor = get_connection_all()
        cursor.execute("""
                INSERT INTO Usuario (nome, sobrenome, data_nascimento)
                VALUES (?, ?, ?)
            """, (nome, sobrenome, data_nascimento))
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:        
        disconnect(conn, cursor)

def realizar_emprestimo(id_livro, id_usuario, data_emprestimo):
    try:
        conn, cursor = get_connection_all()

        cursor.execute("""
            INSERT INTO Emprestimo (id_usuario, id_livro, data_emprestimo)
            VALUES (?, ?, ?)
        """, (id_usuario, id_livro, data_emprestimo))
        conn.commit()

        cursor.execute("""
            UPDATE Livro
            SET exemplares_disponiveis = exemplares_disponiveis - 1
            WHERE id_livro = ?
        """, (id_livro,))
        conn.commit()

    except Exception as e:
        print(f"Erro ao realizar empréstimo: {e}")
    finally:
        disconnect(conn, cursor)

def realizar_devolucao(data_devolucao, id_emprestimo):
    try:
        conn, cursor = get_connection_all()

        cursor.execute("""
            UPDATE Emprestimo
            SET data_devolucao = ?
            WHERE id_emprestimo = ?
        """, (data_devolucao, id_emprestimo))
        conn.commit()

        cursor.execute("SELECT id_livro FROM Emprestimo WHERE id_emprestimo = ?", (id_emprestimo,))
        id_livro = cursor.fetchone()[0]

        cursor.execute("""
            UPDATE Livro
            SET exemplares_disponiveis = exemplares_disponiveis + 1
            WHERE id_livro = ?
        """, (id_livro,))
        conn.commit()

    except Exception as e:
        print(f"Erro ao realizar devolução: {e}")
    finally:
        disconnect(conn, cursor)

def listar_usuarios_db():
    try:
        conn = get_connection()
        query = "SELECT * FROM Usuario"
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as ex:
        print(ex)
        return pd.DataFrame()
    finally:
        disconnect(conn)

def listar_livros_db():
    try:
        conn = get_connection()
        query = "SELECT id_livro, titulo, exemplares_disponiveis FROM Livro"
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as ex:
        print(ex)
        return pd.DataFrame()
    finally:
        disconnect(conn)

def listar_emprestimos_db():
    try:
        conn = get_connection()
        query = "SELECT * FROM Emprestimo"
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as ex:
        print(ex)
        return pd.DataFrame()
    finally:
        disconnect(conn)

def listar_emprestimos_usuario_db(id_usuario):
    try:
        conn, cursor = get_connection_all()
        query = """
            SELECT * FROM Emprestimo
            WHERE id_usuario = ?
        """
        df = pd.read_sql_query(query, conn, params=(id_usuario,))
        return df
    except Exception as ex:
        print(ex)
        return pd.DataFrame()
    finally:
        disconnect(conn, cursor)

def verificar_livro_para_emprestimo_db(id_livro, id_usuario):
    try:
        conn, cursor = get_connection_all()

        cursor.execute("""
            SELECT COUNT(*) FROM Emprestimo
            WHERE id_usuario = ? AND id_livro = ? AND data_devolucao IS NULL
        """, (id_usuario, id_livro))
        if cursor.fetchone()[0] > 0:
            return "ja_possui_emprestimo"

        cursor.execute("""
            SELECT COUNT(*) FROM Emprestimo
            WHERE id_usuario = ? AND data_devolucao IS NULL
        """, (id_usuario,))
        if cursor.fetchone()[0] >= 5:
            return "limite_emprestimos"

        return "ok"
    except Exception as e:
        print(f"Erro ao verificar empréstimo: {e}")
        return "erro"
    finally:
        disconnect(conn, cursor)

def verificar_devolucao_ja_realizada_db(id_emprestimo):
    try:
        conn, cursor = get_connection_all()

        cursor.execute("""
            SELECT COUNT(*) FROM Emprestimo
            WHERE id_emprestimo = ? AND data_devolucao IS NOT NULL
        """, (id_emprestimo,))
        if cursor.fetchone()[0] > 0:
            return True
        return False
    except Exception as e:
        print(f"Erro ao verificar devolução: {e}")
        return True
    finally:
        disconnect(conn, cursor)


