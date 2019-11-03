#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on:   Sat Nov  2 14:41:15 CET 2019
#
# Author(s):    Francesco Urbani <https://urbanij.github.io>
#
# Description:  Empty unit test for traveling_wave_1.py
# 
# ==========================================================

import unittest

from traveling_wave_1 import *
from functions import *

class TravelingWaveTest(unittest.TestCase):

    def test_gamma_tau(self):
        self.assertEquals(1+gamma(2,5), tau(2,5))
        self.assertEquals(1+gamma(-3,7), tau(-3,7))
        


if __name__ == "__main__":
    unittest.main()
