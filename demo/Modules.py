# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# file: modules.py

__author__ = 'Haines Tao'
import sys

def test():
    agrs = sys.argv

    if len(agrs) == 1:
        print('Hello World')
    elif len(agrs) == 2:
        print('Hello %', %agrs[1])
    else:
        print('too many arguments')

# 命令行运行文件时，python解释器将__name__变量置为__main__，在其他地方,if判断则失效
if __name__ == '__main__':
    test()