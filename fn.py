# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 全部函数参考：https://docs.python.org/3/library/functions.html

import collections
import functools

# 绝对值
print(abs(-123.11))

# all参数是一个迭代器，其内容都为真的时候，返回true,否则返回false
print(all([0, -1, 1]))

# any参数是一个迭代器，其内容任意元素为真是，返回true。迭代器空，false
print(any([0, -1, 1]))

print(float('-Infinity'))

print(hex(255))

print('%#x' % 255, '%x' % 255, '%X' % 255)


# 定义函数
def fib(n):
    if n == 1 or n == 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(10))

# 可变参数
def calc(*number):
    sum = 0
    for i in number:
        sum = sum + i * i
    return sum

nums = [1,2,3,4,5]
print(calc(*nums))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(n, p):
    if n == 1:
        return p
    return fact_iter(n - 1, n * p)

print(fact(120))

# 装饰器方法
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper

# 装饰器
@log
def now():
    print('2019-8-30')

now()

# 斐波那契 生成器
# def fib2(max):
#     n,a,b = 0,0,1
#     while n < max: 
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# f = fib2(6)
# print(f.next())

print(isinstance([], collections.Iterable))

def df(x):
    return x * x
r = map(df, [1,2,3,4,5,6])
print(list(r))

def nomalize(name):
    return name.title()

# function tools
# ['RLock', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', 'cmp_to_key', 'get_cache_token', 'lru_cache', 'namedtuple', 'partial', 'partialmethod', 'recursive_repr', 'reduce', 'singledispatch', 'total_ordering', 'update_wrapper', 'wraps']
ftools = [e for e in dir(functools) if not e.startswith('_')]
print(ftools)

# 偏函数
int2 = functools.partial(int, base = 2)
print(int2('1001'))
# 等价于
kw = {'base': 2}
print(int('1001', **kw))

max2 = functools.partial(max, 10)
max2(5, 6, 7)
# 等价于
args = (10, 5, 6, 7)
print(max(*args))

# cmp_to_key
def compare(a, b):
    return a - b

cmp2keyarr = [2, 3, 1]
print(sorted(cmp2keyarr, key = functools.cmp_to_key(compare))) 

# reduce
reduces = range(1, 6)
print(functools.reduce(lambda x, y: x + y, reduces))

