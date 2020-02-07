import pika
import json
from .pubsub import get_parameters, pubsub_settings


class Producer:
    def __init__(self, host, username, password, port=5671):
        self.parameters = get_parameters(host, port, username, password)
        self.exchanges = []

    def produce(self, exchange, body, routing_key=''):
        connection = pika.BlockingConnection(self.parameters)
        channel = connection.channel()
        if exchange not in self.exchanges:
            channel.exchange_declare(exchange=exchange, exchange_type='direct')
            self.exchanges.append(exchange)

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
