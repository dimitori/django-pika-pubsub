Django-pika-pubsub
==================

Django-pika-pubsub is a simple Django app to publish and consume rmq-messages via Pika.

Quick start
-----------

1. Add "django_pika_pubsub" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_pika_pubsub',
    ]

2. Add the following to your settings.py module::

	PUBSUB = {
		'RABBITMQ_USERNAME': os.getenv('RABBITMQ_USERNAME'),
		'RABBITMQ_PASSWORD': os.getenv('RABBITMQ_PASSWORD'),
		'RABBITMQ_HOST': os.getenv('RABBITMQ_HOST'),
		'RABBITMQ_PORT': int(os.getenv('RABBITMQ_PORT')),
	}

3. Do following for producing messages::

	from django_pika_pubsub import Producer
	...
	producer = Producer.get_producer()
	producer.produce(
		exchange='orders',
		body={'id': order.id},
		routing_key='order.sent.order_id.1.0.0'
	)

