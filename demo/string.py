# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 首字母大写
print('tEst WORLD!->', 'TEst WORLD!'.capitalize())

# 字符串转小写-> js中 toLowerCase
print('tEst WORLD!->', 'TEst WORLD!'.casefold())

# 指定长度填充字符
print('tEst WORLD!->', 'tEst WORLD!'.center(20, '9'))

# 查找子串出现次数
print('tEst WORLD!->', 'tEst WORLD!'.count('t',0,8))

# 指定编码格式解码字符串
print('tEst WORLD!->', 'tEst WORLD!'.encode(encoding='utf_8', errors='strict'))

# 字符串指定后缀结尾
print('tEst WORLD!->', 'tEst WORLD!'.endswith('LD!'))

# 制表符【\t】转固定个数空格
print('Tab\t\tTwo tabs->', 'Tab\t\tTwo tabs'.expandtabs(0))

# 从左到右查找是否包含子串，返回出现位置,否则返回-1
print('tEst WORLD!->', 'tEst WORLD!->'.find('t'))

# 查找字符串最后一次出现的位置，返回位置，否则返回-1
print('tEst WORLD!->', 'tEst WORLD!->'.rfind('t'))

# 格式字符串输出
print('tEst{}WORLD!->', 'tEst{}WORLD!'.format('---'))

# 字符串映射替换
s = 'Rock'
t = 'Hai'
print('tEst{s}WORLD!{t}', 'tEst{s}WORLD!{t}'.format_map(vars()))

# 子字符串索引
print('tEst WORLD!->', 'tEst WORLD!->'.index('-'))

# 判断字符串是由字符串或数字组成: .isalpha() || .isdecimal() || .isdigit() || .isnumeric()
print('tEst8878WORLD->', 'tEst8878WORLD'.isalnum())

# 判断字符串中是否是有效标识符:字母或字母加数字或字母、下划线和数字的组合
print('tEst WORLD!->', 'tEst_WORLD001'.isidentifier())

# 字符串连接
print('join', '-'.join(['a', 'b', 'c']))

# 字符串填充
print('ljust', 'ljust'.ljust(10, '$'))
print('rjust', 'rjust'.rjust(10, '#'))

# 去除空格
print('trim  strip  :', 'trim  strip  '.rstrip())

# 对照表,按照字符一一映射
ts = 'hello world!'
tt = ts.maketrans('world', '12345') # 参数字符串长度相等
print(ts.translate(tt))

# 字符串分割
print('hello world', 'hello world'.partition('wor'))

# 去换行符
print('hello\n\nworld', 'hello\n\nworld'.splitlines())

# 检查字符串是否以子串开头
print('hello World', 'hello wrold'.startswith('w', 6, 20))

# 0填充
print('a', 'a'.zfill(5))

# 字母大小写反转
print('aAa hello<->', 'aAa hello'.swapcase())

# 分割
print('aAa hello<->', 'aAa hello'.split(' '))