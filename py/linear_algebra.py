#!/usr/bin/python
# coding=utf-8
########################################################################
#
# Copyright (c) 2020, CUHK CURI
# Author: SGL
#
# All rights reserved.
# force control class for UR
#
#
########################################################################


import numpy as np

a = np.array([[1], [2]])
b = np.array([[3], [4]])
k_ab = np.kron(a, b)
o_ab = np.outer(a, b)
k_abt = np.kron(a, b.T)

print(k_ab)
print(o_ab)
print(k_abt)