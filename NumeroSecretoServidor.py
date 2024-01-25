import socket
import random

HOST = "127.0.0.1"
PORT = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
numRandom = random.randint(1, 10)
print(numRandom)
conn, addr = s.accept()
print(f"Conexion con el cliente IP({addr[0]}) Puerto({addr[1]})")

while True:
    data = conn.recv(1024)
    print(data.decode())

    if int(data) == numRandom:
        conn.send("Has ganado".encode())
        conn.close()
        break
    elif int(data) < numRandom:
        conn.send("El numero es mayor".encode())
    else:
        conn.send("El numero es menor".encode())

conn.close()
