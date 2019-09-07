# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 错误类型和继承关系：https://docs.python.org/3/library/exceptions.html#exception-hierarchy
try:
    print('hello...')
    # 出现异常，后面代码不会执行，直至捕获到该异常
    # foo()
    r = 10 / int('a')
    print('world')
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZoreDivisionError:', e)
# UnicodeError继承自ValueError,因此不会被捕获到
except UnicodeError as e:
    print('UnicodeError', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2

if __name__ == "__main__":
    try:
        bar('0')
    except Exception as e:
        print('Exception:', e)
    finally:
        print('finally...')


