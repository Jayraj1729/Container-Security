import openpyxl
import os




wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.active
list(sheet.columns)[0]

for cellObj in list(sheet.columns)[0]:
    os.system("docker rmi %s"%cellObj.value)
   #print(cellObj.value)