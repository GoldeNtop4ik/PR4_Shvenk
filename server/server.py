import socket
from _thread import *

def client_thread(con):
    data = con.recv(1024)
    name = data.decode()
    while True:
        data = con.recv(1024)
        message = f"\n{name}: {data.decode()}"
        print(f"{message}")
        for i in clients:
            if i != con:
                i.send(message.encode())

server = socket.socket()
hostname = socket.gethostname()
port = 12345
server.bind((hostname, port))
server.listen(5)

clients = []

print("Сервер запущен")

while True:
    client, _ = server.accept()
    clients.append(client)
    start_new_thread(client_thread, (client,))