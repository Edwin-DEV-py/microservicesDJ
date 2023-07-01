--Dockerfile:
FROM python:3.11 --> que tipo de proyecto es.
ENV PYTHONUNBUFFERED 1 -->garantiza que los flujos stdout y stderr se envien a la terminal sin almacenar primero en el bufer, asi obtenemos todos los registros.
WORKDIR /app --> especificamos un directorio de trabajo.
COPY requirements.txt /app/requirements.txt --> copiar los requirements del workdir.
RUN pip install -r requirements.txt --> comando para instalar los paquetes.
COPY . /app --> copiar todos los archivos del directorio.
CMD python manage.py runserver 0.0.0.0:8000 --> comando para correr la app.

--Docker-compose:
version: '3.8' --> version de docker.
services: -->especificamos los servicios que vamos a usar.
  backend: -->en este caso sera un servicio backend.
    build:
      context: . -->usa una imagen a partir de los archivos del directorio.
      dockerfile: Dockerfile --> usa el dockerfile especificado.
    ports:
      - 8000:8000 -->vincula el contenedor y la maquina host al puerto expuesto.
    volumes:
      - .:/app --> aqui decimos que todos loa archivos estan conectados al contenedor.
    depends_on:
      - db -->DB a utilizar.
  
  db: -->servicio de DB.
    image: mysql:8.0.33 -->imagen de sql.
    restart: always -->para evitar que la app se trave al ejecutarse se reinciia la DB.
    environment: --> variables de entorno, en este caso especificamos la DB y el usuario.
      MYSQL_DATABASE: admin
      MYSQL_USER: root
      MYSQL_PASSWORD: root
      MYSQL_ROOT_PASSWORD: root
    volumes: --> donde se almacena los logs de la DBB.
      - .dbdata:/var/lib/mysql
    ports: -->Puerto a ejecutarse.
      - 33066:3306