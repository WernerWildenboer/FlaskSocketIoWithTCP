#!/usr/bin/env python

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import socket
import threading
import random
import string
import time
import os
from app.client import printfunction
import urllib.parse

 

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = 'threading'


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

global socketio
global socketio2
global socketio3
socketio = SocketIO(app, async_mode=async_mode)

#socketio3 = SocketIO(app, async_mode=async_mode)
thread_1 = None
thread_2 = None
thread_3 = None

#!/usr/bin/python           # This is server.py file


def background_thread_port_12003():
    #client.printfunction("df")
    start = time.process_time()
    serverPort = 12003
    # Create a socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # s = socket.socket()
    # host = socket.gethostname()  # Get local machine name

    serverSocket.bind(('', serverPort))
    print('The server is ready to receive')
    serverSocket.listen(5)                 # Now wait for client connection.
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        count += 1
        print("custom pring calling from server")
        # socketio.emit('my_local_response', {
        #              'data': 'Server generated event', 'count': count}, namespace='/local')
        # Establish connection with client.
        connectionSocket, addr = serverSocket.accept()
        print('Got connection from %s', addr)
        # connectionSocket.send("welcome")
        while True:
            # connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024)
            sentence = sentence.decode('utf-8')  # decode
            x = sentence.split("#")
            count = 0
            if len(x) > 1:
                Out = x[1]
                char = x[0]
                for k in Out:
                    if k == char:
                        count = count + 1
                sCount = str(count)
                end = time.process_time() - start
                Output = sCount + "#" + str(end)
                print(Output)
                connectionSocket.send(Output.encode())



def background_thread_port_12004():
    start = time.process_time()
    serverPort = 12004
    # Create a socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # s = socket.socket()
    # host = socket.gethostname()  # Get local machine name

    serverSocket.bind(('', serverPort))
    print('The server is ready to receive')
    serverSocket.listen(5)                 # Now wait for client connection.
    """Example of how to send server generated events to clients."""

    count = 0
    while True:
        count += 1
        print("custom pring calling from server")
        # socketio.emit('my_local_response', {
        #              'data': 'Server generated event', 'count': count}, namespace='/local')
        # Establish connection with client.
        connectionSocket, addr = serverSocket.accept()
        print('Got connection from %s', addr)
        # connectionSocket.send("welcome")
        while True:
            # connectionSocket, addr = serverSocket.accept()
            sentence = sentence.decode('utf-8')  # decode
            x = sentence.split("#")
            count = 0
            if len(x) > 1:
                Out = x[1]
                char = x[0]
                for k in Out:
                    if k == char:
                        count = count + 1
                sCount = str(count)
                end = time.process_time() - start
                Output = sCount + "#" + str(end)
                connectionSocket.send(Output.encode())

            # connectionSocket.close()
            # socketio.emit('my_local_response', {
            #             'data': 'MESSAGE FROM TCP SERVER', 'count': x}, namespace='/local')


def background_thread_port_12005():
    start = time.process_time()
    serverPort = 12005
    # Create a socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # s = socket.socket()
    # host = socket.gethostname()  # Get local machine name
    host = socket.gethostname()

    serverSocket.bind((host, serverPort))
    print('The server is ready to receive')
    serverSocket.listen(5)                 # Now wait for client connection.
    """Example of how to send server generated events to clients."""

    count = 0
    while True:
        count += 1
        print("custom pring calling from server")
        # socketio.emit('my_local_response', {
        #              'data': 'Server generated event', 'count': count}, namespace='/local')
        # Establish connection with client.
        connectionSocket, addr = serverSocket.accept()
        print('Got connection from %s', addr)
        # connectionSocket.send("welcome")
        while True:
            # connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024)
            sentence = sentence.decode('utf-8')  # decode
            x = sentence.split("#")
            count = 0
            if len(x) > 1:
                Out = x[1]
                char = x[0]
                for k in Out:
                    if k == char:
                        count = count + 1
                sCount = str(count)
                end = time.process_time() - start
                Output = sCount + "#" + str(end)
                connectionSocket.send(Output.encode())


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('Post')

            
    return render_template('index.html', async_mode=socketio.async_mode ,)

