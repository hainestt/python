# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 邻接多重表

# 
# 说明：定义无向图中的一个顶点
# 释义：包含顶点值data，与该顶点相关联的第一条边FirstEdge

class VertexAdjacencyMultitable(object):
    def __init__(self, data):
        self.data = data
        self.FirstEdge = None


# 
# 说明：定义无向图中的一条边
# 释义：包含当前边是否被访问的标记mark，该边两个顶点在数组中的下标VertexOne和VertexTwo，
# 与VertexOne对应的顶点相关联的下一条边NextEdgeOne、与VertexTwo对应的顶点相关联的下一条边
# NextEdgeTwo，当前边包含的其他信息info

class Edge(object):
    def __init__(self):
        self.mark = None
        self.VertexOne = None
        self.NextEdgeOne = None
        self.VertexTwo = None
        self.NextEdgeTwo = None
        self.info = None

# 
# 说明：定义一个无向图
# 释义：包含图中顶点数VertexNum,边数EdgeNum和邻接多重表Vertices
# 

class GraphAdjacencyMultitable(object):
    def __init__(self):
        self.VertexNum = 0
        self.EdgeNum = 0
        self.Vertices = []