import pandas
import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook

from functions import *

tmpFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/doc/tmp.xlsx"
wopFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/doc/wop.xlsx"

# 第一行需要属性栏
table = pd.read_excel(io=tmpFN)
table = np.array(table)
table = table.tolist()
length = len(table)
tableDic = dict()

for i in table:
    if i[0] not in tableDic and str(i[1])!='nan':
        tableDic[i[0]] = i[1]
    
for i in table:
    if i[0] in tableDic and str(i[1])=='nan':
        i[1]=tableDic[i[0]]

df = pd.DataFrame(table)
df.to_excel(wopFN, index=False)
function.adjustFormat(wopFN,1)