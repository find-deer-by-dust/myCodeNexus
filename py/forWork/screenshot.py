import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook
import time
import webbrowser
from desktopmagic.screengrab_win32 import getRectAsImage
import pyautogui
import os

from functions import *

# 第一行需要属性栏
basicFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/"
tmpFN= basicFN+"doc/tmp.xlsx"
dictFN=basicFN+"doc/dic.xlsx"
sortFN=basicFN+"doc/sort.xlsx"
pngPath=basicFN+"png/"
os.system("cd C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/png && del * /q")

table = pd.read_excel(io=tmpFN)
table = np.array(table)
table = table.tolist()
length = len(table)

openPageXY=(4565,500)
closePageXY=(3010,-1075)
clickOkToLeaveXY=(4000,-850)

pyautogui.click(openPageXY)
pyautogui.click(closePageXY)
for i in range(length):
    fn=str(table[i][0])
    url=table[i][2]
    webbrowser.open(url)
    time.sleep(10)
    pyautogui.click(openPageXY)
    function.screenshot(fn)
    pyautogui.click(closePageXY)
    pyautogui.click(clickOkToLeaveXY)
    
    print(str(i+1)+'/'+str(length)+"\t"+str(int(str((i+1)/length)[2:4]))+"%")

