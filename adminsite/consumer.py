import pika

params = pika.URLParameters('amqps://rlfcgigm:snIyM-j0ycanTqVvNYhQfNPN2mZ9CK9G@jackal.rmq.cloudamqp.com/rlfcgigm')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')#implementa el protocolo de mensajeria AMQP para declarar una cola.
#una cola es un destino donde los productores envian mensajes y los consumidores reciben. este protocolo crea una cola.

def callback(ch, method, properties, body):
    print('resibido en admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True) #consumimos las llamada sy nos las volvemos a recibir

print('consumiendo')

channel.start_consuming()

channel.close()