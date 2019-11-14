# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 十字链表
# 
# 定义有向图的一个顶点
# data: 顶点值
# FirstHeadArc: 以该顶点为弧头的第一条弧
# FirstTailArc: 以该顶点为弧尾的第一条弧
# 
class VertexOrthogonalList(object):
    def __init__(self, data):
        self.data = data
        self.FirstHeadArc = None
        self.FirstTailArc = None

# 
# 定义有向图中的一条弧
# 
# TailVertex: 当前弧中狐尾在数组中的下标
# HeadVertex: 当前弧中弧头在数组中的下标
# NextTailArc: 与当前弧有相同狐尾的下一条弧
# NextHeadArc: 与当前弧有相同弧头的下一条弧
# info: 当前弧包含的其他信息
# 
class ArcOthogonalList(object):
    def __init__(self):
        self.TailVertex = None
        self.HeadVertex = None
        self.NextTailArc = None
        self.NextHeadArc = None
        self.info = None
