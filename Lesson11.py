from openpyxl import load_workbook, Workbook

wb = load_workbook("Lesson_11.xlsx")

for sheet in wb:
    print(sheet.title)

ws1 = wb.worksheets[0]
ws2 = wb.worksheets[1]
#ws3 = wb[worksheets[2]]

#print("THe first sheet has the title ", ws1.title, "\nThe second sheet has the title ", ws2. title, "The third sheet has the title ", ws3.title)

print(ws1.title, ws2.title)

wb.save("Lesson_11.xlsx")

