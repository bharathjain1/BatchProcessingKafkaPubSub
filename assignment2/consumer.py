from confluent_kafka import Consumer, KafkaError
import json
from connection import AllConn
 
# Kafka broker(s) configuration
kafka_broker = 'localhost:9092'

# Create a Kafka consumer instance
consumer = Consumer({
    'bootstrap.servers': kafka_broker,
    'group.id': 'my-consumer-group'
})

# Subscribe to the topic
topic = 'TestTopic'
consumer.subscribe([topic])

#Stores the consumed message into postresql
def store_messages_postgres(data):
    postgres_conn = AllConn().postgresconnection()
    postgres_cursor = postgres_conn.cursor()
    json_string = data.decode('utf-8')
    json_data = json.loads(json_string)
    title = json_data['title'] if json_data['title'] else None
    cast = json_data['cast'][0] if len(json_data['cast']) > 0  else None
    genres = json_data['genres'][0] if len(json_data['genres']) > 0 else None
    insert_query = '''INSERT INTO movies_1900(movie_name,movie_cast,movie_genre)
                                                                    VALUES (%s,%s,%s);'''
    data_to_insert = (title,cast,genres)
    postgres_cursor.execute(insert_query, data_to_insert)
    print("data inserted in row succesfully !!")
    postgres_conn.commit()
    postgres_conn.close()
   
while True:
    msg = consumer.poll(1.0)  # Poll for messages
    if msg is not None:
        data = msg.value()
        store_messages_postgres(data)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print(f'Reached end of partition for topic {msg.topic()}')
        else:
            print(f'Error while consuming message: {msg.error()}')
    else:
        print(f'Received message: {msg.value()}')


