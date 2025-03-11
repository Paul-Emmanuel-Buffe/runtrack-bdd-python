import mysql.connector

class Employe:
    def __init__(self, config):
        self.connection =  mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()


    def create(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s,%s,%s,%s)"
        self.cursor.execute(query, (nom, prenom, salaire, id_service))
        self.connection.commit()
    
    def read(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(row)

    def update(self, id,id_service):
        query = "UPDATE employe SET id_service= %s WHERE id= %s"
        self.cursor.execute(query,(id,id_service))
        self.connection.commit()
    
    def delete(self, id):
        query = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(query,(id,))
        self.connection.commit()
    
    def close(self):
        self.cursor.close()
        self.connection.close()
        print('Connexion fermée')



config = {
    "user" : "root",
    "password" : "cN06+#P34",
    "host" : "localhost",
    "database" : "effectif",
    "port" : 3306
}
emp = Employe(config)

#emp.create('Buffe', 'Paul', 566.00, 9)

#emp.read()

#emp.update(5,10)

emp.delete(20)

emp.close()