@socketio.on('connect')
def connect():
    #background_thread_port_12003()
    #client.connect_12003()
    #background_thread_port_12004()
    #client.connect_12004()
    #background_thread_port_12005()
    #client.connect_12005()
    #client.start()
    print('Connect')
    

serverName = ''
combo = string.ascii_letters + string.digits



def random_string_generator(str_size, allowed_chars):
    """
    Generates a random number
    Input : str_size, allowed_chars
    Returns : chars of type String(<class 'str'>)
    """
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


def encode():
    """
    Encodes input 
    """


def create_random_character_plus_input(user_input, combo_in):
    """
    Create random character
    """
    random_string = random_string_generator(30, combo_in)
    sentence = user_input + "#" + random_string
    return sentence


def count_time_decode(from_server):
    """
    Decodes message
    gets time
    gets String 

    Return Dictionary of count and time 
    """
    from_server_decoded = from_server.decode('utf-8')
    string = from_server_decoded.split("#")
    count = string[0]
    time = string[1]
    count_time_dict = {'count': count, 'time': time}
    return count_time_dict
 

class MyNamespace(Namespace):
    def on_my_event(self, message):
        start = time.process_time()
        if message['data'] == "I'm connected!":
            emit('my_local_response',{'data':"I'm connected!"})
        else:
            
            session['receive_count'] = session.get('receive_count', 0) + 1
            emit('my_response',
                {'data': message['data'], 'count': session['receive_count']})
            emit('my_local_response',
                {'data': message['data'], 'count': session['receive_count']})
        
            sentence = message['data']

            sentence = urllib.parse.unquote(sentence)

            x = str(sentence).split("#")
    
            count = 0
            if len(x) > 1:
                Out = x[1]
                char = x[0]
                for k in Out:
                    if k == char:
                        count = count + 1
            sCount = str(count)
            end = time.process_time() - start
            Output = sCount + "#" + str(end)

            emit('my_local_response',
                {'data': "String Encoded : "+ message['data2'], 'count': session['receive_count']})

    
            session['num1'] = sCount
            emit('my_local_response',{'data': 'From Server B : ' + sCount, 'count':  session['receive_count']})
            session['receive_count'] = session.get('receive_count', 0) + 1
            emit('my_local_response',{'data': 'Time Taken from Server B : ' + str(end), 'count':  session['receive_count']})
            session['receive_count'] = session.get('receive_count', 0) + 1
            #emit('my_local_response',{'data': 'Total_count:' + str(sever_info['total_count']), 'count':  session['receive_count']})
            print(Output)

    def on_my_broadcast_event(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_local_response',
             {'data': message['data'], 'count': session['receive_count']},
             broadcast=True)

    def on_disconnect_request(self):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_local_response',
             {'data': 'Disconnected!', 'count': session['receive_count']})
        disconnect()

    def on_my_ping(self):
        emit('my_pong')

    def on_connect(self):
        global thread_1

        if thread_1 is None:
            socketio.start_background_task(target=background_thread_port_12003)
        #if thread_2 is None:
        #    socketio.start_background_task(target=background_thread_port_12004)
        #if thread_3 is None:
        #    socketio.start_background_task(target=background_thread_port_12005)
        emit('my_response', {'data': 'Connected', 'count': 0})

    def on_disconnect(self):
        print('Client disconnected', request.sid)


socketio.on_namespace(MyNamespace('/local'))


