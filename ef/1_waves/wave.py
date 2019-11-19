#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on:   Sat Nov  2 11:32:55 CET 2019
#
# Author(s):    Francesco Urbani <https://urbanij.github.io>
#
# File          wave.py
# Description:  Ex. Jan 27 201something
# 
# ==========================================================

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import scipy.constants

# from functions import *
from functions_py import *

### ******************
###     constants
### ******************
π = np.pi
ε_0 = scipy.constants.epsilon_0
ζ_0 = scipy.constants.physical_constants['characteristic impedance of vacuum'][0]

### ******************
###     data
### ******************
f       = 1.8e9 # [Hz]
E_0     = 10.0  # [V]
ε_r_1   = 1.0
μ_r_1   = 1.0
σ_1     = 0.0   #[S/m]
ε_r_2   = 1.5
μ_r_2   = 1.0
σ_2     = 0.12  # [S/m]
wave    = 'cosine'
### ******************

if __name__ == '__main__':
    try:
        while 1:
            _ = float(input(f"Insert f [Hz]: (or enter to use default value {f:.4g}) "))
            if _ > 0: f = _; break
    except Exception as e:
        print(f"Using default: f = {f:.4g}")
    except UnboundLocalError: pass

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

    try:
        _ = input("Insert wave: cosine / gaussian / rectangular pulse ([c]/g/r)? ")
        if   _ == 'c': wave = "cosine"
        elif _ == 'g': wave = "gaussian"
        elif _ == 'r': wave = "rect"
    except Exception as e:
        print(f"Using default: cosine wave")
        wave = "cosine"

### ******************
###    relations
### ******************

ω = 2 * π * f  # [rad/s]

### ******************
###    computations
### ******************
U = σ_2 / (ω * ε_0 * ε_r_2)
material_type = 'Good conductor' if (U >= 1e2) else \
    'Dielectric' if (U < 1e2 and U >= 1e-2) else \
        'Insulator'

print("*"*20)
print(f"σ_2/(ω*ε_0*ε_r_2) = {U:.4g}  ==> medium 2 is a(n) \033[92m{material_type}\x1b[0m")

ε_eq_1 = epsilon_eq(ε_r_1, ω, σ_1)
ε_eq_2 = epsilon_eq(ε_r_2, ω, σ_2)

μ_eq_1 = mu_eq(μ_r_1)
μ_eq_2 = mu_eq(μ_r_2)

ζ_1 = zeta(ε_eq_1, μ_eq_1)
ζ_2 = zeta(ε_eq_2, μ_eq_2)

k_1 = k(μ_eq_1, ε_eq_1, ω)
k_2 = k(μ_eq_2, ε_eq_2, ω)

Γ_e = gamma(ζ_2, ζ_1)
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

β = k_2.real  # 
α = k_2.imag  # damping coefficient   # k := β + j*α  , (α < 0)


print(f"μ_eq_1 = {μ_eq_1:.4g}")
print(f"μ_eq_2 = {μ_eq_2:.4g}")
print(f"ε_eq_1 = {ε_eq_1:.4g}")
print(f"ε_eq_2 = {ε_eq_2:.4g}")

print(f"ζ_1 = {ζ_1:.4g}")
print(f"ζ_2 = ζ_0·({ζ_2/ζ_0:.4g}) = {ζ_2:.4g}")

print(f"k_1 = {k_1:.4g}")
print(f"k_2 = {k_2:.4g}")

print(f"Γ_e = {Γ_e:.4g} = {abs(Γ_e):.4g} ∠ {np.angle(Γ_e):.4g}")
print(f"τ_e = {τ_e:.4g} = {abs(τ_e):.4g} ∠ {np.angle(τ_e):.4g}")



d_neg = -3*Lambda(f, ε_eq_1, μ_eq_1)   # show 3 wavelength before the discontinuity

try:
    δ = -1/α # skin depth
    d_pos = 5*δ + 0.1 * -d_neg/3  # 5 delta + 10 % λ_1
