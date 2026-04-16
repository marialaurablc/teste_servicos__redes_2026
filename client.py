import socket

HOST = "172.18.60.12"
PORT = 2026

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Msg: ")
    if message == "q":
        break
    else:
        udp.sendto(message.encode(), (HOST, PORT))
udp.close()
