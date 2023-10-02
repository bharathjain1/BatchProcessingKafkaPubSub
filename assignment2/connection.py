from pymongo import MongoClient
import psycopg2

class AllConn(object):
    
    def __init__(self):
        # MongoDB connection settings
        self.mongo_host = "localhost"
        self.mongo_port = 27017
        self.mongo_uname = 'root'
        self.mongo_pass = 'root'
        self.mongo_db = "Movies"

        # PostgreSQL connection settings
        self.pg_host = "localhost"
        self.pg_db = "Movies"
        self.pg_user = "root"
        self.pg_password = "root"
        self.pg_port = 5432
    
    def mongoconnection(self):
        client = MongoClient(host=self.mongo_host, 
                             port=self.mongo_port, 
                             username=self.mongo_uname, 
                             password=self.mongo_pass)
        self.conn = client[self.mongo_db]
        return self.conn

    def postgresconnection(self):
        # Connect to PostgreSQL
        pg_connection = psycopg2.connect(
            host=self.pg_host,
            port=self.pg_port,
            database=self.pg_db,
            user=self.pg_user,
            password=self.pg_password
        )
        return pg_connection
