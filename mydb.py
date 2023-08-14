import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Am150296%'

	)

# Preparando e criando um objeto de cursor
cursorObject = dataBase.cursor()

# Criando o banco de dados
cursorObject.execute("CREATE DATABASE rdcod")

print("All done!")
