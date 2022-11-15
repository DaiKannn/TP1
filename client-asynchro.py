import socket
import threading

client_socket = socket.socket()
client_socket.connect(("localhost", 10000))

def reception (client_socket):
    message=""
    data=""
    while message != "bye" and data !="bye" and message !="arret" and data !="arret" :
        message=input("Moi : ")
        t1 = threading.Thread(target=reception, args=[client_socket])
        t1.start()
        t1.join()
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")

client_socket.close()
