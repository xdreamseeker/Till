import random,sys
class MySort():
    def genList(self,n):
        randlist = []
        i = 0
        while i < n:
            randlist.append(random.randint(0,100))
            i += 1
        return randlist

    def bubbleSort(self,list1):
        length = len(list1)
        for i in range(0,length-1):
            for j in range(0,length-i-1):

                if list1[j] > list1[j+1]:
                    list1[j],list1[j+1] = list1[j+1],list1[j]

    def quickSort(self,list1):

        def doswap(list,start,end):
            if start >= end:        #终止条件
                return
            i,j = start,end
            tmp = list[start]
            while i<j:
                while list[j]>tmp and j>i:
                    j -= 1
                if j>i:
                    list[i] = list[j]
                    i += 1

                while list[i] < tmp and i<j:
                    i+=1
                if i<j:
                    list[j] = list[i]
                    j -=1

            list[i] = tmp
            print(i)
            doswap(list,start,i-1)
            doswap(list,i+1,end)

        sys.setrecursionlimit(1000000)
        doswap(list1,0,len(list1)-1)


    def shellSort(self,list1):
        #步长 + 插入排序
        length = len(list1)
        if length < 2:
            return
        step = int(length/2)
        while step>0:
            for i in range(0,step):#step 内进行直插
                for j in range(i+step,length,step):
                    tmp = list1[j]
                    k = j
                    while k-step >= 0 and tmp <list1[k-step]:
                        list1[k] = list1[k-step]
                        k -= step
                    list1[k]=tmp
            step = int(step/2)

    def insertSort(selfm,list1):
        length = len(list1)
        if length < 2:
            return

        for i in range(1,length):
            tmp = list1[i]
            k=i
            while k-1 >= 0 and tmp < list1[k-1]:
                list1[k]=list1[k-1]
                k -= 1
            list1[k] = tmp


if __name__=="__main__":
    # for i in range(0,10,3):
    #     print(i)
    app = MySort()
    list1 = [10,23,3,54,74,2]
    list1 = app.genList(100)
    print(list1)
    app.insertSort(list1)
    print(list1)