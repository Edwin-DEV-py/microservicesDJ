import pika

params = pika.URLParameters('amqps://rlfcgigm:snIyM-j0ycanTqVvNYhQfNPN2mZ9CK9G@jackal.rmq.cloudamqp.com/rlfcgigm')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='',routing_key='main',body='hello main')