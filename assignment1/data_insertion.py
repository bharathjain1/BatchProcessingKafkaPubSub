import json
from connection import AllConn

def insertJsonInMongoDb():
    with open('movies-2020s.json') as file:
        data = json.load(file)
    mongo_conn  = AllConn().mongoconnection()
    print("Data insertion started")
    data_transfer = mongo_conn.movies_of_2020.insert_many(data)
    print("Data inserted in mongodb successfully !")
