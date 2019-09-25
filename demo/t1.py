# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import time
import math
import re
import struct
from datetime import datetime, timedelta, timezone
from collections import namedtuple, OrderedDict, Counter
import hashlib
import logging
import numpy as np

logging.basicConfig(level = logging.INFO)


def sum1(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

start1= time.process_time()
r1 = sum1(10)
end1  = time.process_time()
print(end1 - start1, r1)

def sum2(n):
    return n * (n+1) / 2 

start2 = time.process_time()
r2 = sum2(10)
end2 = time.process_time()
print(end2 - start2, r2)

def primaryNumber1(n):
    isprimary = True
    for i in range(2, n):
        if n % i == 0:
            isprimary = False
            break

    return isprimary

start1 = time.process_time()
r1 = primaryNumber1(1000000)
end1 = time.process_time()
print(r1, end1 - start1)

def primaryNumber2(n):
    isprimary = True
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            isprimary = False
            break
    return isprimary

start2 = time.process_time()
r2 = primaryNumber2(1000000)
end2 = time.process_time()
print(r2, end2 - start2)


def primaryNumber3(n):
    isprimary = True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            isprimary = False
            break
    return isprimary

start3 = time.process_time()  
r3 = primaryNumber3(1000000)
end3 = time.process_time()

print(r3, end3 - start3)

# ----------------------------
# re
r1 = re.split(r'[\s\,]+', 'a   b,c    dd, e,,0,,,f')
print('s->',r1)

# group
g = re.match(r'^(\d{3})-(\d{3,8})$', '123-89899')
print(g.groups(0), g.group(1), g.group(2))

# pre compiler
m = re.compile(r'(\d{3})-(\d{3,8})$')
m1 = m.match('123-8999').groups()
print(m1)

# -----------------------------
dt = datetime(2019,10,1 ,00,00,59)
print(datetime.now())
print(dt.timestamp())
print(dt.strftime('%a,%b %d %H:%M'))

now = datetime.now()
n = now + timedelta(hours = -24)
print(n)

utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
# 北京时区
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)

Point = namedtuple('Point', ['x', 'y'])
p = Point(9091, 2019)
print(p.x, p.y)
print(isinstance(p, tuple))

dt = dict([('a', 1), ('b', 2), ('c', 3)])
odt = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(dt, odt)

od = OrderedDict()
od['z'] = 1
od['a'] = 2
od['b'] = 3

print(list(od.keys()))

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        # super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity
    
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0

        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last = False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)

lt = LastUpdatedOrderedDict(2)
lt.__setitem__(10, 20)
lt.__setitem__(11, 30)
lt.__setitem__(12, 40)
lt.__setitem__(13, 50)

print(lt)

ch = Counter()
for i in 'hello,world':
    ch[i] = ch[i] + 1

print(ch)


st = struct.pack('>I', 10240099)
print(st)

# f = open('./base.py')
# s = f.read()
# f.close()
# print('s-->', s)

md5 = hashlib.md5()
md5.update('how to upgrade your soul'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to upgrade your soul'.encode('utf-8'))
print(sha1.hexdigest())

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)

n =  np.arange(20).reshape(5,4)

print('n', n)