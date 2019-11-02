#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on:   Sat Nov  2 11:32:55 CET 2019
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
# ζ_0 = scipy.constants.physical_constants['characteristic impedance of vacuum'][0]
π = np.pi
ε_0 = scipy.constants.epsilon_0

### ******************
###     functions
### ******************

ζ    = lambda ε_eq, μ_eq:    np.sqrt(μ_eq/ε_eq)
μ_eq = lambda μ_r:           scipy.constants.mu_0 * μ_r
ε_eq = lambda ε_r, ω, σ:     ε_0 * ε_r * (1 - 1j*σ/(ω*ε_0))
k    = lambda μ_eq, ε_eq:    ω * np.sqrt(μ_eq * ε_eq)

λ    = lambda f, ε_eq, μ_eq: (1/np.sqrt(ε_eq*μ_eq))/f
v    = lambda ε_eq, μ_eq:    (1/np.sqrt(ε_eq*μ_eq))

### ******************
###     data
### ******************

E_0   = 6       # [V]
f     = 1e9     # [Hz]

ε_r_1 = 1
ε_r_2 = 3
μ_r_1 = 1
μ_r_2 = 1
σ     = 0.0012  # [S/m]

### ******************
###    relations
### ******************

ω = 2*π*f   # [rad/s]
T = 1/f     # [s]



### ******************
###    computations
### ******************

material_type = 'Good conductor' if σ/(ω*ε_0*ε_r_2)  >= 100                           else \
                'dielectric'     if σ/(ω*ε_0*ε_r_2) < 100 and σ/(ω*ε_0*ε_r_2 >= 0.01) else \
                'Insulator'
print(f"σ/(ω*ε_0*ε_r_2) = {σ/(ω*ε_0*ε_r_2)}  ==> \033[92m{material_type}\x1b[0m")


ε_eq_1 = ε_0 * ε_r_1
ε_eq_2 = ε_eq(ε_r_2, ω, σ)

μ_eq_1 = μ_eq(μ_r_1)
μ_eq_2 = μ_eq(μ_r_2)

ζ_1 = ζ(ε_eq_1, μ_eq_1)
ζ_2 = ζ(ε_eq_2, μ_eq_2)    # [ohm]

k_1 = k(μ_eq_1, ε_eq_1)
k_2 = k(μ_eq_2, ε_eq_2)


Γ_e = (ζ_2-ζ_1)/(ζ_2+ζ_1)
τ_e   = 1 + Γ_e


if material_type == 'conductor':
    print("*"*3)
    print("\tapprox results (good conductor material):")
    δ = np.sqrt(2/(ω*μ_eq_2*σ))
    k_2 = (1/δ)*(1-1j)
    ζ_2 = (1/(σ*δ))*(1+1j)
    print(f"\tdelta = {δ}")
    print(f"\tk_2 = {(1/δ)}·(1-j)")
    print(f"\tζ_2 = {(1/(σ*δ))}·(1+j)")
    print("*"*3)

β =  k_2.real  # 
α = -k_2.imag  # damping coefficient


print(f"μ_eq_1 = {μ_eq_1}")
print(f"μ_eq_2 = {μ_eq_2}")
print(f"ε_eq_1 = {ε_eq_1}")
print(f"ε_eq_2 = {ε_eq_2}")

print(f"ζ_1 = {ζ_1}")
print(f"ζ_2 = {ζ_2}")

print(f"k_1 = {k_1}")
print(f"k_2 = {k_2}")

print(f"Γ_e = {abs(Γ_e)} ∠ {np.angle(Γ_e)}")
print(f"τ_e = {abs(τ_e)} ∠ {np.angle(τ_e)}")

# 
# breakpoint()

d_neg = -3*λ(f, ε_eq_1, μ_eq_1)

try:
    δ = np.sqrt(2/(ω*μ_eq_2*σ))
    print(f"~delta~ = {δ}")
    d_pos = 5*δ + 0.1 * -d_neg/3  # 5 delta + 10 % λ_1
