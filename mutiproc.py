import multiprocessing
import time

def func(msg):
    print("msg:"+ msg)
    time.sleep(1)
    print("end")
    return "done" + msg

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=8)
    result = []
    for i in range(0,100):
        msg="hello %d"%(i)
        result.append(pool.apply_async(func,(msg,)))
    pool.close()
    pool.join()
    for res in result:
        print(":::"+res.get())
    print("Sub-process(es) done.")