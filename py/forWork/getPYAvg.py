import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook

from functions import *

basicFN=function.getmyCodeNexusPath("/py/forWork")
tmpFN=basicFN+"/doc/tmp.xlsx"
dictFN=basicFN+"/doc/dict.xlsx"
sortFN=basicFN+"/doc/sort.xlsx"
imFN=basicFN+"/doc/im.xlsx"

# 第一行需要属性栏
table = pd.read_excel(io=tmpFN)
table = np.array(table)
table = table.tolist()
length = len(table)

for i in range(length):
    table[i][0]=table[i][0].replace(" ","").replace("新","").replace("-随堂测","随堂测")
    
df = pd.DataFrame(table)
df = df.sort_values(by=0,ascending=True)
df.to_excel(tmpFN, index=False)

function.toPercent(tmpFN,'CD')
function.adjustFormat(tmpFN,1)

