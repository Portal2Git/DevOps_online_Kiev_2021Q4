# DevOps_online_Kiev_2021Q4

TASK 4.1

PART 1. 

CREATE DATABASE TestDB;
USE TestDB;

CREATE TABLE Sex (
    SexID smallint NOT NULL AUTO_INCREMENT,
    Value varchar(16),
    PRIMARY KEY (SexID)
);

CREATE TABLE Persons (
    PersonID int NOT NULL AUTO_INCREMENT,
    LastName varchar(64),
    FirstName varchar(64),
    SexID smallint,
    PRIMARY KEY (PersonID),
    FOREIGN KEY (SexID) REFERENCES Sex(SexID)
);

CREATE TABLE Orders (
    OrderID int NOT NULL AUTO_INCREMENT,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);

INSERT INTO Sex (Value) VALUES('male');
INSERT INTO Sex (Value) VALUES('female');

INSERT INTO Persons (LastName , FirstName, SexID) VALUES('Ivanov', 'Ivan', 1);
INSERT INTO Persons (LastName , FirstName, SexID) VALUES('Stepanenko', 'Stepan', 1);
INSERT INTO Persons (LastName , FirstName, SexID) VALUES('Ivanova', 'Svetlana', 2);
INSERT INTO Persons (LastName , FirstName, SexID) VALUES('Danilov', 'Danil', 1);
INSERT INTO Persons (LastName , FirstName, SexID) VALUES('Baev', 'Marat', 1);
INSERT INTO Persons (LastName , FirstName, SexID) VALUES('Strelec', 'Maria', 2);
INSERT INTO Persons (LastName , FirstName, SexID) VALUES('Danilova', 'Maria', 2);

INSERT INTO Orders (OrderNumber , PersonID) VALUES(11234, 1);
INSERT INTO Orders (OrderNumber , PersonID) VALUES(11237, 1);
INSERT INTO Orders (OrderNumber , PersonID) VALUES(12456, 2);
INSERT INTO Orders (OrderNumber , PersonID) VALUES(12378, 3);
INSERT INTO Orders (OrderNumber , PersonID) VALUES(13835, 4);
INSERT INTO Orders (OrderNumber , PersonID) VALUES(14987, 3);
INSERT INTO Orders (OrderNumber , PersonID) VALUES(14989, 5);
INSERT INTO Orders (OrderNumber , PersonID) VALUES(15342, 6);
INSERT INTO Orders (OrderNumber , PersonID) VALUES(16786, 7);

CREATE USER 'admin'@'localhost' IDENTIFIED BY '12344321';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';

CREATE USER 'user1'@'localhost' IDENTIFIED BY '11111111';
GRANT CREATE, DROP, BACKUP ON *.* TO 'user1'@'localhost';

CREATE USER 'user2'@'localhost' IDENTIFIED BY '22222222';
GRANT SELECT, INSERT, UPDATE ON testdb.* TO 'user2'@'localhost';

SELECT * FROM Orders
JOIN Persons ON Orders.PersonID=Persons.PersonID
JOIN Sex ON Persons.SexID=Sex.SexID
WHERE Persons.LastName = 'Ivanov' OR Persons.LastName = 'Ivanova'
ORDER BY OrderNumber;

PART 2. 

sudo mysqldump -u root -p TestDB > testdb.sql

sudo mysql -u root -p TestDB < testdb.sql

mysql -u admin -h database-3.cjomhobfbpeg.us-east-2.rds.amazonaws.com -p12345678

mysql -u admin -h database-3.cjomhobfbpeg.us-east-2.rds.amazonaws.com -p12345678 testdb < /home/m/testdb.sql 

PART 3. 

![alt text](img/3_1-4.png "Install")
