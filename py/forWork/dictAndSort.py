import pandas
import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook

from functions import *

tmpFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/doc/tmp.xlsx"
dictFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/doc/dict.xlsx"
sortFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/doc/sort.xlsx"

# 第一行需要属性栏
table = pd.read_excel(io=tmpFN)
table = np.array(table)
table = table.tolist()
length = len(table)
tableDic = dict()
tag = 0

for i in range(len(table)):
    table[i][2] = table[i][2].replace('\n', '').replace(' ', '')

for i in table:
    if i[2] not in tableDic:
        tableDic[i[2]] = 1
    else:
        tableDic[i[2]] = tableDic[i[2]] + 1

tableList = list(zip(list(tableDic), list(tableDic.values())))


i = 0
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
        if (j[0]=='pad' or j[0]=='Mac OS')and j[2]==tableList[i][0]:
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
    if i[2] not in tableDic:
        tableDic[i[2]] = tag
        tag = tag+1
for i in range(len(table)):
    table[i][1] = tableDic[table[i][2]]

df = pd.DataFrame(table)
df.to_excel(dictFN, index=False)

function.adjustFormat(dictFN)
function.adjustFormat(sortFN)



