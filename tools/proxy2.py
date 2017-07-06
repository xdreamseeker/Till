import asyncore,socket

class Receiver(asyncore.dispatcher):
    def __init__(self, sock):
        asyncore.dispatcher.__init__(self,sock)
        self.from_remote_buffer = b''
        self.to_remote_buffer = b''
        self.sender = None

    def handle_connect(self):
        pass

    def handle_read(self):
        read = self.recv(8192)
        print("recv:"+repr(read))
        self.from_remote_buffer += read


    def writable(self):
        return (len(self.to_remote_buffer) > 0)

    def handle_write(self):
        sent = self.send(self.to_remote_buffer)
        print("sent:"+repr(sent))
        self.to_remote_buffer = self.to_remote_buffer[sent:]

    def handle_close(self):
        self.close()
        if self.sender:
            self.sender.close()


class Sender(asyncore.dispatcher):
    def __init__(self,receiver):
        asyncore.dispatcher.__init__(self)
        self.receiver=receiver
        receiver.sender=self
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect(('www.linux.org',80))


    def handle_read(self):
        read=self.recv(8192)
        print("proxy recv:"+repr(read))
        self.receiver.to_remote_buffer += read

    def writable(self):
        return (len(self.receiver.from_remote_buffer) > 0)

    def handle_write(self):
        sent=self.send(self.receiver.from_remote_buffer)
        print("proxy send:"+repr(sent))
        self.receiver.from_remote_buffer=self.receiver.from_remote_buffer[sent:]

    def handle_close(self):
        self.close()
        self.receiver.close()

class HTTPClient(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.buffer=bytes('', 'ascii')
    # def __init__(self, host, path):
    #     asyncore.dispatcher.__init__(self)
    #     self.create_socket()
    #     self.connect( (host, 80) )
    #     self.buffer = bytes('GET %s HTTP/1.0\r\nHost: %s\r\n\r\n' %(path, host), 'ascii')

    # def handle_connect(self):
    #     pass
    #
    # # def handle_close(self):
    # #     self.close()
    #
    # def handle_read(self):
    #     data = self.recv(8192)
    #     print("recv:"+data)
    #
    #
    # def writable(self):
    #     return (len(self.buffer) > 0)
    #
    # def handle_write(self):
    #     print("send:"+self.buffer)
    #     sent = self.send(self.buffer)
    #     self.buffer = self.buffer[sent:]

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        Sender(Receiver(sock))


client = HTTPClient('localhost', 8080)
asyncore.loop()