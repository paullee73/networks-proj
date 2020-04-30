import zmq
import random
import sys
import time

# wrapper functions ---------------------------------------------------------- #

# prompt user for port, allow only digits
def get_port():
    port = input('Please enter port number: ')

    while not port.isdigit():
        port = input('Please enter only digits for port number: ')

    return int(port)

# create socket using given port
def create_socket(port):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:%s' % port)

    return socket

def publish(socket, topic=None, message=None):
    # if arguments are not provided, prompt user for them
    if message is None:
        message = input('Please enter message you want to broadcast: ')
    if topic is None:
        topic = get_topic()

    socket.send_string('%d %s' % (topic, message))
    print('Sent \'%s\' on topic # %d' % (message, topic))

# prompt user for topic, allow only digits
def get_topic():
    topic = input('Please enter topic number over which to broadcast message: ')

    while not topic.isdigit():
        topic = input('Please enter only digits for topic number: ')

    return int(topic)

# test code ------------------------------------------------------------------ #

port = get_port()

socket = create_socket(port)

# first, prompt user for message and topic
publish(socket)

# then publish a hardcoded message on topic 8888
publish(socket, 8888, 'hi')
