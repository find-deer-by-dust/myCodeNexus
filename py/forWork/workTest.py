import pandas
import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook
import time
import webbrowser
from desktopmagic.screengrab_win32 import getRectAsImage
from pymouse import *

from functions import *

basicFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/"
tmpFN= basicFN+"doc/tmp.xlsx"
dictFN=basicFN+"doc/dic.xlsx"
sortFN=basicFN+"doc/sort.xlsx"
pngPath=basicFN+"png/"

table = pd.read_excel(io=tmpFN)
table = np.array(table)
table = table.tolist()
length = len(table)
m = PyMouse() 
j=0

for i in table:
    fn=str(i[0])+'.png'
    url=i[2]
    webbrowser.open(url)
    time.sleep(5)
    m.click(3810, 422, 1, 1)
    rect = getRectAsImage((2310,-600,4468,471))
    rect.save(pngPath+fn, format='png')
    break



time.sleep(5)
rect = getRectAsImage((1920,-917,4479,522))
rect.save(pngPath+'test'+'.png', format='png')
