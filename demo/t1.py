# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import time
import math
def sum1(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

start1= time.clock()
r1 = sum1(10)
end1  = time.clock()
print(end1 - start1, r1)

def sum2(n):
    return n * (n+1) / 2 

start2 = time.clock()
r2 = sum2(10)
end2 = time.clock()
print(end2 - start2, r2)

def primaryNumber1(n):
    isprimary = True
    for i in range(2, n):
        if n % i == 0:
            isprimary = False
            break

    return isprimary

start1 = time.clock()
r1 = primaryNumber1(1000000)
end1 = time.clock()
print(r1, end1 - start1)

def primaryNumber2(n):
    isprimary = True
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            isprimary = False
            break
    return isprimary

start2 = time.clock()
r2 = primaryNumber2(1000000)
end2 = time.clock()
print(r2, end2 - start2)


def primaryNumber3(n):
    isprimary = True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            isprimary = False
            break
    return isprimary

start3 = time.clock()  
r3 = primaryNumber3(1000000)
end3 = time.clock()

print(r3, end3 - start3)