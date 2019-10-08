# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# 
# 1，数据清洗工具：
#   > OpenRefine    
# 
# 
# 
# 
# 

import os
import numpy as np
import pandas as pd
from scipy.stats import scoreatpercentile
from matplotlib.pyplot import plot, show, hist
from os.path import getsize
from tempfile import NamedTemporaryFile
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re
import operator
import string

# 1
# 矩阵求逆
A = np.mat("2 4 6; 4 2 6; 10 -4 18")
inverseA = np.linalg.inv(A)

# 验证[乘积为单位阵]
I = inverseA * A

# 误差
e = inverseA * A - np.eye(3)


# 2
# 线性方程求解
A1= np.mat("1 -2 1; 0 2 -8;-4 5 9")
b = np.array([0, 8, -9])
x = np.linalg.solve(A1, b)

# 验证
x1 = np.dot(A1, x) # b
print('x->', x1)


# 3
# 特征值与特征向量
A2 = np.mat("3 -2;1 0")

# eigenvalues = np.linalg.eigvals(A2)

eigenvalues, eigenvectors = np.linalg.eig(A2)

print(eigenvalues, eigenvectors)



# 4
cash = np.zeros(10000)
cash[0] = 1000
outcome = np.random.binomial(9, 0.5, size = len(cash))

for i in range(1, len(cash)):
    if outcome[i] < 5:
        cash[i] = cash[i - 1] - 1
    elif outcome[i] < 10:
        cash[i] = cash[i - 1] + 1
    else:
        raise AssertionError('unexpected outcome', outcome)
        print(outcome.min(), outcome.max())

# plot(np.arange(len(cash)), cash)
# show()

# 5
np.random.seed(42) # 作用是确保每次生成的随机数都和上次生成的随机数相同
a = np.random.randn(3, 4)
np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header=' #1, #2, #3, #4')

df = pd.DataFrame(a)
df.to_csv('pd.csv', float_format='%.2f', na_rep="NAN!")
print('a->', a)

# 6
json_str = '{\
    "name": "Python: Current File (Integrated Terminal)",\
    "type": "python",\
    "request": "launch",\
    "program": "qq",\
    "console": "integratedTerminal" \
}'

data = pd.read_json(json_str, typ='series')
data['name'] = 'Python learnning'
print(data.to_json())
print(data)

# 7