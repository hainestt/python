# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

from dataStruct.graph.GraphAdjacencyList import GraphAdjacencyList, VertexAdjacencyList, ArcAdjacencyList
from queue import Queue
# 
# 邻接表实现图
# 
class Graph(GraphAdjacencyList):
    def __init__(self, kind = 0):
        super().__init__(kind)
        self.CreateGraphFromInput()
        
    def CreateGraphFromInput(self):
        GIList = []
        Vertexs = []
        tv = []

        print('输入顶点，以及边信息[0表示无权重], 用空格分隔，以 `# # #` 结束输入,如`A D 1`:')
        
        v1, v2, w = input('->:').split(' ')

        while v1 != '#':
            if self.kind == 2 or self.kind == 3:
                GIList.append([v1, v2, w])
            elif self.kind == 0 or self.kind == 1:
                GIList.append([v1, v2, w])
                GIList.append([v2, v1, w])
            v1,v2,w = input('->:').split(' ')

        for sList in GIList:
            if sList[0] not in tv:
                tv.append(sList[0])
                Vertexs.append(VertexAdjacencyList(sList[0]))
            if sList[1] not in tv:
                tv.append(sList[1])
                Vertexs.append(VertexAdjacencyList(sList[1]))
        
        # 顶点数目
        self.VertexNum = len(Vertexs)
        
        # 边或弧数目
        self.ArcNum = len(GIList)

        # 构建邻接表
        for v in Vertexs:
            p = v
            for s in GIList:
                if v.data == s[0]:
                    edge = ArcAdjacencyList(tv.index(s[1]))
                    edge.info = s[2]
                    if v.FirstArc is None:
                        v.FirstArc = edge
                        p = edge
                    else:
                        p.NextArc = edge
                        p = p.NextArc
                
            self.Vertices.append(v)

    # 
    # vertexIndex: 顶点下标
    # return -> 该顶点第一个邻接点的下标
    # 
    def GetFirstAdjacentVertex(self, vertexIndex):
        vl = len(self.Vertices)

        if vertexIndex >=0 and vertexIndex < vl:
            v = self.Vertices[vertexIndex]
            vn = v.FirstArc
            return vn.adjacent

    # 
    # vertexIndex: 顶点下标
    # nextAdjacent: vertexIndex指定顶点的某一邻接点的下标
    # return -> 下标为nextAdjacent的顶点的后继结点  
    # 
    def GetNextAdjacentVertex(self, vertexIndex, nextAdjacent):
        vl = len(self.Vertices)
        if vertexIndex >= 0 and vertexIndex < vl:
            v = self.Vertices[vertexIndex]
            vn = v.FirstArc

            while vn is not None:
                if vn.adjacent == nextAdjacent:
                    return self.Vertices[nextAdjacent].FirstArc.adjacent
                else:
                    vn = vn.NextArc
    
    # 
    # 深度优先：
    # 对于无向图，从某一顶点v开始，先访问v，然后依次以顶点v未被访问的邻接点为起点深度优先遍历图，直到所有与顶点v连通的顶点都被访问
    # 对于有向图，则依次以顶点v邻接到的未被访问的顶点为起点深度优先遍历图，直到从顶点v出发能到达的所有顶点都被访问
    # 
    def DFSTraverse(self):
        visited = []
        index = 0
        while index < self.VertexNum:
            visited.append('False')
            index = index + 1
        
        index = 0
        while index < self.VertexNum:
            if visited[index] is 'False':
                self.DFS(visited, index)
            index = index + 1
    
    def DFS(self, visited, vIndex):
        visited[vIndex] = 'True'
        self.VisitVertex(vIndex)
        nextAdjacent = self.GetFirstAdjacentVertex(vIndex)

        while nextAdjacent is not None:
            if visited[nextAdjacent] is 'False':
                self.DFS(visited, nextAdjacent)
            elif visited[nextAdjacent] is 'True':
                break
            nextAdjacent = self.GetNextAdjacentVertex(vIndex, nextAdjacent)

    # 
    # 广度优先：
    # 对于无向图，从某一顶点v开始，先访问v，然后依次访问顶点v未被访问的邻接点，再依次访问这些邻接点未被访问的邻接点，直到所有与顶点v连通的顶点都被访问
    # 对于有向图，则依次访问顶点v邻接到的所有未被访问的顶点，再依次访问这些顶点邻接到的未被访问的顶点，直到从顶点v出发能到达的所有顶点都被访问到
    
    # TODO: add test
    # 
    def BFSTraverse(self):
        visited = []
        index = 0
        while index < self.VertexNum:
            visited.append('False')
            index = index + 1
        
        index = 0
        q = Queue(1024)

        while index < self.VertexNum:
            if visited[index] is 'False':
                visited[index] = 'True'
                self.VisitVertex(index)
                q.put(index)
                while q.empty() is False:
                    tVertex = q.get()
                    nextAdjacent = self.GetFirstAdjacentVertex(tVertex)
                    while nextAdjacent is not None:
                        if visited[nextAdjacent] is 'False':
                            visited[nextAdjacent] = 'True'
                            self.VisitVertex(nextAdjacent)
                            q.put(nextAdjacent)
                        nextAdjacent = self.GetNextAdjacentVertex(tVertex, nextAdjacent)
                    
            index = index + 1

    def VisitVertex(self, vIndex):
        print('v->', self.Vertices[vIndex].data)