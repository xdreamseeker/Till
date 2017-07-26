import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

if __name__=="__main__":
    data=pd.read_csv('data.csv',encoding='gb2312',parse_dates=True,sep=',')
    print(len(data.columns))
    print(data['title'])
    fig=plt.figure(figsize=(25,20))
    ax1=fig.add_subplot(111)
    #绘制Total曲线图
    ax1.plot(data['sq'],data['title'],color='#4A7EBB',linewidth=4)
    ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
    ax1.set_xlabel('Time',fontsize=16)
    plt.xticks(pd.date_range(data.index[0],data.index[-1],freq='1min'))#时间间隔
    plt.xticks(rotation=90)
    plt.show()

    for x in range(0,len(data.columns)):
        print("第 %d 列 "%x)
        total=data.ix[:,x]
        print(total.index)
        print(total.values)
