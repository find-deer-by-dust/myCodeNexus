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

#玄学问题，先用这个移动到副屏再解决
#需要拖动到页面最下面
pyautogui.moveTo(4565,500)
startXY=(4930,-427)
endXY=(4930,385)
closePageXY=(3010,-1075)
openProjectXY=(4250,-500)

stepLength=(endXY[1]-startXY[1])/9

pyautogui.moveTo(4250,-500)
# for i in range(10):
#     time.sleep(1)
#     pyautogui.moveTo(startXY[0],startXY[1]+i*stepLength)