# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 邻接表
#
# 说明：定义图中的一个顶点
# 释义：包含顶点值data和与该顶点相关联的第一条边 FirstArc
#
class VertexAdjacencyList(object):
    def __init__(self, data):
        self.data = data
        self.FirstArc = None

#
# 说明：定义图中的一条边或弧
# 释义：邻接点或弧头adjacent、与该边或弧相关的信息info和
#      与该边或弧依附于相同顶点的下一条边或弧 NextArc
#
class ArcAdjacencyList(object):
    def __init__(self, adjacent):
        self.adjacent = adjacent
        self.info = None
        self.NextArc = None

# 
# kind:0->无向图;1->无向网;2->有向图;3->有向网
# Vertices: 所有顶点的顶点集
# Arcs: 邻接矩阵
# VertexNum: 图中顶点数
# ArcNum: 图中边或弧的数目
# 
class GraphAdjacencyList(object):
    def __init__(self, kind):
        self.kind = kind
        self.VertexNum = 0
        self.ArcNum = 0
        self.Vertices = []
