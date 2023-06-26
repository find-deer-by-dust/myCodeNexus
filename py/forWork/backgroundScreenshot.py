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
import pyperclip

from functions import *

# 第一行需要属性栏
basicFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/"
tmpFN= basicFN+"doc/tmp.xlsx"

os.system("cd C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/png && del * /q")


startXY=(4930,-427)
endXY=(4930,385)

firstPageXY=(2500,-1075)
closePageXY=(3010,-1075)
openProjectXY=(4250,-500)
inMiddleXY=(4565,500)
urlXY=(3000,-1025)
stepLength=(endXY[1]-startXY[1])/9
students=list()

times=10
#玄学问题，先用这个移动到副屏再解决
#需要拖动到页面最下面
pyautogui.moveTo(inMiddleXY)
tag='1'

while tag=='1':
    pyautogui.moveTo(inMiddleXY)
    for i in range(times):
        print(str(i+1)+'/'+str(times))
        pyautogui.click(startXY[0],startXY[1]+i*stepLength)
        time.sleep(5)
        pyautogui.click(openProjectXY)
        time.sleep(5)
        pyautogui.click(urlXY)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        url=pyperclip.paste()
        fn=url.split(r"%2F")[4]
        if fn not in students:
            students.append(fn)
            function.screenshot(fn)
        time.sleep(1)
        pyautogui.click(closePageXY)
        time.sleep(0.5)
        pyautogui.click(firstPageXY)
        
    tag=input("输入1以继续，同时记得切换页面并滑到最下方\n")
    df = pd.DataFrame(students)
    df.insert(1, '1', [1]*len(df))
    df = df.sort_values(by=0,ascending=False)
    df.to_excel(tmpFN, index=False)