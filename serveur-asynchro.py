import socket

server_socket = socket.socket()
server_socket.bind(("localhost", 10000))
reply=""
data=""
server_socket.listen(1)

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
server_socket.close()