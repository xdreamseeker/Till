import threading
import time
import queue

def register(self):
    pass


class Bot():
    def __init__(self):
        print("init")
        self.msgq = queue.Queue()

        self.listening_thread=threading.Thread(target=self._listen)
        self.listening_thread.start()

        self.product_thread=threading.Thread(target=self._product_thread)
        self.product_thread.start()

    def _listen(self):
        while True:
            try:
                msg = self.msgq.get(block=True,timeout=0.5)
                self.process(str(msg))
            except queue.Empty:
                print(" i am lisetn.....")
                time.sleep(5)
    @register
    def process(self,msg):
        print("process:"+msg)



    def _product_thread(self):
        while True:
            try:
                self.msgq.put(11)
                print("put one")
                time.sleep(1)
            except queue.Full:
                print("queue is full")
                time.sleep(10)

    def join(self):
        self.listening_thread.join()
        self.product_thread.join()
