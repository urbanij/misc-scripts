#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on:   Sat Nov  2 21:12:21 CET 2019
#
# Author(s):    Francesco Urbani <https://urbanij.github.io>
# Description:  Ex. Jan 27 201something
# 
# ==========================================================

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import scipy.constants

### ******************
###     constants
### ******************
π   = np.pi
ε_0 = scipy.constants.epsilon_0
μ_0 = scipy.constants.mu_0
ζ_0 = scipy.constants.physical_constants['characteristic impedance of vacuum'][0]

### ******************
###     functions
### ******************

ζ    = lambda ε_eq, μ_eq:    np.sqrt(μ_eq/ε_eq)                 # characteristic impedance [Ω]
μ_eq = lambda μ_r:           μ_0 * μ_r                          # magnetic constant [H/m]
ε_eq = lambda ε_r, ω, σ:     ε_0 * ε_r * (1 + σ/(1j*ω*ε_0*ε_r)) # electric constant [F/m]
k    = lambda μ_eq, ε_eq:    ω * np.sqrt(μ_eq * ε_eq)           # wavenumber [1/m]

v    = lambda ε_eq, μ_eq:    (1/np.sqrt(ε_eq*μ_eq)).real        # signal velocity [m/s]
λ    = lambda f, ε_eq, μ_eq: v(ε_eq,μ_eq)/f                     # wavelength [m]
Γ    = lambda ζ_2, ζ_1:      (ζ_2-ζ_1)/(ζ_2+ζ_1)                # reflection coefficient


### ******************
###     data
### ******************
f     = 1.8e9   # [Hz]
E_0   = 10      # [V]
ε_r_1 = 1
μ_r_1 = 1
σ_1   = 0       # [S/m]
ε_r_2 = 1.15
μ_r_2 = 1
σ_2   = 23  # [S/m]
### ******************

try:
    while 1:
        _ = float(input(f"Insert f [Hz]: (or enter to use default value {f:.4g}) "))
        if _ > 0: f = _; break
except Exception as e:
    print(f"Using default: f = {f:.4g}")

try:
    while 1:
        _ = float(input(f"Insert E_0 [V]: (or enter to use default value {E_0:.4g}) "))
        if _ > 0: E_0 = _; break
except Exception as e:
    print(f"Using default: E_0 = {E_0:.4g}")

try:
    while 1:
        _ = float(input(f"Insert ε_r_1: (or enter to use default value {ε_r_1:.4g}) "))
        if _ >= 1: ε_r_1 = _; break
except Exception as e:
    print(f"Using default: ε_r_1 = {ε_r_1:.4g}")

try:
    while 1:
        _ = float(input(f"Insert μ_r_1: (or enter to use default value {μ_r_1:.4g}) "))
        if _ >= 1: μ_r_1 = _; break
except Exception as e:
    print(f"Using default: μ_r_1 = {μ_r_1:.4g}")

try:
    while 1:
        _ = float(input(f"Insert σ_1: (or enter to use default value {σ_1:.4g}) "))
        if _ >= 0: σ_1 = _; break
except Exception as e:
    print(f"Using default: σ_1 = {σ_1:.4g}")

try:
    while 1:
        _ = float(input(f"Insert ε_r_2: (or enter to use default value {ε_r_2:.4g}) "))
        if _ >= 1: ε_r_2 = _; break
except Exception as e:
    print(f"Using default: ε_r_2 = {ε_r_2:.4g}")

try:
    while 1:
        _ = float(input(f"Insert μ_r_2: (or enter to use default value {μ_r_2:.4g}) "))
        if _ >= 1: μ_r_2 = _; break
except Exception as e:
    print(f"Using default: μ_r_2 = {μ_r_2:.4g}")

try:
    while 1:
        _ = float(input(f"Insert σ_2: (or enter to use default value {σ_2:.4g}) "))
        if _ >= 0: σ_2 = _; break
except Exception as e:
    print(f"Using default: σ_2 = {σ_2:.4g}")


### ******************
###    relations
### ******************

ω = 2*π*f   # [rad/s]
T = 1/f     # [s]


### ******************
###    computations
### ******************

material_type = 'Good conductor' if σ_2/(ω*ε_0*ε_r_2) >= 100                              else \
                'Dielectric'     if σ_2/(ω*ε_0*ε_r_2) < 100 and σ_2/(ω*ε_0*ε_r_2 >= 0.01) else \
                'Insulator'
print()
print("*"*20)
print(f"σ_2/(ω*ε_0*ε_r_2) = {σ_2/(ω*ε_0*ε_r_2):.4g}  ==> medium 2 is a(n) \033[92m{material_type}\x1b[0m")


ε_eq_1 = ε_eq(ε_r_1, ω, σ_1)
ε_eq_2 = ε_eq(ε_r_2, ω, σ_2)

μ_eq_1 = μ_eq(μ_r_1)
μ_eq_2 = μ_eq(μ_r_2)

ζ_1 = ζ(ε_eq_1, μ_eq_1)
ζ_2 = ζ(ε_eq_2, μ_eq_2)

k_1 = k(μ_eq_1, ε_eq_1)
k_2 = k(μ_eq_2, ε_eq_2)


Γ_e = Γ(ζ_2, ζ_1)
τ_e = 1 + Γ_e


