import mysql.connector

config = {
    "user" : "root",
    "password" : "cN06+#P34",
    "host" : "localhost",
    "database" : "laplateforme",
    "port" : 3306
}

liste = []

connection = mysql.connector.connect(**config)
print("connexion OK !!")

cursor = connection.cursor()

query = "SELECT SUM(superficie) FROM etage"
cursor.execute(query)

total = cursor.fetchone()[0]

print(f'La surface totale de la plateforme est de {total} m2')

cursor.close()
connection.close()


