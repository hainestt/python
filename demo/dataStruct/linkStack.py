# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class StackNode(object):
    def __init__(self):
        self.data = None
        self.next = None

class LinkStack(object):
    def __init__(self):
        self.top = StackNode()
    
    def IsEmptyStack(self):
        if self.top.next == None:
            iTop = True
        else:
            iTop = False
        return iTop

    def PushStack(self, da):
        tsnode = StackNode()
        tsnode.data = da
        tsnode.next = self.top.next
        self.top.next = tsnode
    
    def PopStack(self):
        if self.IsEmptyStack() == True:
            print('stack empty!')
            return
        else:
            tsnode = self.top.next
            self.top.next = tsnode.next

            return tsnode.data
    
    def GetTopStack(self):
        if self.IsEmptyStack():
            print('stack empty!')
            return
        else:
            return self.top.next.data
    
    def CreateStackByInput(self):
        data = input('input something: ')
        while data != '#':
            self.PushStack(data)
            data = input('please input and end with #')
    
