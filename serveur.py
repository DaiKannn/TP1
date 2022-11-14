import socket


server_socket = socket.socket()
server_socket.bind(("localhost", 10000))


while True :
    server_socket.listen(500)
    reply=input("Moi : ")
    conn, address = server_socket.accept()
    data = conn.recv(1024).decode()
    conn.send(reply.encode())
    print(f"Message du client : {data}")

    if data == "bye" :
        conn, address = server_socket.accept()
        data = conn.recv(1024).decode()


conn.close()
