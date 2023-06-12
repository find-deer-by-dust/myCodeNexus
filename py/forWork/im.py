import pandas
import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook

from functions import *

maxTime = 180

    
table = pd.read_excel(io=r'C:\Users\Administrator\Desktop\py\doc/tmp.xlsx')
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
df.to_excel("./doc/im.xlsx", index=False)
function.adjustFormat("./doc/im.xlsx")
