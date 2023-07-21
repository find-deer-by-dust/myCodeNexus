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

basicFN=function.getmyCodeNexusPath("/py/forWork")
tmpFN=basicFN+"/doc/tmp.xlsx"
dictFN=basicFN+"/doc/dict.xlsx"
sortFN=basicFN+"/doc/sort.xlsx"
imFN=basicFN+"/doc/im.xlsx"
testFN= basicFN+"/doc/test.txt"
resultFN= basicFN+"/doc/result.txt"

with open(testFN, "r", encoding='utf-8') as f: 
    text = f.read() 

while True:
    a=text.find('（')
    b=text.find('）')
    if a!=-1 and b!=-1:
        text=text[:a]+text[b+1:]
    else:
        break

while True:
    a=text.find('【')
    b=text.find('】')
    if a!=-1 and b!=-1:
        text=text[:a]+text[b+1:]
    else:
        break

text=text.replace("～","~")
text=text[text.find('：')+1:]
text=text[text.find('：')+2:]
text="AI创想家，开启AI新探索~\n\n"+text
text=text.strip()
pyperclip.copy(text)
with open(resultFN,'w+',encoding='utf-8') as f:
   f.write(text)