import mysql.connector

config = {
    "user" : "root",
    "password" : "777777",
    "host" : "localhost",
    "database" : "laplateforme",
    "port" : 3306
}

liste = []

connection = mysql.connector.connect(**config)
print("connexion OK !!")

cursor = connection.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

for i in cursor:
    liste.append(i)

print(liste)


