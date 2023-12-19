from datetime import datetime
import gspread
import randomtime,queryTable, BoundaryHours, updateTable
from decimal import Decimal

gc = gspread.service_account()
current_datetime= datetime.now()
#formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
serial_number = []

values=queryTable.traeHorasAdicionales()
updateops=updateTable.updateHorasAdicionalesgspread()
for fila in values:
    current_datetime = randomtime.get_random_datetime_in_current_month()
    time_serial = (fila[2] - datetime(1899, 12, 30)).total_seconds() / (60 * 60 * 24)
    fila[2] = time_serial
    fila[4] = int(fila[4])
    print(f'FilaModificada={fila}')

print(f'{values}')
spreadsheet = gc.open_by_key('15n-wRKlL8rON3zxyMinhbEx3TicfCZ2Vawhmzpg_gCY')
#spreadsheet = gc.open("Horas Adicionales")

sheet_name = '3DSuite'
worksheet = spreadsheet.worksheet(sheet_name)
# Insert a new row at the top of the sheet
worksheet.insert_rows(values, row=2)  # Adjust the index as needed

# worksheet.insert_row(values, row=1, value_input_option='RAW')

print(worksheet.get('A2'))
#gc.logout()