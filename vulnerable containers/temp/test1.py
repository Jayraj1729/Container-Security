import openpyxl
import os




wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.active
list(sheet.columns)[0]

for cellObj in list(sheet.columns)[0]:
    os.system("grype %s >result1/%s.txt"% (cellObj.value, cellObj.value.replace("/","_")))
    os.system("docker rmi %s"%cellObj.value)
   #print(cellObj.value)