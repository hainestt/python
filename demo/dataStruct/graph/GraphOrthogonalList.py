# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 
# 定义有向图的一个顶点
# 
class VertexOrthogonalList(object):
    def __init__(self, data):
        # 顶点值
        self.data = data
        # 以该顶点为弧头的第一条弧
        self.FirstHeadArc = None
        # 以该顶点为弧尾的第一条弧
        self.FirstTailArc = None

# 
# 定义有向图中的一条弧
# 
class ArcOthogonalList(object):
    def __init__(self):
        # 当前弧中狐尾在数组中的下标
        self.TailVertex = None
        # 当前弧中弧头在数组中的下标
        self.HeadVertex = None
        # 与当前弧有相同狐尾的下一条弧
        self.NextTailArc = None
        # 与当前弧有相同弧头的下一条弧
        self.NextHeadArc = None
        # 当前弧包含的其他信息
        self.info = None
