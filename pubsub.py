import ssl
import pika
from django.conf import settings

pubsub_settings = {
    'user': settings.PUBSUB['RABBITMQ_USERNAME'],
    'password': settings.PUBSUB['RABBITMQ_PASSWORD'],
    'host': settings.PUBSUB['RABBITMQ_HOST'],
    'port': settings.PUBSUB['RABBITMQ_PORT'],
}


def get_parameters(host, port, username, password):
    credentials = pika.PlainCredentials(username, password)
    context = get_context()
    ssl_options = pika.SSLOptions(context)
    parameters = pika.ConnectionParameters(
        host=host,
        port=port,
        credentials=credentials,
        ssl_options=ssl_options,
    )
    return parameters


def get_context():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    return context
