import socket

# SOCK_DGRAM -> UDP
# SOCK_STREAM -> TCP

HOSTNAME = socket.gethostbyname('server')
PORT_NUMBER = 8000
SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOSTNAME, PORT_NUMBER))

print(f"Server address: {HOSTNAME}")
print(f"Server listening on port {PORT_NUMBER}")

# queue of 5 just in case
server_socket.listen(5)

flag = True
while flag:
    # create a new socket instance to handle the connection
    new_socket, address = server_socket.accept()

    # receive
    byte_message = new_socket.recv(SIZE)
    message = byte_message.decode("utf-8")
    print(f"Received packet from {address}: {message}")

    # send
    reply = f"Hello from the server"
    new_socket.send(bytes(reply, "utf-8"))
    print(f"Sent packet to {address}: {reply}")
    new_socket.close()