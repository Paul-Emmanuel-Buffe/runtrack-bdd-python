import mysql.connector

config = {
    "user" : "root",
    "password" : "cN06+#P34",
    "host" : "localhost",
    "database" : "laplateforme",
    "port" : 3306
}


connection = mysql.connector.connect(**config)
print("connexion OK !!")

cursor = connection.cursor()

cursor.execute("SELECT * FROM etudiant")

for i in cursor:
    print(i)


