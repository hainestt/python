# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import types

class Animal(object):
    def run(self):
        print('Animal running')

# 继承
class Dog(Animal):
    __slots__ = ('name', 'age')
    def run(self):
        print('Dog is running')
    def eat(self):
        print('Dog is eating')

class Cat(Animal):
    # def run(self):
    #     print('Cat is running')
    def eat(self):
        print('Cat eating')

cins = Cat()
cins.run()
print(isinstance(cins, Animal))
print(type(cins), type(Dog))
print(dir({}))

# 给实例绑定方法
dog = Dog()
def sleep(self, time):
    self.time = time

dog.sleep = types.MethodType(sleep, dog)
dog.sleep(20)
print('sleep',dog.time)

dog.name = 'Michael'
dog.age = 21
dog.score = 12
print(dog.name, dog.age, dog.score)


class Student(object):

    # getter
    @property
    def score(self):
        return self._score
    
    @property
    def name(self):
        return self._name

    # setter
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interge!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        
        self._score = value

    @name.setter
    def name(self, value):
        self._name = value

s = Student()
s.score = 60
print(s.score)
s.score = 88
s.name = 'haines'
print(s.score)
print(s.name)

# 定制类
class Person(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Person object name: %s' %(self.name)

print(Person('haines'))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if (self.a > 10000):
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# for n in Fib():
#     print(n)
f = Fib()
print(f[0], f[10])
print(f[0:5], f[: 10])

# 枚举类
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Month)

@unique
class Weekday(Enum):
    Sum = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sum)

# 元类
Hello = type('Hello', (object,), dict(hello = Weekday))
h = Hello()
print(h)