# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

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


