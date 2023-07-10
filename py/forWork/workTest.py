import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook
import re
from functions import *

basicFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/"
tmpFN= basicFN+"doc/tmp.xlsx"
pyimFN=basicFN+"doc/pyim.xlsx"

# 第一行需要属性栏
table = pd.read_excel(io=tmpFN)
table = np.array(table)
table = table.tolist()
length = len(table)
tableSet = set()

i=0
while i <len(table):
    if table[i][2]!='Windows':
        table.pop(i)
        i-=1
    i+=1

length = len(table)

for i in range(length):
    name=table[i][0][:table[i][0].find('-')+2]
    tmp=[]
    tmp.append(name)
    table[i]=tmp+table[i]
    if name not in tableSet:
        tableSet.add(name)

newTable=list(tableSet)
newTable.sort()

for i in range(len(newTable)):
    tmp=['0']*10
    tmp[0]=newTable[i]
    newTable[i]=tmp

for i in table:
    num=int(i[4])
    name=i[2].replace(".xpy3",'')
    tmp= re.sub(u"([^\u0030-\u0039])", "", name)
    if name in i[1]:
        tag=8
    elif tmp!='':
        tag=int(tmp)+1
    else:
        tag=1
    for j in range(len(newTable)):
        if newTable[j][0]==i[0]:
            newTable[j][tag]=int(newTable[j][tag])+num
            break

for i in range(len(newTable)):
    sum=0
    for j in range(8):
        sum+=int(newTable[i][j+1])
    newTable[i][9]=sum

df = pd.DataFrame(newTable)
df.to_excel(pyimFN, index=False)
function.adjustFormat(pyimFN,1)