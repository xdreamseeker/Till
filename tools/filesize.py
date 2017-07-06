import sys
import os
class FileHelpper():
    def __init__(self,path):
        self._path=path
        self._files=[]

    def _getAllFiles(self):
        for parent,dirnames,filenames in os.walk(self._path):
            #case 1:
            for dirname in dirnames:
                # print("parent folder is:" + parent)
                # print("dirname is:" + dirname)
                pass
            #case 2
            for filename in filenames:
                # print("parent folder is:" + parent)
                print("filename with full path:"+ os.path.join(parent,filename))
                self._files.append(os.path.join(parent,filename))
    def size(self):
        totalsize = 0
        self._getAllFiles()
        for entry in self._files:
            try:
                totalsize += (os.path.getsize(entry)/1024/1024)
            except:
                pass
            # print("%s:%d"%(entry,os.path.getsize(entry)))
        print("%.2fM"%totalsize)

if __name__=="__main__":
    # if len(sys.argv) != 2:
    #     print("参数不正确")
    #     exit(1)
    app = FileHelpper("C:/")
    app.size()

