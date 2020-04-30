from openpyxl import load_workbook

wb = load_workbook("Lesson_10.xlsx")

source = wb["Sheet"]

new_sheet = wb.copy_worksheet(source)
new_sheet.title = "Copy of Sheet"

wb.save("Lesson_10.xlsx")

for sheet in wb:
    print(sheet.title)