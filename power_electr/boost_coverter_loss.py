#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on:   Wed Mar 18 11:47:56 CET 2020
#
# Author(s):    Francesco Urbani <https://urbanij.github.io>
#
# File          
# Description:  
# 
# ==========================================================

import numpy as np
import matplotlib.pyplot as plt


D = np.linspace(0, 0.999, 200)

# R = 1000          # load
# R_L = 5           # inductor's 
# R_d = 5           # diode's
# V_gamma = 0.7     # diode's
# R_on = 5          # mosfet's
# Vd = 0.6          # 


def vo_over_vd(R_L=1000, R_d=5, R_on=4, V_gamma=0.7, Vd=0.6):
    return (1-D) * (1 - (1-D) * V_gamma/Vd)/(1 + ((R_L + R_on*D + R_d*(1-D))/(1-D)**2))

def eta(R_L=1000, R_d=5, R_on=4, V_gamma=0.7, Vd=0.6):
    return (1 - (V_gamma*(1-D))/(Vd))/(1 + (R_L + R_on*D + R_d*(1-D))/(1-D)**2)


R_L = np.array([200, 500, 1000])
for rl in R_L:
    plt.plot(D, vo_over_vd(R_L=rl, R_d=5, R_on=4, V_gamma=0.7, Vd=0.6), color="red", linewidth=rl/1000, label=f"$R_L = {rl}$")

# plt.plot(D, eta, label="eta", color='green')
plt.grid()
plt.legend()
plt.show()


