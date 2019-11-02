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


class TravelingWaveTest(unittest.TestCase):
    def test_power_density(self):
        self.assertGreater(S_i, S_t)



if __name__ == "__main__":
    unittest.main()
