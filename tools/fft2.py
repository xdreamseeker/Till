import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *



def showHist(arr):
    hist =arr
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xsize = hist.shape[0] + 1
    ysize = hist.shape[1] + 1
    xedges=arange(0, xsize, 1)
    yedges=arange(0, ysize, 1)
    # Construct arrays for the anchor positions of the 16 bars.
    # Note: np.meshgrid gives arrays in (ny, nx) so we use 'F' to flatten xpos,
    # ypos in column-major order. For numpy >= 1.7, we could instead call meshgrid
    # with indexing='ij'.
    xpos, ypos = np.meshgrid(xedges[:-1]  + 0.75, yedges[:-1] + 0.75)
    xpos = xpos.flatten('F')
    ypos = ypos.flatten('F')
    zpos = np.zeros_like(xpos)

    # Construct arrays with the dimensions for the 16 bars.
    dx = 0.5 * np.ones_like(zpos)
    dy = dx.copy()
    dz = hist.flatten()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

    plt.show()


if __name__=="__main__":
    hist =array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
    img = cv.imread('lena.jpg', 0)
    showHist(img)