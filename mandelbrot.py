import numpy as np
from numpy import newaxis
import matplotlib.pyplot as plt

def mandelbrot(N_max, threshold, n):
    #1D arrays of size n
    x = np.linspace(-2, 1, n)
    y = np.linspace(-1.5, 1.5, n)
    #nxn grid of c values
    c = x[:, newaxis] + 1j * y[newaxis, :]

    z = 0
    with np.warnings.catch_warnings():
        np.warnings.simplefilter("ignore")
        for j in range(N_max):
            z = z ** 2 + c
        #pt 3 2D boolean array
        mask = (abs(z) < threshold)
    return mask

mask = mandelbrot(50, 50, 50)

#pt 4
plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')
