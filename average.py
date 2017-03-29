#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

t = np.loadtxt("./dock_motion.txt", usecols=(0,))
h = np.loadtxt("./dock_motion.txt", usecols=(3,))
#h = np.loadtxt("./surfaceElevation.dat", usecols=(2,))
index = t>150
heave=h[index]

n = len(heave)
a=[]
d=[]
b =0
c =0
for i in range(1,n-1):
    if(heave[i]>heave[i-1] and heave[i]>heave[i+1]):
        a.append(heave[i])
        b = b+1

for i in range(1,n-1):
    if(heave[i]<heave[i-1] and heave[i]<heave[i+1]):
        d.append(heave[i])
        c= c+1
lengthMax = len(a)
lengthMin = len(d)

if (lengthMax != lengthMin):
    e = min(lengthMin,lengthMax)
else: 
    e = lengthMax
f=[]
for i in range (0,e):
    i = a[i]-d[i]
    f.append(i)
g = sum(f)/len(f)

print g
