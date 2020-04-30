import sys
import zmq

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
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://localhost:%s' % port)

    return socket

def subscribe_to_topic(socket, topic=None):
    if topic is None:
        topic = get_topic()

    socket.setsockopt(zmq.SUBSCRIBE, topic.encode())

    print('Now receiving messages on topic # %s...' % topic)

def process_n_updates(n, socket):
    for update in range(n):
        data = socket.recv()
        topic, message = data.split()

        print('Message received: \'%s\' over topic # %s' % (message, topic))

# prompt user for topic, allow only digits
def get_topic():
    topic = input('Please enter topic number over which to receive messages: ')

    while not topic.isdigit():
        topic = input('Please enter only digits for topic number: ')

    return topic

# test code ------------------------------------------------------------------ #

port = get_port()

socket = create_socket(port)

subscribe_to_topic(socket)

process_n_updates(2, socket)
