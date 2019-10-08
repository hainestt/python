# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import copy

class GLNode(object):
    def __init__(self):
        self.tag = 1
        self.union = None
        self.next = None

class GList(object):
    def CreateGList(self, Table):
        if len(Table) > 0:
            tTable = Table.pop(0)
            tGLNode = GLNode()
            if tTable == '(':
                tGLNode.tag = 1
                tGLNode.union = self.CreateGList(Table)
            elif tTable == ')' or tTable == '#':
                tGLNode = None
            else:
                tGLNode.tag = 0
                tGLNode.union = tTable
        else: 
            tGLNode = None
        
        if len(Table) > 0:
            tTable = Table.pop(0)
        if tGLNode != None:
            if tTable == ',':
                tGLNode.next = self.CreateGList(Table)
            else:
                tGLNode.next = None
        
        return tGLNode

    def TraverseGList(self, GList):
        if GList != None:
            if GList.tag == 0:
                print(GList.union, end=' ')
            else:
                print('(', end='')
                if GList.union == None:
                    print('#', end=' ')
                else:
                    self.TraverseGList(GList.union)
                print(')', end=' ')
            if GList.next != None:
                print(',', end=' ')
                self.TraverseGList(GList.next)

    def GetGListHead(self, GList):
        if GList != None and GList.union != None:
            head = copy.deepcopy(GList.union)
            head.next = None

            return head
        else:
            print('can not get head list!')

    def GetGListTail(self, GList):
        if GList != None and GList.union != None:
            tail = copy.deepcopy(GList.union.next)
            return tail
        else:
            print('can not get tail list!')






