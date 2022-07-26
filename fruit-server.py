#!/usr/bin/env python3

from queue import Empty
from socket import *
import json
from sys import flags
from tabnanny import check

def main():
    serverName = '127.0.0.1'
    serverPort = 47123
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((serverName, serverPort))

    serverSocket.listen(1)
    print(f'Server listening on: localhost port: {serverPort}')
    
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(f"Connected by: {addr}")
        client_message = connectionSocket.recv(1024).decode()
        client_message = json.loads(client_message)
        print(f"Received message from client: {client_message}")
        fruit_list = ['apple', 'mango', 'grape', 'watermelon', 'banana', 'kiwi', 'peach', 'strawberry', 'blueberry', 'cherry']
        def list_contains_fruit(data, fruit_list):
            items = []
            for item in data:
                
                if item in fruit_list:
                    items.append(True)
                else:
                    items.append(False)
            return(items)
        final_message = list_contains_fruit(client_message, fruit_list)
        print("Sent the final message successfully...")
        server_message = json.dumps(final_message)
        connectionSocket.send(server_message.encode())

if __name__ == "__main__":
    main()