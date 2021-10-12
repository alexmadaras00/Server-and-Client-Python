import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = 'localhost'
port = 2020
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(2048)
        reply = '[SERVER]: ' + data.decode('utf-8')
        received_message = data.decode()
        if received_message == "Hello":
            connection.send("How are you?".encode())

        elif received_message == "Fine":
            connection.send("Glad to hear that. What is your name?".encode())
        elif received_message == "Quit":
            connection.send("Quitting...".encode())
            connection.close()
            break
        if not data:
            break

    connection.close()


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
