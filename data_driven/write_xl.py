import openpyxl

path = "C:\\Users\\dell\\Downloads\\testcases.xlsx"

workbook= openpyxl.load_workbook(path)
sheet=workbook.active

for row in range(1,6):
    for col in range(1,4):
        sheet.cell(row=row,column=col).value="welcome"

workbook.save(path)
