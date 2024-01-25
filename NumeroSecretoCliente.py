import socket

HOST = "127.0.0.1"
PORT = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Conectado con exito")
acertado = True

intentos = 0
while acertado and intentos < 4:
    numero = input("dame un numero: ")
    s.send(numero.encode())
    data = s.recv(1024)

    if not data:
        print("El servidor ha cerrado la conexión.")
        break

    if data.decode() == "Has ganado":
        print("Has acertado el numero")
        print(data.decode())
        acertado = False
    else:
        print(f"Recibo: {data.decode()}")
        intentos += 1

if acertado and intentos == 4:
    print("Has perdido")
s.close()
