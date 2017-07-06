import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

img = cv.imread('lena.jpg', 0)
f = np.fft.fft2(img) # 快速傅里叶变换算法得到频率分布
fshift = np.fft.fftshift(f) # 默认结果中心点位置是在左上角，转移到中间位置

fimg = np.log(np.abs(fshift)) # fft 结果是复数，求绝对值结果才是振幅

# 逆变换
f1shift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f1shift)
#出来的是复数，无法显示
img_back = np.abs(img_back)


# 展示结果
plt.subplot(131), plt.imshow(img, 'gray'), plt.title('Original Fourier')
plt.subplot(132), plt.imshow(fimg, 'gray'), plt.title('Fourier Fourier')
plt.subplot(133),plt.imshow(img_back,'gray'),plt.title('img back')
plt.show()