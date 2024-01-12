UI : Python
BackEnd : fastAPI(python)
dataBase : MySql

to start Backend : uvicorn main:app --host 0.0.0.0 --port 8080
to start UI : python ui.py

To create dataBase : create dataBase trial
to create table : 

CREATE TABLE transaction (ID varchar(255) NOT NULL, userName varchar(255) NOT NULL, merchantName varchar(255) NOT NULL, Amount int NOT NULL, Currency varchar(255) NOT NULL, Quantity int NOT NULL, ProductID varchar(255) NOT NULL, date  varchar(255) NOT NULL, PRIMARY KEY (ID));
