import pandas
import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook

from functions import *

maxTime = 180
tmpFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/doc/tmp.xlsx"
imFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/doc/im.xlsx"

table = pd.read_excel(io=tmpFN)
table = np.array(table)
table = table.tolist()
i = 0
# print(len(table))
while i < len(table)-1:
    t = table[i][3]
    tt = table[i+1][3]
    t = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    tt = datetime.datetime.strptime(tt, "%Y-%m-%d %H:%M:%S")
    if (t-tt).total_seconds() < maxTime:
        table.pop(i)
        i = i-1
    i = i+1
# print(len(table))
for i in range(len(table)):
    table[i][0] = table[i][2].split(r"%2F")[4]
for i in range(len(table)):
    table[i][1] = table[i][4]
for i in range(len(table)):
    table[i].pop(3)
    table[i].pop(3)
    table[i].pop(3)
# print(table[0][0])
df = pd.DataFrame(table)
# print(df)
df = df.sort_values(by=0,ascending=False)
df.to_excel(imFN, index=False)

function.adjustFormat(imFN)