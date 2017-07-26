import pandas as pd

if __name__=="__main__":
    data=pd.read_csv('data.csv',encoding='gb2312',parse_dates=True,sep=',')
    print(len(data.columns))
    print(data['title'])

    for x in range(0,len(data.columns)):
        print("第 %d 列 "%x)
        total=data.ix[:,x]
        print(total.index)
        print(total.values)