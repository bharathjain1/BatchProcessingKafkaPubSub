from connection import AllConn
from data_insertion import insertJsonInMongoDb

class BatchProcessing(object):
        def __init__(self) -> None:
            self.mongo_conn = AllConn().mongoconnection()
            self.postgres_conn = AllConn().postgresconnection()
            self.postgres_cursor = self.postgres_conn.cursor()
        
        def read_mongodb_json(self):
            for docs in self.mongo_conn.movies_of_2020.find():
                movie_name = docs['title']
                movie_cast = docs['cast']
                movie_genres = docs['genres']
                insert_query = '''INSERT INTO movies_2020(movie_name,movie_cast,movie_genre)
                                                                    VALUES (%s,%s,%s);'''
                data_to_insert = (movie_name,movie_cast[0],movie_genres[0])
                self.postgres_cursor.execute(insert_query, data_to_insert)
                print("data inserted in row succesfully !!")
                self.postgres_conn.commit()
            self.postgres_conn.close()

        
if __name__ == "__main__":
    insertJsonInMongoDb()
    bp = BatchProcessing()
    bp.read_mongodb_json()

