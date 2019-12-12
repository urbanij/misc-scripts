#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
# Created on:   Sun Nov  3 19:03:45 CET 2019
#
# Author(s):    Francesco Urbani <https://urbanij.github.io>
#
# File          functions_py.py
# Description:  Ex. Jan 27 201something
# 
#
# ==========================================================
import scipy.constants
import numpy as np

epsilon_0 = scipy.constants.epsilon_0
mu_0 = scipy.constants.mu_0


def epsilon_eq(epsilon_r, omega, sigma):
    """
    electric constant [F/m]

    Parameters
    ----------
    epsilon_r : integer > 1 
    omega     : angular frequency   [rad/s]
    sigma     : conductivity        [S/m]
    Returns
    """
    return epsilon_0 * epsilon_r * (1 + sigma/(1j*omega*epsilon_0*epsilon_r)) 

def mu_eq(mu_r):
    """
    magnetic constant [H/m]
    """
    return mu_0 * mu_r                          

def zeta(epsilon_eq, mu_eq):   
    """
    characteristic impedance [Ω]
    epsilon_eq:   
    """
    return np.sqrt(mu_eq/epsilon_eq)

def k(mu_eq, epsilon_eq, omega):   
    """
    wavenumber [1/m]
    """
    return omega * np.sqrt(mu_eq * epsilon_eq)           

def v(epsilon_eq, mu_eq):   
    """
    signal velocity [m/s]
    """
    return (1/np.sqrt(epsilon_eq*mu_eq)).real        

def Lambda(f, epsilon_eq, mu_eq):
    """
    wavelength [m]
    """
    return v(epsilon_eq,mu_eq)/f                     

def gamma(zeta_2, zeta_1):   
    """
    reflection coefficient
    """
    return (zeta_2-zeta_1)/(zeta_2+zeta_1)

def tau(zeta_2, zeta_1):   
    """
    transmission coefficient
    """
    return 2*zeta_2/(zeta_2+zeta_1)

