# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import math

critics = {
    'Lisa': {
        'Lady in the Water': 2.5,
        'Snake on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5
    },
    'Toby': {
        'Lady in the Water': 3.0,
        'Snake on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.0
    },
    'Mick': {
        'Lady in the Water': 3.0,
        'Snake on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'You, Me and Dupree': 3.0
    },
    'Jack': {
        'Lady in the Water': 3.0,
        'Snake on a Plane': 4.0,
        'Just My Luck': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5
    }
}

# 1
# 欧几里德距离
# 
# 返回值越小，表明两人偏好越相近
def simDistance(c, p1, p2):
    si = {}
    for item in c[p1]:
        if item in c[p2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    
    diff = c[p1][item] - c[p2][item]
    sumOfSquares = sum([pow(diff, 2) for item in c[p1] if item in c[p2]])

    return 1 / (1 + math.sqrt(sumOfSquares))

# 皮尔逊相关度
# 
# 返回值在-1～1之间，为1时表示两个人对每一样物品有一致的评价
def simPearson(c, p1, p2):
    si = {}
    for item in c[p1]:
        if item in c[p2]:
            si[item] = 1

    n = len(si)

    if n == 0:
        return 1
    
    # 对所有偏好求和
    sum1 = sum(c[p1][item] for item in si)
    sum2 = sum(c[p2][item] for item in si)

    # 求平方和
    sum1Sq = sum([pow(c[p1][item], 2) for item in si])
    sum2Sq = sum([pow(c[p2][item], 2) for item in si])

    # 求乘积之和
    pSum = sum([c[p1][item] * c[p2][item] for item in si])

    # 计算皮尔逊价值
    num = pSum - (sum1 * sum2 / n)
    den = math.sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    
    r = num / den

    return r

# 最佳匹配
def topMatches(c, p, n = 4, similarity = simPearson):
    scores = [(similarity(c, p, o), o) for o in c if o != p]

    scores.sort()
    scores.reverse()
    return scores[0:n]

# 利用加权平均，提供建议
def getRecommendations(c, p, similarity = simPearson):  
    totals = {}
    simSums = {}

    for o in c:
        if o == p:
            continue
        sim = similarity(c, p, o)
    
        # 忽略价值小于等于零的情况
        if sim < 0:
            continue
        
        for item in c[o]:
            if item not in c[p] or c[p][item] == 0:
                # 相似度，评价值
                totals.setdefault(item, 0)
                totals[item] += c[o][item] * sim

                # 相似度之和
                simSums.setdefault(item, 0)
                simSums[item] += sim
                
    # 建立一个归一化的列表
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    # 返回经过排序的列表
    rankings.sort()
    rankings.reverse()
    
    return rankings

# 键值转换
def transformsPrefs(c):
    ret = {}

    for p in c:
        for i in c[p]:
            ret.setdefault(i, {})

            # 物品和人对调
            ret[i][p] = c[p][i]

    return ret



    


