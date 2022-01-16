import openpyxl
from datetime import datetime

def write(from_value,to_value,size,output):
    date_time = datetime.fromtimestamp(1887639468)
    wrkbk = openpyxl.load_workbook("Database.xlsx")
    sheet = wrkbk.active
    max_row=sheet.max_row
    sheet['A'+str(max_row+1)]=from_value
    sheet['B'+str(max_row+1)]=to_value
    sheet['C'+str(max_row+1)]=size
    sheet['D'+str(max_row+1)]=output
    sheet['E'+str(max_row+1)]=date_time
    wrkbk.save('Database.xlsx')

