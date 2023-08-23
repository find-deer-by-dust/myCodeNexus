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

# xiaoeAIGC用于删减文本中非对话内容

def deleteContent(text,x,y):
    while True:
        a=text.find(x)
        b=text.find(y)
        if a!=-1 and b!=-1:
            if x in text[a+1:b] or a>b:
                print('符号不匹配')
                break
            text=text[:a]+text[b+1:]
        elif a*b<0:
            print('有剩余符号')
            break
        else:
            break
    return text

basicPath=function.getmyCodeNexusPath("/py/forWork")
tmpPath=basicPath+"/doc/tmp.xlsx"
dictPath=basicPath+"/doc/dict.xlsx"
sortPath=basicPath+"/doc/sort.xlsx"
imPath=basicPath+"/doc/im.xlsx"
testPath= basicPath+"/doc/test.txt"
resultPath= basicPath+"/doc/result.txt"

with open(testPath, "r", encoding='utf-8') as f: 
    text = f.read() 

text=deleteContent(text,'（','）')
text=deleteContent(text,'【','】')

for i in range(5):
    text=text.replace("～"*(5-i),"~")

text=text[text.find('：')+1:]
text=text[text.find('：')+2:]
text="AI创想家，开启AI新探索~\n\n"+text
text=text.strip()
pyperclip.copy(text)
with open(resultPath,'w+',encoding='utf-8') as f:
   f.write(text)