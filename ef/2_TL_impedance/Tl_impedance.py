#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
# Created on:   Tue Nov 12 20:17:41 CET 2019
#
# Author(s):    Francesco Urbani <https://urbanij.github.io>
#
# File          
# Description:  
# 
# ==========================================================

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation


Z0 = 50
k = .96

num_load_cases = 100
Z_L = np.linspace(0,4*Z0, num_load_cases)

num_points = 2_000
z = np.linspace(-8, 0, num_points)


def Z(Z0=50, ZL=50): 
    return Z0 * (ZL + 1j*Z0*np.tan(k*z)/(Z0 + 1j*ZL*np.tan(k*z)))


fig = plt.figure(figsize=(10,8))
fig.set_dpi(100)
def animate(i):
    plt.clf()
    plt.title("Z(z)/$Z_0$")
    plt.plot(z, Z(Z0, Z_L[i])/Z0, label="$Z_L/Z_0$ = " + f"{Z_L[i]/Z0:.3g}")
    plt.xlabel('space (z)')
    plt.ylabel('Z(z)/$Z_0$')
    plt.legend(loc='upper right')
    plt.xlim([z[0], z[-1]])
    plt.grid(True)   
anim = animation.FuncAnimation(fig, animate, frames=num_load_cases, interval=10)


plt.show()

