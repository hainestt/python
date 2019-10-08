# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib.pyplot import plot, show, loglog
from mpl_toolkits.mplot3d.axes3d import Axes3D

# 1
x = np.linspace(0, 20)
plot(x, .5 + x)
plot(x, 1 + 2 * x, '--')
# show()

# 2