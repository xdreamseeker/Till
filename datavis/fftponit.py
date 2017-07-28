import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib.dates import date2num,num2date
import datetime as DT
import numpy as np

if __name__=="__main__":
    data=pd.read_csv('data.csv',encoding='gb2312',parse_dates=True,sep=',')
    print(len(data.columns))

    fig=plt.figure(figsize=(12,5))

    #绘制Total曲线图
    x = data['no']
    x = [date2num(DT.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")) for date in data['no']]


    y = data['value']

    f = np.fft.fft(y)
    freq = np.fft.fftfreq(len(x))

    ax1=fig.add_subplot(221)

    ax1.scatter(x,y,s=1)
    ax4=fig.add_subplot(222)

    ax4.scatter(x,f,s=1)

    ax2=fig.add_subplot(223)
    ax2.plot(freq,f.real)

    ax3=fig.add_subplot(224)
    ax3.plot(freq,f.imag)


    plt.show()

    # for x in range(0,len(data.columns)):
    #     print("第 %d 列 "%x)
    #     total=data.ix[:,x]
    #     print(total.index)
    #     print(total.values)


#select  to_char((timestamp '1970-01-01 00:00:00 GMT' + numtodsinterval(CLOCK, 'SECOND')) at time zone 'Asia/Shanghai', 'YYYY-MM-DD HH24:MI:SS') clocktime,value from HISTORY t where t.ITEMID='78087' and clock > (sysdate-1-to_date('1970-01-01','YYYY-MM-DD HH24:MI:SS'))*86400;