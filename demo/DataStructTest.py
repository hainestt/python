# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import os
import time
import numpy as np

from sys import getrefcount
from dataStruct.SequenceStack import SequenceStack
from dataStruct.HuffmanTree import HuffmanTreeNode
from dataStruct.StringList import StringList
from dataStruct.GeneralList import GList
from dataStruct.graph.Graph import Graph


def plaindrome(s):
    ss1 = SequenceStack(100)
    ss2 = SequenceStack(100)
    i = 0
    
    while i < len(s):
        ss1.PushStack(s[i])
        i = i + 1
    
    print('ss1栈元素为：', ss1.StackTraverse())

    i = i - 1
    while i < len(s) and i >= 0:
        ss2.PushStack(s[i])
        i = i - 1
    print('ss2栈元素为: ', ss2.StackTraverse())

    while ss1.isEmptyStack != True:
        if ss1.PopStack() != ss2.PopStack():
            print(s,'不是回文')
        return

s = '秋江楚雁宿沙洲，雁宿沙洲浅水流。流水浅洲沙宿雁，洲沙宿雁楚江秋'
t = '秋江楚雁宿沙洲，雁宿沙洲浅水流。流水浅洲沙宿雁，洲沙宿雁楚江秋'

# plaindrome(s)
# print(hex(id(s)), hex(id(t)), s is t, getrefcount(t))


def hfmtest():
    LeafNodes = []
    huffman = HuffmanTreeNode()
    huffman.CreateLeafNodes(LeafNodes)
    
    print('create huffman tree!:)')
    root = huffman.CreateHuffmanTree(LeafNodes)
    Codes = []
    print('huffman encode!:)')
    huffman.HuffmanEncoding(root, LeafNodes, Codes)

    print('endcode result: ')
    for index in range(len(Codes)):
        print(LeafNodes[index].data, ':', Codes[index])

# hfmtest()

def stringTest():
    sPath = '/demo/file/'
    cwd = os.getcwd()
    path = cwd+sPath

    files = os.listdir(path)
    sourceStr = StringList()
    targetStr = StringList()
    targetStr.CreateStringV2('the sake of love alone')

    start1 = time.process_time()
    for file in files:
        if not os.path.isdir(file):
            f = open(path+file)

            lines = f.readlines()
            lineCount = len(lines)

           
            for i in range(lineCount):
                string = lines[i]
                sourceStr.CreateStringV2(string)
                # kmpIndex = sourceStr.IndexKMP(0, targetStr, targetStr.GetListNext())
                # kmpIndex = sourceStr.IndexKMP(0, targetStr, targetStr.GetListNextValue())
                kmpIndex = sourceStr.IndexBF(0, targetStr)

                if kmpIndex is not None:
                    print('文件路径：%s, 匹配的文件行： %i, 匹配的文件列：%i' % (path+file, i+1, kmpIndex+1))

            f.close()

    end1 = time.process_time()
    print('处理时间：', end1 - start1)


    # test2
    ss = StringList()
    tt = StringList()
    ss.CreateStringV2('ababaab')
    tt.CreateStringV2('ababaab')

    ss.IndexKMP(0, tt, tt.GetListNextValue())

# stringTest()

def generalListTest():
    s = GList()
    t = s.CreateTable()

    gl = s.CreateGList(t)
    s.TraverseGList(gl)

# generalListTest()


def graphTest():
    g = Graph(1)
    g.DFSTraverse()


graphTest()