import pika
import json
from .pubsub import get_parameters, pubsub_settings


class Producer:
    def __init__(self, host, username, password, port=5671):
        self.parameters = get_parameters(host, port, username, password)
        self.exchanges = []

    def produce(self, body, routing_key):
        exchange = ''
        queue = routing_key
        connection = pika.BlockingConnection(self.parameters)
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )
        connection.close()

    @classmethod
    def get_producer(cls):
        return cls(**pubsub_settings)
