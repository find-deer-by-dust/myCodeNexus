import pandas
import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook


class function:
    def adjustFormat(fl):
        workbook = load_workbook(filename=fl)
        sheet = workbook.active
        s="QAZWSXEDCRFVTGBYHNUJMIOPKL"
        for item in s:
            colD = sheet[item]
        for c in colD:
            font = Font(name="微软雅黑",size=10)    
        c.font = font
        workbook.save(filename=fl)