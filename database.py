import sqlite3

def get_connection_all():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None, None
    
def get_connection():
    try:
        conn = sqlite3.connect('biblioteca.db')
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None   

def disconnect(conn, cursor=None):
    try:
        if cursor:
            cursor.close()
    except sqlite3.Error as e:
        print(f"Erro ao fechar o cursor: {e}")
    
    try:
        if conn:
            conn.close()
    except sqlite3.Error as e:
        print(f"Erro ao fechar a conexão: {e}")
