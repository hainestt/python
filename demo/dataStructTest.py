# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

from dataStruct.sequenceStack import SequenceStack
from dataStruct.huffmanTree import HuffmanTreeNode

from sys import getrefcount

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
plaindrome(s)

print(hex(id(s)), hex(id(t)), s is t, getrefcount(t))


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

hfmtest()
