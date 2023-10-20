import socket
from _thread import *

client = socket.socket()
hostname = socket.gethostname()
port = 12345
client.connect((hostname,port))

name = input("Имя: ")
client.send(name.encode())

def Send():
    while True:
        message = input("Введите текст")
        client.send(message.encode())
def Take():
    while True:
        data = client.recv(1024)
        print(data.decode())
        
start_new_thread(Send, ())
start_new_thread(Take, ())

while True:
    a = 1