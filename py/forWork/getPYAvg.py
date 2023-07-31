import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook

from functions import *

# 坏,忘了

basicPath=function.getmyCodeNexusPath("/py/forWork")
tmpPath=basicPath+"/doc/tmp.xlsx"
dictPath=basicPath+"/doc/dict.xlsx"
sortPath=basicPath+"/doc/sort.xlsx"
imPath=basicPath+"/doc/im.xlsx"

# 第一行需要属性栏
table = pd.read_excel(io=tmpPath)
table = np.array(table)
table = table.tolist()
length = len(table)

for i in range(length):
    table[i][0]=table[i][0].replace(" ","").replace("新","").replace("-随堂测","随堂测")
    
df = pd.DataFrame(table)
df = df.sort_values(by=0,ascending=True)
df.to_excel(tmpPath, index=False)

function.toPercent(tmpPath,'CD')
function.adjustFormat(tmpPath,1)

