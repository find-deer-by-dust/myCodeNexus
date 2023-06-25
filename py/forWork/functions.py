import pandas as pd
import numpy as np
import time
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook
from openpyxl import Workbook,load_workbook
from openpyxl.styles import *

class function:
    def adjustFormat(fl,tag):
        workbook = load_workbook(filename=fl)
        sheet = workbook.active
        s="QAZWSXEDCRFVTGBYHNUJMIOPKL"
        for item in s:
            colD = sheet[item]
            for c in colD:
        # max_rows = sheet.max_row  # 获取最大行
        # max_columns = sheet.max_column  # 获取最大列   
        # for i in range(1,max_rows+1):
        #     for j in range(1,max_columns+1):
        #         c=sheet.cell(i, j)
                if tag==1:
                     align=Alignment(horizontal='left',vertical='center',wrapText=True)
                else:
                    align=Alignment(horizontal='left',vertical='center')
                font = Font(name="微软雅黑",size=10)    
                border=Border(left=Side(style='thin'),  bottom=Side(style='thin'), right=Side(style='thin'),top=Side(style='thin'))
                
                c.font = font
                c.border = border
                c.alignment = align
        workbook.save(filename=fl)

    def toPercent(fl):
        workbook = load_workbook(filename=fl)
        sheet = workbook.active
        tmp=sheet['D']
        for i in tmp:
            if i.value!=2:
                data= i.value
                data = float('%.4f' % (float(data)))
                i.value = data
                i.number_format = '0.00%'

        workbook.save(filename=fl)