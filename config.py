import mysql
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)
cursor = conexao.cursor()

# Criação do banco de dados
cursor.execute("CREATE DATABASE desafiopubfuture")

# Criação de tabelas
cursor.execute("CREATE TABLE receitas(id INT AUTO INCREMENT PRIMARY KEY,valor_receita FLOAT(9),data_recebimento DATE,data_receb_esperado DATE,tipo_receita VARCHAR(255),descricao VARCHAR(255),conta INT)")
cursor.execute("CREATE TABLE despesas(id INT AUTO INCREMENT PRIMARY KEY,valor_despesa FLOAT(9),data_recebimento DATE,data_receb_esperado DATE,tipo_despesa VARCHAR(255),conta INT)")
cursor.execute("CREATE TABLE contas(id INT AUTO INCREMENT PRIMARY KEY,conta VARCHAR(255), instituicao_financeira VARCHAR(255),saldo FLOAT(9),tipo_conta VARCHAR(255))")
