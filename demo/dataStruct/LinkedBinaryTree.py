# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 
# 定义一个二叉树的结点
# 
class BSTNode(object):
    def __init__(self, value):
        self.value = value
        self.Left = None
        self.Right = None

# 
# 二叉树
# 
class LinkedBinaryTree(object):
    def __init__(self):
        self.Root = None
        self.VisitedFlag = 0 # 后序遍历使用

    # 插入结点
    # O(lgn)
    def InsertNode(self, data):
        lp = self.Root

        if not lp:
            self.Root = BSTNode(data)
            return

        while True:
            if data < lp.value:
                if not lp.Left:
                    lp.Left = BSTNode(data)
                    return
                lp = lp.Left
            elif data > lp.value:
                if not lp.Right:
                    lp.Right = BSTNode(data)
                    return
                lp = lp.Right
            else:
                lp.value = data
                return

    # 删除结点
    # O(lgn)
    def DeleteNode(self, data):
        p = self.Root
        f = None

        # 查找
        while p:
            if p.value == data:
                break
            f = p
            if p.value > data:
                p = p.Left
            if p.value < data:
                p = p.Right

        if not p:
            return
        
        # 删除
        if not p.Left and not p.Right:
            s = p.Left
            while not s.Right:
                s = s.Right

            # 将s的值临时保存到q中
            q = s.value
            # 删除结点s
            self.DeleteNode(s.value)
            # 将q的值赋值给p
            p.value = q

        if p.Left is None and p.Right is None:
            if f.Left == p:
                f.Left = None
                return
            elif f.Right == p:
                f.Right = None
                return
            
        if not p.Left and p.Right is None:
            if f.Left == p:
                f.Left = p.Left
                return
            if f.Right == p:
                f.Right == p.Left
                return
        if p.Left is None and not p.Right:
            if f.Left == p:
                f.Left = p.Right
                return
            if f.Right == p:
                f.Right = p.Right
                return
        

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
            self.PreOrder(Root.Left)
            self.PreOrder(Root.Right)
    
    def PreOrderNonRecursive(self, Root):
        tStack = []
        tp = Root
        while len(tStack) > 0 or tp is not None:
            while tp is not None:
                self.VisitNode(tp)
                tStack.append(tp)
                tp = tp.Left
            if len(tStack) > 0:
                tp = tStack.pop()
                tp = tp.Right

    # 
    # 中序
    # 遍历左子树 -> 访问结点 -> 遍历右子树
    # 
    def InOrder(self, Root):
        if Root is not None:
            self.InOrder(Root.Left)
            self.VisitNode(Root)
            self.InOrder(Root.Right)
    
    def InOrderNonRecursive(self, Root):
        tStack = []
        tp = Root

        while len(tStack) > 0 or tp is not None:
            while tp is not None:
                tStack.append(tp)
                tp = tp.Left

            if len(tStack) > 0:
                tp = tStack.pop()
                self.VisitNode(tp)
                tp = tp.Right

    # 
    # 后序
    # 遍历左子树 -> 遍历右子树 -> 访问结点
    # 
    def PostOrder(self, Root):
        if Root is not None:
            self.PostOrder(Root.Left)
            self.PostOrder(Root.Right)
            self.VisitNode(Root)
    
    def PostOrderNonRecursive(self, Root):
        tStack = []
        tp = Root

        while tp is not None:
            tStack.append(tp)
            tp = tp.Left
        
        while len(tStack) > 0:
            tp = tStack.pop()
            
            if tp.Right is None or tp.VisitedFlag == 1:
                self.VisitNode(tp)
            else:
                tp.VisitedFlag = 1
                tStack.append(tp)
                tp = tp.Right
                while tp is not None:
                    tStack.append(tp)
                    tp = tp.Right