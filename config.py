import mysql
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

cursor = conexao.cursor()
