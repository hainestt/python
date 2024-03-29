class Practise(object):
    def fpt(self, number):
        i = 2
        ret = []

        while number != 1 and i <= number:
            r = number / i
            if r == int(r):
                ret.append(i)
                number = r
            else:
                i = i + 1

        return ret

    def mathround(self, number):
        if isinstance(number, float):
            num = round(number, 1)
            snum = int(str(num).split('.')[1])

            num = int(num) + 1 if snum >= 5 else int(num) - 1

            return num
    
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    def sortByDict(self):
        n = int(input('Please input the number of strings: '))
        strList = []
        while n > 0:
            s = input('Please input a string: ')
            strList.append(s)
            n = n - 1
        
        print('input:', ' '.join(strList))
        length = len(strList)
        for i in range(length):
            for j in range(length):
                if strList[i] < strList[j]:
                    self.swap(strList, i, j)
        
        print('output:', ' '.join(strList))



    def mainFindLongSubString():
        num = int(input('Please input the group number of substrings:'))
        strList = []
        ret = []
        while num > 0:
            subs1, subs2 = input('string1:'), input('string2:')
            strList.append([subs1, subs2])
            num = num - 1
        
        length = len(strList)
        if length > 0:
            for i in range(length):
                    ret.append(findLongSubString(strList[i][0], strList[i][1]))
        
        if len(ret) > 0:
            for i in range(len(ret)):
                print(ret[i], '\n')

    def findLongSubString(str1, str2):
        stack = []
        maxStack = []
        i,j = 0, 0
        len1 = len(str1)
        len2 = len(str2)
        
        while i <= len1 - 1:
            while j <= len2 - 1:
                if str2[j] == str1[i]:
                    stack.append(str2[j])
                    i = i + 1
                    if i >= len1:
                        break
                elif len(stack) > 0:
                    maxStack.append(len(stack))
                    stack = []
                j = j + 1
            
            i = i + 1
            j = 0
        
        if len(stack) > 0:
            maxStack.append(len(stack))

        if len(maxStack) > 0:
            return max(maxStack)
        else:
            return 0
    
    # 
    # 01背包问题，待回溯
    # TODO
    def shopping(self):
        N, m = int(input('input N:')), int(input('input m: '))
        sList = []
        n = m

        while n > 0:
            sl = input('shopping list, split with space,e :800 2 0 ->:').split(' ')
            # sl[0]: 表示物价；sl[1]: 表示单价与重要度之积，即价值；sl[2]:表示主件还是附件
            sList.append((int(sl[0]), int(sl[0]) * int(sl[1]), int(sl[2])))
            n = n - 1
        a = [[0] * (N + 1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, N+1):
                # if sList[i][2] == 0 :
                # if sList[i - 1][0] <= j:
                #     a[i][j] = max(a[i - 1][j], a[i - 1][j - sList[i - 1][0]] + sList[i][1])
        print(a[m][N])
        


        
p = Practise()

# p.sortByDict()
p.mainFindLongSubString()