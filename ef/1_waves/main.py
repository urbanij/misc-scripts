#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
# Created on:   Tue Nov 26 19:54:11 CET 2019
#
# Author(s):    Francesco Urbani <https://urbanij.github.io>
#
# File          main.py
# Description:  Ex. Jan 27 201something
# 
# ==========================================================

from wave import Medium, Sine, Gaussian, Rect


if __name__ == '__main__':

    f_0     = 1.8e9 # [Hz]
    E_0     = 10.0  # [V]

    free_space = Medium(ε_r=1, μ_r=1, σ=0)

    

    medium2 = Medium(ε_r=1, μ_r=1, σ=0)       # vacuum
    medium2 = Medium(ε_r=5, μ_r=3, σ=.04)
    # medium2 = Medium(ε_r=9, μ_r=1, σ=.1)     
    # medium2 = Medium(ε_r=3, μ_r=1, σ=0.35)


    wave = Sine(f=f_0, A=E_0)

    # wave = Gaussian(rms=1.3)
    
    # wave = Rect(width=4)


    wave.add_mediums(medium1=free_space, medium2=medium2)
    wave.print_data()
    wave.show()

