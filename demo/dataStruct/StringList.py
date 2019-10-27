# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 顺序串
class StringList(object):
    def __init__(self):
        self.MaxStringSize = 4096
        self.chars = ''
        self.length = 0
    
    def IsEmptyString(self):
        if self.length == 0:
            IsEmpty = True
        else:
            IsEmpty = False
        return IsEmpty

    def CreateStringV2(self, string):
        self.chars = string[:self.MaxStringSize]
        self.length = len(self.chars)

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
        return len(self.chars)

    def GetString(self):
        return self.chars   

    # 模式匹配：BF算法
    # 优点：算法简单易懂
    # 缺点：会出现重复匹配不必要的字符；最坏时间复杂度较高
    # 
    # 
    def IndexBF(self, pos, T):
        length = T.GetStringLength()
        if len(self.chars) >= length:
            i = pos
            string = T.GetString()

            while(i <= len(self.chars) - length):
                iT = i
                j = 0
                tag = False

                while j < length:
                    if self.chars[i] == string[j]:
                        i = i + 1
                        j = j + 1
                    else:
                        break
                    
                if j == length:
                    # print('matched success! matched pos:', iT)
                    tag = True
                    break
                else:
                    i = iT + 1
            
            if tag == False:
                # print('matched failure')
                return None
            else:
                return iT
    
    # 模式匹配：KMP算法
    # -> 基本思想是在匹配失败后，无须回到主串和模式串最近一次开始比较的位置，而是在不改变主串已经匹配到的位置的前提下，
    #    根据已经匹配的部分字符，从模式串的某一位置开始继续进行串的模式匹配
    # -> 复杂度: O(m + n)
    # 
    def IndexKMP(self, pos, T, NextList):
        i = pos
        j = 0
        length = T.GetStringLength()
        string = T.GetString()

        while i < len(self.chars) and j < length:
            if j == -1 or self.chars[i] == string[j]:
                i = i + 1
                j = j + 1
            else:
                j = NextList[j]
        if j == length:
            # print('matched success! matched pos:', i - length)
            return i - length
        else:
            # print('matched failure')
            return None


    # 对于当前位置j,ListNext[j]的值计算规则如下：
    # 1，当j = 0是，ListNext[j] = -1
    # 2，若存在一个k,使得 0<k<j且T[0 ~ k-1] == T[j-k ~ j-1], 则ListNext[j] = k,
    #    这里把T[0 ~ k-1]称为真前缀串，T[j-k ~ j-1]称为真后缀串
    # 3，其他情况下, ListNext[j] = 0
    def GetListNext(self):
        length = len(self.chars)
        ListNext = [None for x in range(length * 3)]
        ListNext[0] = -1
        j = 0
        k = -1
        while j < length:
            if k == -1 or self.chars[j] == self.chars[k]:
                k = k+1
                j = j+1
                ListNext[j] = k
            else:
                k = ListNext[k]

        print('NextList', ListNext)
        return ListNext
    
    # 对GetListNext方法改进原因：
    # -> 当ListNext[j] = k，而T[k] == T[j]，若有S[i] != T[j]，则不需要进行S[i]与T[k]的比较，可直接获取下一个ListNext值，
    #    并与T[j]进行比较
    # 
    def GetListNextValue(self):
        length = len(self.chars)
        ListNextValue = [None for x in range(length)]
        ListNextValue[0] = -1
        k = -1
        j = 0
        while j < length - 1:
            if k == -1 or self.chars[j] == self.chars[k]:
                k = k + 1
                j = j + 1
                if self.chars[j] != self.chars[k]:
                    ListNextValue[j] = k
                else:
                    ListNextValue[j] = ListNextValue[k]
            else:
                k = ListNextValue[k]
        
        print('ListNextValue->', ListNextValue)
        return ListNextValue


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

