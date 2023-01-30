import os
import openpyxl

wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.active
list(sheet.columns)[0]

for cellObj in list(sheet.columns)[0]:
    os.system("echo %s"%cellObj.value.replace("/", "_"))
    os.system("echo done loop %s"%cellObj.value.replace("/", "_"))
#os.system("ls -l")