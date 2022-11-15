import socket

client_socket = socket.socket()
client_socket.connect(("localhost", 10000))
message=""
data=""

while message != "bye" and data !="bye" and message !="arret" and data !="arret" :
    message=input("Moi : ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(f"Message du serveur : {data}")

client_socket.close()
