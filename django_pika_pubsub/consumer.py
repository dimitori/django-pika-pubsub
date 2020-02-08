import pika
from .pubsub import get_parameters, pubsub_settings


class Consumer:
    def __init__(self, host, username, password, port=5672):
        self.parameters = get_parameters(host, port, username, password)
        self.connection = None

    def consume(self, routing_key, callback):
        queue_name = routing_key
        if not self.connection:
            self._init_connection()
        self._init_channel()
        self._init_queue(queue_name)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
        )
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def _init_connection(self):
        self.connection = pika.BlockingConnection(self.parameters)

    def _init_channel(self):
        self.channel = self.connection.channel()

    def _init_queue(self, queue_name):
        """declare a queue"""
        self.channel.queue_declare(queue=queue_name, durable=True)

    @classmethod
    def get_consumer(cls):
        return cls(**pubsub_settings)
