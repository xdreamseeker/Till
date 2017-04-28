import socket,time


"""
一个简单的socket服务器每次连接之处理一次发送
"""
host = ('127.0.0.1', 8001)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(host)
sock.listen(2)   #超后不处理

while True:
    conn,address = sock.accept()
    print("connect"+repr(conn))
    ret_bytes = conn.recv(1024)
    conn.sendall(ret_bytes)
    conn.close()