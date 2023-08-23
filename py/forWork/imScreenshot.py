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

# 在im后台截图

# 第一行需要属性栏
basicPath=function.getmyCodeNexusPath("/py/forWork")
tmpPath=basicPath+"/doc/tmp.xlsx"
dictPath=basicPath+"/doc/dict.xlsx"
sortPath=basicPath+"/doc/sort.xlsx"
imPath=basicPath+"/doc/im.xlsx"
pngPath=basicPath+"/png/"

os.system("cd C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/png && del * /q")

table = pd.read_excel(io=imPath)
table = np.array(table)
table = table.tolist()
length = len(table)
inMiddleXY=(4565,500)


#玄学问题，先用这个移动到副屏再解决
pyautogui.click(inMiddleXY)

for i in range(length):
    fn=str(table[i][0])
    url=table[i][2]
    webbrowser.open(url)
    time.sleep(10)
    function.screenshot(fn)
    print(str(i+1)+'/'+str(length)+"\t"+str(int((str((i+1)/length)+'0000')[2:4]))+"%")

