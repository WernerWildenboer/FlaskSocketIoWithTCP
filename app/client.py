# This is the client

import socket
from socket import *              # Import socket module
import random
import string
import time
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
    close_room, rooms, disconnect


# Server variables
serverName = ''
combo = string.ascii_letters + string.digits


def printfunction(x):
    print(x)

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


# Port 1
        #try:
def connect_12003():
    serverPort = 12003
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    while True:
        from_server_1 = clientSocket.recv(1024)
        clientSocket.sendall(create_random_character_plus_input(
                    user_input, combo).encode('utf-8'))
        dict_ct_1 = count_time_decode(from_server_1)
        print(dict_ct_1)
    
        #except ValueError:
            #print('Connection Error')
            # Port 2
        #try:
def connect_12004():
    serverPort2 = 12004
    clientSocket2 = socket(AF_INET, SOCK_STREAM)
    clientSocket2.connect((serverName, serverPort2))
    while True:
        from_server_1 = clientSocket2.recv(1024)
        clientSocket2.sendall(create_random_character_plus_input(
                    user_input, combo).encode('utf-8'))
        dict_ct_1 = count_time_decode(from_server_1)
        print(dict_ct_1)
            # Port 3
        #except ValueError:
            #print('Connection Error')
        #try:
        #try:
def connect_12005():
    serverPort3 = 12005
    clientSocket3 = socket(AF_INET, SOCK_STREAM)
    clientSocket3.connect((serverName, serverPort3))
    while True:
        from_server_1 = clientSocket3.recv(1024)
        user_input=input('Input character (letter or digit): ')
        clientSocket3.sendall(create_random_character_plus_input(
                    user_input, combo).encode('utf-8'))
        dict_ct_1 = count_time_decode(from_server_1)
        print(dict_ct_1)
        #except ValueError:
            #print('Connection Error')

          

           
        


def start():
    while True:
            print('olo')
            from_server_1 = connect_12003().recv(1024)
            from_server_2 = connect_12004().recv(1024)
            from_server_3 = connect_12005().recv(1024)

            connect_12003().sendall(create_random_character_plus_input(
                user_input, combo).encode('utf-8'))
            connect_12004().sendall(create_random_character_plus_input(
                user_input, combo).encode('utf-8'))
            connect_12005().sendall(create_random_character_plus_input(
                user_input, combo).encode('utf-8'))
            
            dict_ct_1 = count_time_decode(from_server_1)
            dict_ct_2 = count_time_decode(from_server_2)
            dict_ct_3 = count_time_decode(from_server_3)

            total_count = int(dict_ct_1['count']) + \
                int(dict_ct_2['count']) + int(dict_ct_3['count'])

            dict_server_info = {'server1':dict_ct_1,'server2':dict_ct_2,'server3':dict_ct_3,'total_count':total_count}

            print(dict_server_info)
    
