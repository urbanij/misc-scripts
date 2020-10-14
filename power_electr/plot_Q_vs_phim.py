#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Thu Apr  2 13:39:20 CEST 2020
# 
# Author(s):    Francesco Urbani
# Description:  
# 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#style.use("ggplot")
style.use("dark_background")

ε = 1e-9
PI = np.pi

phi_m = np.linspace(ε, PI/2-ε, 500)
Q = (np.cos(phi_m))**0.5 / np.sin(phi_m)


plt.figure()#num='This is the title')
plt.title("Closed-loop Q vs. Phase margin")
plt.grid(color='#9c9b97', linestyle='-.', linewidth=0.2)
plt.xlim(0,np.pi/2)
plt.ylim(-30,30)

plt.plot(phi_m, 10*np.log(Q), linewidth=0.8, label="$Q_{dB}$", color='#f0ef51')

plt.xlabel("$\phi_m$")
plt.ylabel("$Q(\phi_m)|_{dB}$")
plt.legend()

plt.show()
