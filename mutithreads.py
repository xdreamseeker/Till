import threadpool
import time

def func(msg):
    print("msg:"+ msg)
    time.sleep(1)
    print("end")
    return "done" + msg
def print_result():
    pass

if __name__ == "__main__":
    task_pool=threadpool.ThreadPool(1000)
    request_list=[]#存放任务列表
    data = []
    for i in range(0,20000):
        msg="hello %d"%(i)
        data.append(msg)
    request_list=threadpool.makeRequests(func,data)
    # map(task_pool.putRequest,request_list)
    [task_pool.putRequest(req) for req in request_list]
#     for req in requests:
# 　　　　 pool.putRequest(req)
    task_pool.wait()

    print("Sub-process(es) done.")