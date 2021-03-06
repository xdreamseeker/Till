import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib.dates import date2num,num2date
import datetime as DT

if __name__=="__main__":
    data=pd.read_csv('data.csv',encoding='gb2312',parse_dates=True,sep=',')
    print(len(data.columns))

    fig=plt.figure(figsize=(10,8))
    ax1=fig.add_subplot(111)
    #绘制Total曲线图
    x = data['no']
    x = [date2num(DT.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")) for date in data['no']]
    f = np.fft.fft2(img)

    y = data['value']

    ax1.plot(x,y,color='#4A7EBB',linewidth=1)
    ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
    ax1.set_xlabel('Time',fontsize=16)

    ticks =pd.date_range(data['no'][0],data['no'][data['no'].size -1],freq='30min')
    plt.xticks(ticks)#时间间隔
    plt.xticks(rotation=90)
    plt.show()

    # for x in range(0,len(data.columns)):
    #     print("第 %d 列 "%x)
    #     total=data.ix[:,x]
    #     print(total.index)
    #     print(total.values)
