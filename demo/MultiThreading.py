# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import threading, multiprocessing

balance = 0
# 线程锁，防止线程中断
lock = threading.Lock()

def change_it(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(1000000):
        # 获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
            

t1 = threading.Thread(target = run_thread, args=(5,))
t2 = threading.Thread(target = run_thread, args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

# print(balance)

print('CPU count: %s' % multiprocessing.cpu_count())


# ------------------------------------------------------------------------------
local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s, pid is %s' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target = process_thread, args=('Alice'), name = 't-A')
t2 = threading.Thread(target = process_thread, args=('Bob'), name='t-B')

t1.start()
t2.start()
t1.join()
t2.join()



