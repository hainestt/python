# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import os

arrys = list(range(1, 16, 2))

for item in arrys: 
    print('h:',item)

squares = []
for value in range(1, 11):
    squares.append(value ** 2 + 1)
print('squares', squares)

digits = list(range(10))
print(min(digits), max(digits), sum(digits))

players = ['haines', 'rocks', 'pythons']
print('players:', players[0: 2])

copyPlayers = players[:]
players.append('tim')
print('copyPlayers->players', copyPlayers, players)

isRinP = 'rocks' in players
inTnotInP = 'petter' not in players
print(isRinP, inTnotInP)


age = 19
if age < 18:
    print('lower')
elif age == 18:
    print('equal')
else:
    print('higher')

dics = {'color': 'green', 'points': 5}
for key, value in dics.items():
    print(key, value)

print(dics.keys(), dics.values(), dics.items())

# number = input()
# print(type(number))

# 列表生成器
lg = [x * x for x in range(1, 11)]
print(lg)

lg1 = [m + n for m in 'ABC' for n in 'XYZ']
print(lg1)

lg2 = [d for d in os.listdir('.')]
print(lg2, os)

# 数据类型 str, object, dict, tuple, int, float
print(isinstance(2, tuple))

# 生成器
g = (x * x for x  in range(1, 11))
print(next(g), next(g))

aa = 11
bb = 22

tp = (bb, aa + bb)
aa, bb = tp
print(aa, bb)

print(int('18', 16))

# lambda: 相当于js中的箭头函数
g = lambda x, y: x + y
print(g(1, 210))

# 初始化列表
[2 for i in range(10)] # 定义一个长度为10的列表，列表中每个值都为2

