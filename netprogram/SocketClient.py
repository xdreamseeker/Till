import socket,time

host = ('127.0.0.1', 8001)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(host)

while True:
    try:
        sock.sendall(b"a")
        ret = str(sock.recv(1024),encoding="utf-8")
        print(ret)
    except socket.error:
        print("error")
        break
    time.sleep(2)