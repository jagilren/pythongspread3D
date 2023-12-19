import random
import pyodbc
from datetime import datetime, timedelta
from decimal import Decimal
import BoundaryHours
def traeHorasAdicionales():
    global cursor, conn
    try:
        conn = pyodbc.connect('DSN=access2003DSN;')
        # Create a cursor
        cursor = conn.cursor()
        outlaw = -1
        HoraInicial, HoraFinal= BoundaryHours.ConsigueHoras()
        # Execute a SQL query
        query = f'''SELECT [HorasAdicionales].Habitacion, [HorasAdicionales].Concepto, [HorasAdicionales].Fecha, [HorasAdicionales].Cantidad, [HorasAdicionales].Importe
        FROM [HorasAdicionales] 
        WHERE [HorasAdicionales].Fecha BETWEEN #{HoraInicial}# AND #{HoraFinal}# 
        ORDER BY [HorasAdicionales].Fecha DESC'''
        cursor.execute(query)
        list_of_tuples = cursor.fetchall()
        print(f'rows= {list_of_tuples}')
        list_of_lists = [list(t) for t in list_of_tuples]
        print(f'flattened_data= {list_of_lists}')
        for fila in list_of_tuples:
            pass
            #print(f'filas: {fila[0]}')
    except:
        facturaNumero=None
    else:
        cursor.close()
        conn.close()
    finally:
        pass
    return list_of_lists

#ultima = traeHorasAdicionales()
