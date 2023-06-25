import pandas
import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook

from functions import *

basicFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/"
tmpFN= basicFN+"doc/tmp.xlsx"
imFN=basicFN+"doc/im.xlsx"

table = pd.read_excel(io=tmpFN)
table = np.array(table)
table = table.tolist()
tableSet=set()


for i in range(len(table)):
    table[i][0] = table[i][2].split(r"%2F")[4]
for i in range(len(table)):
    table[i][1] = table[i][4]
for i in range(len(table)):
    table[i].pop(3)
    table[i].pop(3)
    table[i].pop(3)

i=len(table)-1
while i>-1:
    if table[i][0] not in tableSet:
        tableSet.add(table[i][0])
    else:
        table.pop(i)
        # i=i+1
    i=i-1


# print(table[0][0])
df = pd.DataFrame(table)
# print(df)
df = df.sort_values(by=0,ascending=False)
df.to_excel(imFN, index=False)

function.adjustFormat(imFN,0)