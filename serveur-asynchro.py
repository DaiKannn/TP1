import socket
import threading

server_socket = socket.socket()
server_socket.bind(("localhost", 10000))
server_socket.listen(1)

def reception (server_socket):
    reply=""
    data=""
    while reply !="arret" and data !="arret":
        conn, address = server_socket.accept()
        reply=""
        data=""
        while reply != "bye" and data != "bye" and reply != "arret" and data != "arret":
            reply=input("Moi : ")
            data = conn.recv(1024).decode()
            conn.send(reply.encode())
            print(f"Message du client : {data}")
        conn.close()

t1 = threading.Thread(target=reception, args=[server_socket])
t1.start()
t1.join()
server_socket.close()
