# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# file: sequenceStack.py

class SequenceStack(object):
    def __init__(self, Max):
        self.MaxStackSize = Max or 10
        self.s = [None for x in range(0, self.MaxStackSize)]
        self.top = -1
    
    def isEmptyStack(self):
        if self.top == -1:
            iTop = True
        else:
            iTop = False
        
        return iTop

    def PushStack(self, x):
        if self.top < self.MaxStackSize - 1:
            self.top = self.top + 1
            self.s[self.top] = x
        else:
            print('stack full')
            return
    def PopStack(self):
        if self.isEmptyStack():
            print('stack empty')
            return
        else:
            iTop = self.top
            self.top = self.top -1
            return self.s[iTop]
    def GetTopStack(self):
        if self.isEmptyStack():
            print('stack empty')
            return
        else:
            return self.s[self.top]
    def StackTraverse(self):
        if self.isEmptyStack():
            print('stack empty')
            return
        else:
            for i in range(0, self.top + 1):
                print(self.s[i], end = '  ')
    def CreateStackByInput(self):
        data = input('input something: ')
        while data != '#':
            self.PushStack(data)
            data = input('place input and end with #: ')