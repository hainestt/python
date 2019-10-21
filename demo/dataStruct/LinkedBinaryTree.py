# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class LinkedBinaryTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.LeftChild = None
        self.RightChild = None
        self.VisitedFlag = 0 # 后序遍历使用

    def VisitNode(self, Node):
        if Node.data is not '#':
            print(Node.data)

    # 
    # 先序
    # 先访问结点 -> 遍历左子树 -> 遍历右子树
    # 
    def PreOrder(self, Root):
        if Root is not None:
            self.VisitNode(Root)
            self.PreOrder(Root.LeftChild)
            self.PreOrder(Root.RightChild)
    
    def PreOrderNonRecursive(self, Root):
        tStack = []
        tp = Root
        while len(tStack) > 0 or tp is not None:
            while tp is not None:
                self.VisitNode(tp)
                tStack.append(tp)
                tp = tp.LeftChild
            if len(tStack) > 0:
                tp = tStack.pop()
                tp = tp.RightChild

    # 
    # 中序
    # 遍历左子树 -> 访问结点 -> 遍历右子树
    # 
    def InOrder(self, Root):
        if Root is not None:
            self.InOrder(Root.LeftChild)
            self.VisitNode(Root)
            self.InOrder(Root.RightChild)
    
    def InOrderNonRecursive(self, Root):
        tStack = []
        tp = Root

        while len(tStack) > 0 or tp is not None:
            while tp is not None:
                tStack.append(tp)
                tp = tp.LeftChild

            if len(tStack) > 0:
                tp = tStack.pop()
                self.VisitNode(tp)
                tp = tp.RightChild

    # 
    # 后序
    # 遍历左子树 -> 遍历右子树 -> 访问结点
    # 
    def PostOrder(self, Root):
        if Root is not None:
            self.PostOrder(Root.LeftChild)
            self.PostOrder(Root.RightChild)
            self.VisitNode(Root)
    
    def PostOrderNonRecursive(self, Root):
        tStack = []
        tp = Root

        while tp is not None:
            tStack.append(tp)
            tp = tp.LeftChild
        
        while len(tStack) > 0:
            tp = tStack.pop()
            
            if tp.RightChild is None or tp.VisitedFlag == 1:
                self.VisitNode(tp)
            else:
                tp.VisitedFlag = 1
                tStack.append(tp)
                tp = tp.RightChild
                while tp is not None:
                    tStack.append(tp)
                    tp = tp.RightChild

    # TODO
    # 