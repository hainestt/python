# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Search(object):
    def __init__(self, dataList, chunks = 5):
        self.data = dataList
        self.chunks = chunks
    
    # 顺序查找
    def SequenceSearch(self, key):
        for i in range(len(self.data)-1, 0, -1):
            if self.data[i] == key:
                return i
        return -1

    # 折半查找
    def BinarySearch(self, key):
        low = 0
        high = len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2 # 向下取整
            if key < self.data[mid]:
                high = mid - 1
            elif key > self.data[mid]:
                low = mid + 1
            else:
                return mid
        return -1
    
    # 索引查找
    # 1，将列表分成若干块
    # 2，取出每分块中的最大值分别与待查值比较，只有前者大的时候，才在当前分块中继续查找
    # 
    def IndexSearch(self, key):
        IndexTable = self.CreateIndexTable()
        iPos = -1
        low = 0
        high = 0
        num = len(self.data) // self.chunks # 子块元素个数

        for i in range(len(IndexTable)-1):
            maxKey = IndexTable[i]
            nextKey = IndexTable[i+1]
            if key <= maxKey[0]:
                low = 0
                high = low + num
                break
            elif key > maxKey[0] and key <= nextKey[0]:
                low = nextKey[1]
                high = low + num
                break

        if high is not 0:
            for i in range(low, high):
                if key == self.data[i]:
                    return i
        else:
            return -1
            
    
    # 
    # 创建索引表：
    # 注意分块有序
    # 
    def CreateIndexTable(self):
        tList = []
        n = self.chunks
        listLength = len(self.data)
        if n <= listLength:
            subListLen = listLength // n
            for i in range(n):
                # tList分为两部分：
                # 第一部分为当前分块中最大值
                # 第二部分h为当前分块在原列表中的起始地址
                low = i * subListLen
                high = i * subListLen + subListLen
                idx = i * subListLen
                tList.append([max(self.data[low:high]), idx])
        
        # 以字典序排序
        tList.sort()
        return tList

    # TODO


            






