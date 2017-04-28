import sys
import time
import socket
import select
import queue

"""
一个select socket 服务器

一个epoll socket 服务器
sellect、poll、epoll三者的区别（多路IO复用都是同步的）
select
select最早于1983年出现在4.2BSD中，它通过一个select()系统调用来监视多个文件描述符的数组，当select()返回后，该数组中就绪的文件描述符便会被内核修改标志位，使得进程可以获得这些文件描述符从而进行后续的读写操作。
select目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个优点，事实上从现在看来，这也是它所剩不多的优点之一。
select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，不过可以通过修改宏定义甚至重新编译内核的方式提升这一限制。
另外，select()所维护的存储大量文件描述符的数据结构，随着文件描述符数量的增大，其复制的开销也线性增长。同时，由于网络响应时间的延迟使得大量TCP连接处于非活跃状态，但调用select()会对所有socket进行一次线性扫描，所以这也浪费了一定的开销。

poll
poll在1986年诞生于System V Release 3，它和select在本质上没有多大差别，但是poll没有最大文件描述符数量的限制。
poll和select同样存在一个缺点就是，包含大量文件描述符的数组被整体复制于用户态和内核的地址空间之间，而不论这些文件描述符是否就绪，它的开销随着文件描述符数量的增加而线性增大。
另外，select()和poll()将就绪的文件描述符告诉进程后，如果进程没有对其进行IO操作，那么下次调用select()和poll()的时候将再次报告这些文件描述符，所以它们一般不会丢失就绪的消息，这种方式称为水平触发（Level Triggered）。

epoll
直到Linux2.6才出现了由内核直接支持的实现方法，那就是epoll，它几乎具备了之前所说的一切优点，被公认为Linux2.6下性能最好的多路I/O就绪通知方法。
epoll可以同时支持水平触发和边缘触发（Edge Triggered，只告诉进程哪些文件描述符刚刚变为就绪状态，它只说一遍，如果我们没有采取行动，那么它将不会再次告知，这种方式称为边缘触发），理论上边缘触发的性能要更高一些，但是代码实现相当复杂。

epoll同样只告知那些就绪的文件描述符，而且当我们调用epoll_wait()获得就绪文件描述符时，返回的不是实际的描述符，而是一个代表就绪描述符数量的值，你只需要去epoll指定的一个数组中依次取得相应数量的文件描述符即可，这里也使用了内存映射（mmap）技术，这样便彻底省掉了这些文件描述符在系统调用时复制的开销。

"""
class Server(object):
    def __init__(self, host='127.0.0.1', port=8001, timeout=2, client_nums=10):
        self.__host = host
        self.__port = port
        self.__timeout = timeout
        self.__client_nums = client_nums
        self.__buffer_size = 1024

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setblocking(False)
        self.server.settimeout(self.__timeout)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #keepalive SO_KEEPALIVE 保持连接检测对方主机是否崩溃，避免（服务器）永远阻塞于TCP连接的输入。
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #端口复用
        server_host = (self.__host, self.__port)
        try:
            self.server.bind(server_host)
            self.server.listen(self.__client_nums)
        except:
            raise Exception("bind error")

        self.inputs = [self.server] #select 接收文件描述符列表
        self.outputs = [] #输出文件描述符列表
        self.message_queues = {}#消息队列
        self.client_info = {}

    def run(self):
        while True:
            readable , writable , exceptional = select.select(self.inputs, self.outputs, self.inputs, 10)
            if not (readable or writable or exceptional) :
                continue

            for s in readable :
                if s is self.server:#是客户端连接
                    connection, client_address = s.accept()
                    #print "connection", connection
                    print("%s connect." % repr(client_address))
                    connection.setblocking(0) #非阻塞
                    self.inputs.append(connection) #客户端添加到inputs
                    self.client_info[connection] = repr(client_address)
                    self.message_queues[connection] = queue.Queue()   #每个客户端一个消息队列

                else:#是client, 数据发送过来
                    try:
                        data = s.recv(self.__buffer_size)
                    except:
                        err_msg = "Client Error!"+repr(s)
                        print(err_msg)
                    if data :
                        #print data
                        data = "%s %s say: %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.client_info[s], data)
                        self.message_queues[s].put(data) #队列添加消息

                        if s not in self.outputs: #要回复消息
                            self.outputs.append(s)
                    else: #客户端断开
                        #Interpret empty result as closed connection
                        print("Client:%s Close." % str(self.client_info[s]))
                        if s in self.outputs :
                            self.outputs.remove(s)
                        self.inputs.remove(s)
                        s.close()
                        del self.message_queues[s]
                        del self.client_info[s]

             # 如果现在没有客户端请求,也没有客户端发送消息时，开始对发送消息列表进行处理，是否需要发送消息
            for s in writable: #outputs 有消息就要发出去了
                try:
                # 如果消息队列中有消息,从消息队列中获取要发送的消息
                    if not self.message_queues[s].empty():  # 从该客户端对象的消息队列中获取要发送的消息
                        send_data = self.message_queues[s].get()
                        s.sendall(send_data.encode(encoding="utf-8"))
                    else:  # 将监听移除等待下一次客户端发送消息
                        self.outputs.remove(s)

                except ConnectionResetError:# 客户端连接断开了
                    del self.message_queues[s]
                    self.outputs.remove(s)
                    print("\n[output] Client  {0} disconnected".repr(s))

            for s in exceptional:
                print("Client:%s Close Error." % repr(self.client_info[s]))
                if s in self.inputs:
                    self.inputs.remove(s)
                    s.close()
                if s in self.outputs:
                    self.outputs.remove(s)
                if s in self.message_queues:
                    del self.message_queues[s]
                del self.client_info[s]


if "__main__" == __name__:
    Server().run()
    print("aa")