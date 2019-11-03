#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on:   Sun Nov  3 19:03:45 CET 2019
#
# Author(s):    Francesco Urbani <https://urbanij.github.io>
#
# File          functions.py
# Description:  Ex. Jan 27 201something
# 
#
# ==========================================================
import scipy.constants
import numpy as np

cdef float epsilon_0 = scipy.constants.epsilon_0
cdef float mu_0 = scipy.constants.mu_0


cpdef epsilon_eq(float epsilon_r, float omega, float sigma):
    """
    electric constant [F/m]

    Parameters
    ----------
    epsilon_r : integer > 1 
    omega   : angular frequency [rad/s]
    sigma   : conductivity [S/m]
    Returns
    """
    return epsilon_0 * epsilon_r * (1 + sigma/(1j*omega*epsilon_0*epsilon_r)) 

cpdef mu_eq(float mu_r):
    """
    magnetic constant [H/m]
    """
    return mu_0 * mu_r                          

cpdef zeta(complex epsilon_eq, float mu_eq):   
    """
    characteristic impedance [Ω]
    epsilon_eq:   
    """
    return np.sqrt(mu_eq/epsilon_eq)

cpdef k(float mu_eq, complex epsilon_eq, float omega):   
    """
    wavenumber [1/m]
    """
    return omega * np.sqrt(mu_eq * epsilon_eq)           

cpdef v(complex epsilon_eq, float mu_eq):   
    """
    signal velocity [m/s]
    """
    return (1/np.sqrt(epsilon_eq*mu_eq)).real        

cpdef Lambda(float f, complex epsilon_eq, float mu_eq):
    """
    wavelength [m]
    """
    return v(epsilon_eq,mu_eq)/f                     

cpdef gamma(complex zeta_2, complex zeta_1):   
    """
    reflection coefficient
    """
    return (zeta_2-zeta_1)/(zeta_2+zeta_1)

cpdef tau(complex zeta_2, complex zeta_1):   
    """
    transmission coefficient
    """
    return 2*zeta_2/(zeta_2+zeta_1)

