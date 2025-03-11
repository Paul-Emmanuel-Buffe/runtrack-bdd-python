import mysql.connector

config = {
    "user" : "root",
    "password" : "cNççç34",
    "host" : "localhost",
    "database" : "laplateforme",
    "port" : 3306
}

liste = []

connection = mysql.connector.connect(**config)
print("connexion OK !!")

cursor = connection.cursor()

query = "SELECT SUM(capacite) FROM salle"
cursor.execute(query)

total = cursor.fetchone()[0]

print(f'La capacité de toutes les salles est de {total} m2')

cursor.close()
connection.close()


