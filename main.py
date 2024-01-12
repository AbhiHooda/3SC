import json

from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
import mysql.connector

app = FastAPI()

class Transaction(BaseModel):
    userName: str
    merchantName: str
    amount: str
    currency: str
    productId: str
    quantity: str


@app.post("/create")
async def create(transaction: Transaction):
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='trial')
    cursor = cnx.cursor()
    print ('here')
    transactionId = str(uuid.uuid4())
    current_time = datetime.datetime.now()
    sql = f'INSERT INTO transaction (ID, userName, merchantName, Amount, Currency, Quantity, ProductID, date) VALUES ("{str(transactionId)}", "{str(transaction.userName)}", "{str(transaction.merchantName)}", {int(transaction.amount)}," {str(transaction.currency)}",{int(transaction.quantity)},"{str(transaction.productId)}"," {str(current_time)}")'

    vals = (str(transactionId), str(transaction.userName), str(transaction.merchantName), int(transaction.amount),str(transaction.currency),
            str(transaction.productId),int(transaction.quantity),str(current_time))
    print(vals)
    cursor.execute(sql)
    cnx.commit()
    return 'success'

@app.get("/search")
async def getTransaction(tid: str):
    myquery = {"_id": tid}
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='trial')
    cursor = cnx.cursor()
    cursor.execute(f'SELECT * FROM transaction where ID = "{str(tid)}"')
    result = []
    for res in cursor.fetchall():
        result.append(tuple(res))
    return result

@app.get("/fetchAllsearch")
async def getTransaction():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='trial')
    cursor = cnx.cursor()
    cursor.execute(f'SELECT * FROM transaction ORDER BY date DESC')
    result = []
    for res in cursor.fetchall():
        result.append(tuple(res))
    return result

