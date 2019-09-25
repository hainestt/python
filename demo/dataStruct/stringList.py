# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 顺序串
class StringList(object):
    def __init__(self):
        self.MaxStringSize = 256
        self.chars = ''
        self.length = 0
    
    def IsEmptyString(self):
        if self.length == 0:
            IsEmpty = True
        else:
            IsEmpty = False
        return IsEmpty

    def CreateString(self):
        string = input('please input: ')

        if len(string) > self.MaxStringSize:
            print('out of storage space')
            self.chars = string[:self.MaxStringSize]
        else:
            self.chars = string

        self.length = len(self.chars)

    def StringConcat(self, strSrc):
        length = strSrc.length
        string = strSrc.chars

        if length + len(self.chars) <= self.MaxStringSize:
            self.chars = self.chars + string
        else:
            print('out of storage space')
            size = self.MaxStringSize - len(self.chars)
            self.chars = self.chars + string[0:size]

    def SubString(self, iPos, length):
        if iPos > len(self.chars) - 1 or (length + iPos) > len(self.chars) or iPos < 0 or length < 1:
            print('can not get substring')
            substr = None
        else:
            substr = self.chars[iPos: iPos + length]
        return substr
    
    def GetStringLength(self):
        return self.length

    def GetString(self):
        return self.chars

    # 模式匹配：BF算法
    # def IndexBF(self, pos, T):
    #     length = T.GetStringLength()
        


# 链式串节点
class StringNode(object):
    def __init__(self):
        self.data = None
        self.next = None

# 链式串
class StringLink(object):
    def __init__(self):
        self.head = StringNode()
        self.tail = self.head
        self.length = 0

    def IsEmptyString(self):
        if self.head.next == None and self.tail.next == None and self.length == 0:
            IsEmpty = True
        else:
            IsEmpty = False
        
        return IsEmpty

    def CreateString(self):
        string = input('please input:')

        while len(string) > self.length:
            Tstring = StringNode()
            Tstring.data = string[self.length]
            Tstring.tail.next = Tstring
            self.tail = Tstring
            self.length = self.length + 1
    
    def StringCopy(self, strSrc):
        self.head = strSrc.head
        self.tail = strSrc.tail
        self.length = strSrc.length

    def StringConcat(self, strSrc):
        self.tail.next = strSrc.head.next
        self.tail = strSrc.tail
        self.length = self.length + strSrc.length

