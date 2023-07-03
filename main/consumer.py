import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()
import pika, json
from products.models import Product

params = pika.URLParameters('amqps://rlfcgigm:snIyM-j0ycanTqVvNYhQfNPN2mZ9CK9G@jackal.rmq.cloudamqp.com/rlfcgigm')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')#implementa el protocolo de mensajeria AMQP para declarar una cola.
#una cola es un destino donde los productores envian mensajes y los consumidores reciben. este protocolo crea una cola.

def callback(ch, method,properties, body):
    
    print('resibido en main')
    data = json.loads(body)
    print(data)
    

    if properties.content_type == 'producto_creado':
        print(data)
        product, created = Product.objects.get_or_create(id=data['id'], defaults={'title': data['title'], 'image': data['image']})
        print('producto creado =>', created)


        
    elif properties.content_type == 'producto':
        print('lista')
        
    elif properties.content_type == 'producto_editado':
        product = Product.objects.get(id=data['id'])
        product.title = data['title']
        product.image = data['image']
        product.save()
        print('Producto actualizado =>', product)

    
    elif properties.content_type == 'producto_eliminado':
        product = Product.objects.get(id=data)
        product.delete()
        print('producto eliminado=')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('consumiendo')


channel.start_consuming()

channel.close()