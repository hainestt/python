# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 邻接矩阵
class VertexMatrix(object):
    def __init__(self, data):
        self.data = data
        self.info = None

class GraphMatrix(object):
    def __init__(self, kind):
        self.kind = kind
        self.Vertices = []
        self.Arcs = []
        self.VertexNum = 0
        self.ArcNum = 0