except ZeroDivisionError as e:
    print(e)
else:
    print(f"δ = {δ:.4g}")
    if abs(δ) == np.inf:
        d_pos = -d_neg  # λ_1

d_pos = d_pos.real # just to make sure...


λ_1   = Lambda(f, ε_eq_1, μ_eq_1)
v_1   = v(ε_eq_1, μ_eq_1)
print(f"λ_1 = {λ_1:.4g}")
print(f"v_1 = {v_1:.4g}")



z_neg = np.linspace(d_neg, 0, 400, endpoint=True)
z_pos = np.linspace(0, d_pos, 400, endpoint=True)
z     = z_neg + z_pos


frames = 80
t1    = np.linspace(0, λ_1/v_1, frames)
t2    = np.linspace(-1e-9, 1.3e-9, frames)
t3    = np.linspace(-2e-9, 2e-9, frames)


# E1_i   = lambda k, z, t: E_0 * np.exp(1j*k*z) * np.exp(1j*ω*t)
def cosine(k, z, t):
    return  E_0 * np.exp(1j*k*z) * np.exp(1j*ω*t)

def windowed_cosine(k, z, t):
    window = 3
    return  cosine(k, z, t) * (np.heaviside(ω*t + k.real*z+window,1e-6) - np.heaviside(ω*t + k.real*z-window, 1e-6))

def gaussian(k, z, t, rms=1.20, A=E_0):
    return A * 1/np.sqrt(2*π*rms**2) * np.exp(-((ω*t + k.real*z)**2)/(2 * rms**2)) * np.exp(-k.imag*z)

def rect(k, z, t):
    window = 3
    return (np.heaviside(ω*t + k.real*z+window,1e-6) - np.heaviside(ω*t + k.real*z-window, 1e-6)) * np.exp(-k.imag*z)


if wave == 'cosine':
    E1_i = cosine
elif wave == 'gaussian':
    E1_i = gaussian
elif wave == 'rect':
    E1_i = rect
else:
    raise Exception("Invalid wave")

t = t2 if E1_i == gaussian else t3 if E1_i == rect else t1


e1_i   = lambda z, t: (      E1_i(k_1, -z, t)).real 
e1_r   = lambda z, t: (Γ_e * E1_i(k_1, +z, t)).real
e2_t   = lambda z, t: (τ_e * E1_i(k_2, -z, t)).real
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
            plt.plot(z_neg, e1_i(z_neg, t[i]),   "--", color='blue',   label='$e_1^i(z,t)$',     linewidth=1)
            plt.plot(z_neg, e1_r(z_neg, t[i]),   "-.", color='red',    label='$e_1^r(z,t)$',     linewidth=1)
            plt.plot(z_neg, e1_tot(z_neg, t[i]), "-",  color='green',  label='$e_1^{tot}(z,t)$', linewidth=1.5)
            plt.plot(z_pos, e2_t(z_pos, t[i]),   "-",  color='orange', label='$e_2^t(z,t)$',     linewidth=1.5)
            
            plt.xlabel('space (z)')
            plt.ylabel('E [V/m]')
            plt.legend(loc='upper right')
            plt.grid(True)
            
            
            if wave == "gaussian":
                peak_high=max(e1_tot(z, t[0]))
                peak_low=min(e1_tot(z, t[40]))
            elif wave == "cosine":
                peak_high=max(e1_tot(z, t[0]))
                peak_low=-peak_high
            else:
                peak_high=max(e1_tot(z, t[2]))
                peak_low=min(e1_tot(z, t[40]))

            plt.ylim([1.6*peak_low, 1.6*peak_high])
            plt.xlim([d_neg, d_pos])

        anim = animation.FuncAnimation(fig, animate, frames=frames, interval=10)

        if input("Want to save plot animation? (y/[n])? ") == 'y': 
            ### Save animation
            Writer = animation.writers['ffmpeg']
            writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
            anim.save('media/traveling_wave_1.mp4', writer=writer, dpi=200)
        else:
            plt.show()