class MyNamespace2(Namespace):
    def on_my_event(self, message):
        start = time.process_time()
        if message['data'] == "I'm connected!":
            emit('my_local_response',{'data':"I'm connected!"})
        else:

            session['receive_count'] = session.get('receive_count', 0) + 1
            emit('my_response',
                {'data': message['data'], 'count': session['receive_count']})
            emit('my_local_response',
                {'data': message['data'], 'count': session['receive_count']})
        
            sentence = message['data']

            sentence = urllib.parse.unquote(sentence)

            x = str(sentence).split("#")
    
            count = 0
            if len(x) > 1:
                Out = x[1]
                char = x[0]
                for k in Out:
                    if k == char:
                        count = count + 1
            sCount = str(count)
            end = time.process_time() - start
            Output = sCount + "#" + str(end)

            emit('my_local_response',
                {'data': "String Encoded : "+ message['data2'], 'count': session['receive_count']})

    
            session['num2'] = sCount
            emit('my_local_response',{'data': 'From Server C : ' + sCount, 'count':  session['receive_count']})
            session['receive_count'] = session.get('receive_count', 0) + 1
            emit('my_local_response',{'data': 'Time Taken from Server C : ' + str(end), 'count':  session['receive_count']})
            session['receive_count'] = session.get('receive_count', 0) + 1
            #emit('my_local_response',{'data': 'Total_count:' + str(sever_info['total_count']), 'count':  session['receive_count']})
            print(Output)

       
 
  
    def on_my_broadcast_event(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_local_response',
             {'data': message['data'], 'count': session['receive_count']},
             broadcast=True)

    def on_disconnect_request(self):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_local_response',
             {'data': 'Disconnected!', 'count': session['receive_count']})
        disconnect()

    def on_connect(self):
        global thread_2
        #if thread_1 is None:
        #    socketio.start_background_task(target=background_thread_port_12003)
        if thread_2 is None:
            socketio.start_background_task(target=background_thread_port_12004)
        #if thread_3 is None:
        #    socketio.start_background_task(target=background_thread_port_12005)
        emit('my_response', {'data': 'Connected', 'count': 0})

    def on_disconnect(self):
        print('Client disconnected', request.sid)


socketio.on_namespace(MyNamespace2('/local2'))

class MyNamespace3(Namespace):
    def on_my_event(self, message):
        start = time.process_time()
        if message['data'] == "I'm connected!":
            emit('my_local_response',{'data':"I'm connected!"})
        else:

            session['receive_count'] = session.get('receive_count', 0) + 1
            emit('my_response',
                {'data': message['data'], 'count': session['receive_count']})
            emit('my_local_response',
                {'data': message['data'], 'count': session['receive_count']})
        
            sentence = message['data2']

            sentence = urllib.parse.unquote(sentence)

            x = str(sentence).split("#")
    
            count = 0
            if len(x) > 1:
                Out = x[1]
                char = x[0]
                for k in Out:
                    if k == char:
                        count = count + 1
            sCount = str(count)
            end = time.process_time() - start
            Output = sCount + "#" + str(end)
            emit('my_local_response',
                {'data': "String Encoded : "+ message['data2'], 'count': session['receive_count']})
            #emit('my_local_response',
            #    {'data': "String Dencoded : "+ sentence, 'count': session['receive_count']})
    
            session['num3'] = sCount
            emit('my_local_response',{'data': 'From Server D : ' + sCount, 'count':  session['receive_count']})
            session['receive_count'] = session.get('receive_count', 0) + 1
            emit('my_local_response',{'data': 'Time Taken from Server D :   ' + str(end), 'count':  session['receive_count']})
            session['receive_count'] = session.get('receive_count', 0) + 1
            #emit('my_local_response',{'data': 'Total_count:' + str(sever_info['total_count']), 'count':  session['receive_count']})

            total = int(session['num1'])+int(session['num2'])+int(session['num3'])
            emit('my_local_response',{'total': 'Total:  ' + str(total)})
            session['receive_count'] = session.get('receive_count', 0) + 1
            print(Output)
    
        
 
  
    def on_my_broadcast_event(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_local_response',
             {'data': message['data'], 'count': session['receive_count']},
             broadcast=True)

    def on_disconnect_request(self):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_local_response',
             {'data': 'Disconnected!', 'count': session['receive_count']})
        disconnect()

    def on_connect(self):
        global thread_3
        if thread_3 is None:
            socketio.start_background_task(target=background_thread_port_12005)
        emit('my_response', {'data': 'Connected', 'count': 0})

    def on_disconnect(self):
        print('Client disconnected', request.sid)


socketio.on_namespace(MyNamespace3('/local3'))


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0',port=5000)


