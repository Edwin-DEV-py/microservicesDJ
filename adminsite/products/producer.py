import pika, json

params = pika.URLParameters('amqps://rlfcgigm:snIyM-j0ycanTqVvNYhQfNPN2mZ9CK9G@jackal.rmq.cloudamqp.com/rlfcgigm')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method,body):
    properties = pika.BasicProperties(method,delivery_mode=2)#anadir el delivery_mode=2 para que sea persistente
    channel.basic_publish(exchange='',routing_key='vista2',body=json.dumps(body), properties=properties)