import socket

SERVER_IP = socket.gethostbyname('server')
#SERVER_IP = '0.0.0.0'

PORT_NUMBER = 8000
SIZE = 1024
print(f"Server address: {SERVER_IP}:{PORT_NUMBER}")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT_NUMBER))

flag = True
while flag:

    # send
    message = "Hello from the python client"
    print(f"Send message: {message}")
    client_socket.send(bytes(message, "utf-8"))

    # receive
    byte_message = client_socket.recv(SIZE)
    message = byte_message.decode("utf-8")

    print(f"Receive message: {message}")
    flag = False
    