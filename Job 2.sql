CREATE TABLE etage (
id INT PRIMARY KEY AUTO_INCREMENT,
nom VARCHAR(255) NOT NULL,
numero INT NOT NULL,
superficie INT);

mysql> CREATE TABLE salle(
    -> id INT PRIMARY KEY AUTO_INCREMENT,
    -> nom VARCHAR(255) NOT NULL,
    -> id_etage  INT NOT NULL,
    -> capacite INT NOT NULL);