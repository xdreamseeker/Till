import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib.dates import date2num,num2date
import datetime as DT
import numpy as np


if __name__=="__main__":
    data=pd.read_csv('data.csv',encoding='gb2312',parse_dates=True,sep=',')
    print(len(data.columns))

    fig=plt.figure(figsize=(10,8))
    ax1=fig.add_subplot(111)
    #绘制Total曲线图
    x = data['no']
    x = [date2num(DT.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")) for date in data['no']]

    y = data['value']

    ax1.scatter(x,y,s=1)
    #T:散点的颜色
#s：散点的大小
#alpha:是透明程度
    ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
    ax1.set_xlabel('Time',fontsize=16)
    ticks =pd.date_range(data['no'][0],data['no'][data['no'].size -1],freq='30min')
    # ticks =pd.date_range(data['no'][0],data['no'][-1],freq='2min')

    plt.xticks(ticks)#时间间隔
    plt.xticks(rotation=90)
    plt.show()

    # for x in range(0,len(data.columns)):
    #     print("第 %d 列 "%x)
    #     total=data.ix[:,x]
    #     print(total.index)
    #     print(total.values)


#select  to_char((timestamp '1970-01-01 00:00:00 GMT' + numtodsinterval(CLOCK, 'SECOND')) at time zone 'Asia/Shanghai', 'YYYY-MM-DD HH24:MI:SS') clocktime,value from HISTORY t where t.ITEMID='78087' and clock > (sysdate-1-to_date('1970-01-01','YYYY-MM-DD HH24:MI:SS'))*86400;