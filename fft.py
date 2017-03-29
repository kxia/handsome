#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
#t = np.loadtxt("./surfaceElevation.dat" , usecols= (11,))
t_1 = np.loadtxt("./dock_motion.txt",usecols=(1,))
t= t_1 - 0.8
m = len(t)
sp = np.fft.fft(t)
amp= np.sqrt(sp.real**2+sp.imag**2)*2/m
freq = np.fft.fftfreq(m,0.01)
plt.plot(freq, amp)
plt.xlim([0,0.4])
#[<matplotlib.lines.Line2D object at 0x...>, <matplotlib.lines.Line2D object at 0x...>]
plt.show()
