#!/usr/bin/env python
import pika
import sys, json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

data = {
    "orderId" : 123,
    "status" : "completed"
}

data = json.dumps(data)

channel.basic_publish(exchange='logs', routing_key='', body=data)
print(" [x] Sent %r" % data)
connection.close()