import numpy as np
import pandas as pd


def getStrongAssociationRules(a, b):
    aNum = 0
    bNum = 0
    for deal in data:
        aInDeal = True
        for aItem in a:
            aInDeal = aInDeal and (deal[aItem] == 1)
        if aInDeal:
            aNum = aNum+1
            bInDeal = True
            for bItem in b:
                bInDeal = bInDeal and (deal[bItem] == 1)
            if bInDeal:
                bNum = bNum+1
    if (bNum/aNum > degreeOfConfidence):
        print(str(a)+'->'+str(b))
        print(bNum/aNum)


data = [[1, 1, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0],
        ]

degreeOfConfidence = 0.5
support = 2
numberOfDeals = len(data)
numberOfGoods = len(data[0])
numberOfItem = 1

tmpList = []
supList = []
listOfTmpList = []
for i in range(numberOfGoods):
    tmp = []
    tmp.append(i)
    tmpList.append(tmp)

for i in range(len(tmpList)):
    sup = 0
    for j in data:
        tmp = True
        for t in tmpList[i]:
            tmp = tmp and (j[t] == 1)
        if (tmp == True):
            sup = sup + 1
    supList.append(sup)

while (i < len(supList)):
    if (supList[i] < support):
        supList.remove(supList[i])
        tmpList.remove(tmpList[i])
        i = i-1
    i = i+1

tmpListCopy = tmpList.copy()
listOfTmpList.append(tmpListCopy)

while (len(listOfTmpList[len(listOfTmpList)-1]) != 0):
    numberOfItem = numberOfItem + 1
    usedSet = set()
    for i in tmpList:
        for j in i:
            usedSet.add(j)

    length = len(tmpList)
    for i in range(length):
        for j in usedSet:
            if j not in tmpList[i]:
                z = tmpList[i]+[j]
                z.sort()
                if z not in tmpList:
                    tmpList.append(z)

    i = 0
    while (i < len(tmpList)):
        if (len(tmpList[i]) != numberOfItem):
            tmpList.remove(tmpList[i])
            i = i-1
        i = i+1

    if (len(tmpList[0]) != 1):
        df = pd.DataFrame(tmpList)
        df.drop_duplicates(inplace=True)
        tmpList = df.values.tolist()

    supList = []
    for i in range(len(tmpList)):
        sup = 0
        for j in data:
            tmp = True
            for t in tmpList[i]:
                tmp = tmp and (j[t] == 1)
            if (tmp == True):
                sup = sup + 1
        supList.append(sup)
    i = 0

    while (i < len(supList)):
        if (supList[i] < support):
            supList.remove(supList[i])
            tmpList.remove(tmpList[i])
            i = i-1
        i = i+1

    tmpListCopy = tmpList.copy()
    listOfTmpList.append(tmpListCopy)

for i in listOfTmpList:
    print(i)

resultList = listOfTmpList[len(listOfTmpList)-2]
for i in resultList:
    for j in range(len(i)):
        if (j != 0):
            a = i[:j]
            b = i[j:]
            getStrongAssociationRules(a, b)
            getStrongAssociationRules(b, a)
