# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

from dataStruct.graph.GraphMatrix import VertexMatrix, GraphMatrix

# 
# 邻接矩阵实现Prim算法--构造最小生成树
# 
class Prim(GraphMatrix):
    def __init__(self, kind = 0):
        super().__init__(kind)
        self.CreateGraphFromInput()

    def CreateGraphFromInput(self):
        pass
        
    # 
    # Vertex：创建最小生成树的起点
    def MiniSpanTreePrim(self, Vertex):
        pass
        
    def GetMin(self, CloseEdge):
        pass
