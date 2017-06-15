import hotfixdemo.refresh as refresh
import os
import time
import sys
import importlib
if __name__=="__main__":
    rc = refresh.RefreshClass()
    rc.print_info()


    while True:
        if os.path.exists('refresh.signal'):
            print('reload')
            importlib.reload(refresh)
            print(rc.__class__)
            rc.__class__ = refresh.RefreshClass

        time.sleep(5)
        rc.print_info()

