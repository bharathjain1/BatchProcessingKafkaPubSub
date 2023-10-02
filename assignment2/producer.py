from confluent_kafka import Producer
import json
import time



with open('movie_1990s.json') as file:
    data = json.load(file)

# Kafka broker(s) configuration
kafka_broker = 'localhost:9092'

# Create a Kafka producer instance
producer = Producer({'bootstrap.servers': kafka_broker})

# Define the topic to which you want to publish messages
topic = 'TestTopic'

# Publish a message to the topic
for i in data:
    producer.produce(topic, key='key', value=json.dumps(i))

# Flush the producer to ensure the message is sent
producer.flush()

