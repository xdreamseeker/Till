import numpy as np
from matplotlib.pyplot import plot, show
x = np.linspace(0, 2 * np.pi, 30)
wave = np.cos(x)  #创建一个包含30个点的余弦波信号。
transformed = np.fft.fft(wave)  #使用fft函数对余弦波信号进行傅里叶变换。
shifted = np.fft.fftshift(transformed) #使用fftshift函数进行移频操作。
print(np.all((np.fft.ifftshift(shifted) - transformed) < 10 ** -9))  #用ifftshift函数进行逆操作，这将还原移频操作前的信号。
plot(transformed, lw=2)
plot(shifted, lw=3)
show()