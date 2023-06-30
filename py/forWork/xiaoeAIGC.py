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

basicFN="C:/Users/Administrator/Desktop/code/for-now-coder/py/forWork/"
testFN= basicFN+"doc/test.txt"
with open("1.txt", "r", encoding='utf-8') as f: 
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
pyperclip.copy(text)