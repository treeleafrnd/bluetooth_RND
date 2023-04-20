import socket
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("a8:64:f1:69:9f:82", 4))
server.listen(1)
client,addr = server.accept()
try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Mesage: {data.decode('utf-8')}")
        message = input("enter msg:")

        client.send(message.encode("utf-8"))
except OSError as e:
    pass
client.close()
server.close()