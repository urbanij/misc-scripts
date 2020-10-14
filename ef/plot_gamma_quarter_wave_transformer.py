#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Wed Jul 08 08:41:07 AM CEST 2020
# 
# Author(s):    Francesco Urbani
# Description:  
# 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#style.use("ggplot")
style.use("dark_background")

c = 3e8

Z0 = 50
Rl = 20

f = 100e6


Zx = (Z0 * Rl)**0.5
Lambda = c/f
beta = 2*np.pi/Lambda

z = np.linspace(0, -0.25*Lambda, 100)
Z = Zx * (Rl + 1j*Zx*np.tan(beta*z))/(Zx + 1j*Rl*np.tan(beta*z))

Gamma = (Z-Z0)/(Z+Z0)
#print(Gamma)

fig,ax = plt.subplots()
ax.scatter(Gamma.real, Gamma.imag)


#plt.figure(num='This is the title')

plt.title("Title")
plt.grid(color='#9c9b97', linestyle='-.', linewidth=0.2)
#plt.plot(z, Gamma, label='$y(x)$', linewidth=0.8, color='#f0ef51')

#plt.xlim(-12,12)
#plt.ylim(-1,4)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.show()
