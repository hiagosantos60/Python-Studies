import psycopg2
import PySimpleGUI as sg

#Função para conectar ao banco de dados 
def conectar():
    try:
        conn = psycopg2.connect(
            dbname="cadastro",
            user="hiago", #usuário 
            password="hiago123", #senha
            host="localhost",  
            port="5432" #porta do DB postgree
        )
        return conn
    except Exception as erro:
        sg.popup_error(f"Erro ao conectar ao banco de dados: {erro}")
        return None

def add_produto(conn, nome_do_produto, codigo, data_saida, descricao):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO cadastro (nome_do_produto, codigo, data, descricao) VALUES (%s, %s, %s, %s)",
                (nome_do_produto, codigo, data_saida, descricao)
            )
            conn.commit()
            sg.popup("Produto adicionado!")
    except Exception as erro:
        sg.popup_error(f"Erro ao adicionar o produto: {erro}")

def remove_produto(conn, codigo):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM cadastro WHERE codigo = %s",
                (codigo,)
            )
            if cursor.rowcount > 0:
                conn.commit()
                sg.popup("Produto removido!")
            else:
                sg.popup("Nenhum produto encontrado com esse código.")
    except Exception as erro:
        sg.popup_error(f"Erro ao remover o produto: {erro}")

def encerra_conexao(conn):
    if conn:
        conn.close()
