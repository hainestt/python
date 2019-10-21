# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

from multiprocessing import Process, Pool, Queue
import os, time, random
import subprocess

print('Process %s start...' % os.getpid())

pid = os.fork()

if pid == 0:
    print('child process %s, parent process %s.' % (os.getpid(), os.getppid()))
else:
    print('my procrss %s, parent process %s.' % (os.getpid(), pid))


def child(name):
    print('running subprocess in %s, and args is %s' %(os.getpid(), name))

def parent():
    print('parent process is %s' % os.getpid())
    p = Process(target = child, args = ('test', ))
    print('child process starting')
    p.start()
    p.join()
    print('child process ending')

parent()

def long_time_task(name):
    print('Run task %s on(%s)' %(name, os.getpid()))
    start = time.start()
    time.speep(random.random() * 3)
    end = time.end()
    print('Task %s runs %0.2f seconds' % (name, (end - start)))

def poolfn():
    print('parent processing %s' %(os.getpgid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args = (i, ))
    print('waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done.')

# poolfn()
def nslookupfn():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('exit', r)

# nslookupfn()

# 进程间通信
def write(q):
    print('Process id: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put %s in queue' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process id: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from the queue' % value)

def main() :
    q = Queue()
    pw = Process(target = write, args = (q,))
    pr = Process(target = read, args = (q,))

    pw.start()

    pr.start()

    pw.join()

    pr.terminate()
    
main()


