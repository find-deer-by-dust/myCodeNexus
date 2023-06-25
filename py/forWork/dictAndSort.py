import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook

from functions import *

basicFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/"
tmpFN= basicFN+"doc/tmp.xlsx"
dictFN=basicFN+"doc/dic.xlsx"
sortFN=basicFN+"doc/sort.xlsx"

# 第一行需要属性栏
table = pd.read_excel(io=tmpFN)
table = np.array(table)
table = table.tolist()
length = len(table)
tableDic = dict()

for i in range(len(table)):
    table[i][3] = table[i][3].replace('\n', '').replace(' ', '')

for i in table:
    if i[3] not in tableDic:
        tableDic[i[3]] = 1
    else:
        tableDic[i[3]] = tableDic[i[3]] + 1

tableList = list(zip(list(tableDic), list(tableDic.values())))


# i = 0
# tableList.append(["其他", 0])
# while i < len(tableList)-1:
#     if tableList[i][1] == 1:
#         tableList[len(tableList)-1][1] = tableList[len(tableList)-1][1]+1
#         tableList.pop(i)
#         i = i-1
#     i = i+1

macsum=0
for i in range(len(tableList)):
    tmp = list()
    mac=0
    for j in table:
        if j[1]=='Windows' or j[1]=='Mac OS' or j[1]=='电脑' or str(j[1])=='1':
            j[1]='电脑'
        else :
            j[1]='pad'

        if j[1]=='pad' and j[3]==tableList[i][0]:
            mac=mac+1
    macsum=macsum+mac
    # tmp.append(i+1)
    tmp.append(tableList[i][1]-mac)
    tmp.append(mac)
    tmp.append(tableList[i][1]/length)
    tmp.append(tableList[i][0])
    tableList[i] = tmp

df = pd.DataFrame(tableList)
df = df.sort_values(by=2,ascending=False)
df.insert(0, 'a', list(range(1,len(tableList)+1)))
df.to_excel(sortFN, index=False)

print("sum:",length)
print("pc:",length-macsum)
print("mac:",macsum)


tableDic = dict()
tag = 0
for i in table:
    if i[3] not in tableDic:
        tableDic[i[3]] = tag
        tag = tag+1
for i in range(len(table)):
    table[i][2] = tableDic[table[i][3]]

df = pd.DataFrame(table)
df.to_excel(dictFN, index=False)

function.toPercent(sortFN)
function.adjustFormat(dictFN,1)
function.adjustFormat(sortFN,1)




