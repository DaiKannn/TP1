import socket
hope =True

client_socket = socket.socket()
# client_socket.connect(("localhost", 10000))

while hope == True :
    client_socket.connect(("localhost", 10000))
    message=input("Moi : ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(f"Message du serveur : {data}")

    if message == "bye" :
        client_socket.close()
        hope = False


client_socket.close()
