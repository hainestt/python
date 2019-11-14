# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 邻接矩阵

# 
# 定义一个顶点
# data: 顶点值
# info: 与顶点相关信息
class VertexMatrix(object):
    def __init__(self, data):
        self.data = data
        self.info = None

# 
# 定义一个图
# kind:0->无向图;1->无向网;2->有向图;3->有向网
# Vertices: 所有顶点的顶点集
# Arcs: 邻接矩阵
# VertexNum: 图中顶点数
# ArcNum: 图中边或弧的数目
# 
class GraphMatrix(object):
    def __init__(self, kind, *args, **kwargs):
        self.kind = kind
        self.Vertices = []
        self.Arcs = []
        self.VertexNum = 0
        self.ArcNum = 0
        super().__init__(*args, **kwargs)