except RuntimeWarning:
    pass
except ZeroDivisionError:
    d_pos = 3*λ(f, ε_eq_2, μ_eq_2)
d_pos = d_pos.real



λ_1   = λ(f, ε_eq_1, μ_eq_1)
v_1   = v(ε_eq_1, μ_eq_1)

t     = np.linspace(0, 2*λ_1/v_1, 80)
z_neg = np.linspace(d_neg, 0, 400, endpoint=False)
z_pos = np.linspace(0, d_pos, 400, endpoint=False)
z     = z_neg + z_pos

e1_i   = lambda z, t: (      E_0 * np.exp(-1j*k_1*z) * np.exp(1j*ω*t)).real * (0.5 * (np.sign(-z) +1))
e1_r   = lambda z, t: (Γ_e * E_0 * np.exp(+1j*k_1*z) * np.exp(1j*ω*t)).real * (0.5 * (np.sign(-z) +1))
e2_t   = lambda z, t: (τ_e * E_0 * np.exp(-1j*k_2*z) * np.exp(1j*ω*t)).real * (0.5 * (np.sign(+z) +1))
e1_tot = lambda z, t: (e1_i(z,t) + e1_r(z, t)) * (0.5 * (np.sign(-z) +1))


S_i = 0.5 * 1/ζ_1 * abs(E_0)**2
S_t = S_i * (1-(abs(Γ_e))**2)

print(f"S_i = {S_i}")
print(f"S_t = {S_t}")


E_max_over_E_min = lambda E_max, E_min : E_max/E_min

E_max_1 = max(e1_tot(0, t))
E_min_1 = min(abs(e1_tot(0, t)))
E_max_2 = max(e2_t(0, t))
E_min_2 = min(abs(e2_t(0, t)))


print(f"E_max_over_E_min_1 = {E_max_1}/{E_min_1} = {E_max_over_E_min(E_max_1, E_min_1)}")
print(f"E_max_over_E_min_2 = {E_max_2}/{E_min_2} = {E_max_over_E_min(E_max_2, E_min_2)}")


# exit(0)     #### comment this out to just show the results and avoid plotting
# breakpoint()


if __name__ == '__main__':
        
    fig = plt.figure(1)
    fig.set_dpi(100)


    def animate(i):
        plt.clf()
        plt.title("Traveling wave, interface @ z = 0" + \
            "\nmedium 1: z<0, $\epsilon_r$=" + str(ε_r_1)+", $\mu_r$="+str(μ_r_1) + \
            "\nmedium 2: z>0, $\epsilon_r$=" + str(ε_r_2)+ ", $\mu_r$=" + str(μ_r_2) + ", $\sigma$ =" + str(σ)
        )
        plt.plot(z_neg, e1_i(z_neg, t[i]),  color='blue',   label='$e_1^i(z,t)|_{z=z_0}$',    linewidth=1.0)
        plt.plot(z_neg, e1_r(z_neg, t[i]),  color='red',    label='$e_1^r(z,t)|_{z=z_0}$',    linewidth=1.0)
        plt.plot(z_neg, e1_tot(z_neg, t[i]),color='green',  label='$e_1^{tot}(z,t)|_{z=z_0}$',linewidth=1.0)
        plt.plot(z_pos, e2_t(z_pos, t[i]),  color='orange', label='$e_2^t(z,t)|_{z=z_0}$',    linewidth=1.0)
        plt.xlabel('space (z)')
        plt.ylabel('E [V/m]')
        plt.legend(loc='upper right')
        plt.grid(True)
        e1_max_swing = 2*E_0 #max(abs(e1_i(z,0)) + abs(e1_r(z,0)))
        plt.ylim([-e1_max_swing, e1_max_swing])
        plt.xlim([d_neg, d_pos])


    anim = animation.FuncAnimation(fig, animate, frames=60, interval=20)
    plt.show()

    ### Save animation
    # Writer = animation.writers['ffmpeg']
    # writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    # anim.save('media/traveling_wave_1.mp4', writer=writer, dpi=200)


