import numpy as np
import pandas as pd

if __name__=="__main__":
    for i in range(0,3):
        print(i)
    obj = pd.Series(range(3),index=['a','b','c'])
    print(obj)

    frame = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['ac','bc','cc'])
    print(frame)