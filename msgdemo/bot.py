import threading
import time
class Bot():
    def __init__(self):
        print("init")
        self.listening_thread=threading.Thread(target=self._listen)
        self.listening_thread.start()

    def _listen(self):
        while True:
            print(" i am lisetn.....")
            time.sleep(5)



    def join(self):
        self.listening_thread.join()
