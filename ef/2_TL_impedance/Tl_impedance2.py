#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on:   Tue Nov 12 20:17:41 CET 2019
#
# Author(s):    Francesco Urbani
#
# File          
# Description:  
# 
# ==========================================================
 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider  # import the Slider widget
 
k = .71
 
ZL_min  = 1e-3      # the minimial value of the paramater a
ZL_max  = np.log(10_000)      # the maximal value of the paramater a
ZL_init = np.log(50)    # the value of the parameter a to be used initially, when the graph is created
 
z = np.linspace(-10, 0, 5_000)
 
def Z(ZL, Z0=50): 
    # dealing with edge cases first
    if ZL == 0:                     # short circuit
        return -1j*Z0*np.tan(k*z)
    elif ZL > 100*Z0:               # i.e. ZL -> +inf (open circuit)
        return 1j*Z0* (1/np.tan(k*z)) 
    return Z0 * (ZL + 1j*Z0*np.tan(k*z)/(Z0 + 1j*ZL*np.tan(k*z)))
 
 
def gamma(ZL,Z0,z):
    def _gamma0(zl,z0=50):
        return (zl-z0)/(zl+z0)
    return _gamma0(ZL,Z0)*np.exp(1j*2*k*z)
 
def V(ZL, Z0=50):
    return np.exp(-1j*k*z) * (1 + gamma(ZL,Z0,z))
 
fig = plt.figure(figsize=(8,6))
 
# first we create the general layout of the figure
# with two axes objects: one for the plot of the function
# and the other for the slider
sin_ax = plt.axes([0.1, 0.2, 0.8, 0.65])
slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])
 
 
 
# in plot_ax we plot the function with the initial value of the parameter a
plt.axes(sin_ax) # select sin_ax
plt.title('V(z) @ $Z_0$=50 $\Omega$')
v_plot, = plt.plot(z, abs(V(ZL_init)), 'r')
 
 
 
plt.xlim(z[0], z[-1])
plt.ylim(-.2, 2.2)
plt.grid(True)
 
# here we create the slider
ZL_slider = Slider(slider_ax,      # the axes object containing the slider
                  '$log(Z_L)$',    # the name of the slider parameter
                  ZL_min,          # minimal value of the parameter
                  ZL_max,          # maximal value of the parameter
                  valinit=ZL_init  # initial value of the parameter
                 )
 
# Next we define a function that will be executed each time the value
# indicated by the slider changes. The variable of this function will
# be assigned the value of the slider.
def update(ZL_slider):
    v_plot.set_ydata(abs(V(np.exp(ZL_slider)))) # set new y-coordinates of the plotted points
    fig.canvas.draw_idle()          # redraw the plot
 
# the final step is to specify that the slider needs to
# execute the above function when its value changes
ZL_slider.on_changed(update)
 
plt.show()

