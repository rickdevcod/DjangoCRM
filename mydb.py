import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '3306' # A SENHA DO BANCO DE DADOS, DEVE SER A SUA UTILIZEI O MYSQL

	)

# Preparando e criando um objeto de cursor
cursorObject = dataBase.cursor()

# Criando o banco de dados
cursorObject.execute("CREATE DATABASE rdcod")

print("All done!")