if material_type == 'Good conductor':
    print("*"*3)
    print("\tapprox results (good conductor material):")
    δ = np.sqrt(2/(ω*μ_eq_2*σ_2))
    k_2 = (1/δ)*(1-1j)
    ζ_2 = (1/(σ_2*δ))*(1+1j)
    print(f"\tδ = {δ:.4g}")
    print(f"\tk_2 = {(1/δ):.4g}·(1-j)")
    print(f"\tζ_2 = {(1/(σ_2*δ)):.4g}·(1+j)")
    print("*"*3)

β =  k_2.real  # 
α = -k_2.imag  # damping coefficient   # k := β - j*α


print(f"μ_eq_1 = {μ_eq_1:.4g}")
print(f"μ_eq_2 = {μ_eq_2:.4g}")
print(f"ε_eq_1 = {ε_eq_1:.4g}")
print(f"ε_eq_2 = {ε_eq_2:.4g}")

print(f"ζ_1 = {ζ_1:.4g}")
print(f"ζ_2 = ζ_0·({ζ_2/ζ_0:.4g}) = {ζ_2:.4g}")

print(f"k_1 = {k_1:.4g}")
print(f"k_2 = {k_2:.4g}")

print(f"Γ_e = {abs(Γ_e):.4g} ∠ {np.angle(Γ_e):.4g}")
print(f"τ_e = {abs(τ_e):.4g} ∠ {np.angle(τ_e):.4g}")



λ_1   = λ(f, ε_eq_1, μ_eq_1)
v_1   = v(ε_eq_1, μ_eq_1)
print(f"λ_1 = {λ_1:.4g}")
print(f"v_1 = {v_1:.4g}")



z_neg = np.linspace(-.5, 0, 400, endpoint=False)
z_pos = np.linspace(0, .5, 400,  endpoint=False)
z     = z_neg + z_pos
t     = np.linspace(-0.2e-9, 1.2e-9, 100)


def cosine(k, z, t, A=E_0):
    return E_0 * np.cos(ω*t + k*z)
    # return A * np.exp(1j*k*z) 

# def windowed_cosine(k, z):
#     return cosine(k, z)

def gaussian(k, z, t, rms=0.20, A=E_0):
    return A * 1/np.sqrt(2*π*rms**2) * np.exp(-((ω*t + k*z)**2)/(2 * rms**2))



### ****     Capitalized == phasor         ****

ei = cosine
# E1_i = cosine 
# E1_i = windowed_cosine
# E1_i   = lambda k, z, t : E_0 * (np.heaviside(ω*t + k*(z+.3), 0) - np.heaviside(ω*t + k*(z+.1), 0))



e1_i   = lambda z, t: (      ei(k_1, -z, t))
e1_r   = lambda z, t: (Γ_e * ei(k_1, +z, t))
e2_t   = lambda z, t: (τ_e * ei(k_2, -z, t))
e1_tot = lambda z, t: e1_i(z,t) + e1_r(z, t)



S_i = 0.5 * 1/ζ_1 * abs(E_0)**2
S_t = S_i * (1-(abs(Γ_e))**2)

print(f"S_i = {S_i:.4g}")
print(f"S_t = {S_t:.4g} = {100*S_t/S_i:.4g}% S_i")


E_max_over_E_min = lambda E_max, E_min : E_max/E_min



if __name__ == '__main__':

    if input("Want to plot? ([y]/n)? ") != 'n': 

        fig = plt.figure(figsize=(10,8))
        fig.set_dpi(100)


        def animate(i):
            plt.clf()
            plt.title("Traveling wave, interface @ z = 0" + \
                "\nmedium 1: z<0, $\epsilon_r$=" + str(ε_r_1) + ", $\mu_r$=" + str(μ_r_1) + ", $\sigma$ =" + str(σ_1) + \
                "\nmedium 2: z>0, $\epsilon_r$=" + str(ε_r_2) + ", $\mu_r$=" + str(μ_r_2) + ", $\sigma$ =" + str(σ_2)
            )
            plt.plot(z_neg, e1_i(z_neg, t[i]),   "--", color='blue',   label='$e_1^i(z,t)|_{z=z_0}$',     linewidth=1)
            plt.plot(z_neg, e1_r(z_neg, t[i]),   "-.", color='red',    label='$e_1^r(z,t)|_{z=z_0}$',     linewidth=1)
            plt.plot(z_neg, e1_tot(z_neg, t[i]), "-",  color='green',  label='$e_1^{tot}(z,t)|_{z=z_0}$', linewidth=1)
            plt.plot(z_pos, e2_t(z_pos, t[i]),   "-",  color='orange', label='$e_2^t(z,t)|_{z=z_0}$',     linewidth=1)
            
            plt.xlabel('space (z)')
            plt.ylabel('E [V/m]')
            plt.legend(loc='upper right')
            plt.grid(True)
            
            plt.ylim([-2*E_0, 2*E_0])
            plt.xlim([min(z), max(z)])

            print(i)
            breakpoint()

        anim = animation.FuncAnimation(fig, animate, frames=40, interval=20)

        if input("Want to save plot animation? (y/[n])? ") == 'y': 
            ### Save animation
            Writer = animation.writers['ffmpeg']
            writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
            anim.save('media/traveling_wave_1.mp4', writer=writer, dpi=200)
        else:
            plt.show()

