from socket import *
import json

def main():
    serverName = "127.0.0.1"
    serverPort = 47123
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    print(f"Connected to: {serverName} on port: {serverPort}")
    client_message = ["apple", "bread", "milk", "grape", "banana"]
    client_message = json.dumps(client_message)
    clientSocket.send(client_message.encode())
    server_message = clientSocket.recv(1024).decode()
    server_message = json.loads(server_message)
    print('The Results are in...(True = Fruit, False = Not a fruit)')
    print(server_message)

if __name__ == "__main__":
    main()