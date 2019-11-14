# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib.pyplot import plot, bar, pie, show, loglog
from mpl_toolkits.mplot3d.axes3d import Axes3D
import vendor.Pmf as pmf

# 1
x = np.linspace(0, 20)
plot(x, .5 + x)
plot(x, 1 + 2 * x, '--')
# show()

# 2
hist = pmf.MakeHistFromList([1,6,2,2,3,5])
# hist.Freq(5)
# hist.Values()
vals,fregs = hist.Render()
rectangles = bar(vals, fregs)
show()
print(vals, fregs)

