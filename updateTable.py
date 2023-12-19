import random
import pyodbc
from datetime import datetime, timedelta
from decimal import Decimal
import BoundaryHours
def updateHorasAdicionalesgspread():
    global cursor, conn
    try:
        conn = pyodbc.connect('DSN=access2003DSN;')
        # Create a cursor
        cursor = conn.cursor()
        outlaw = -1
        HoraInicial, HoraFinal= BoundaryHours.ConsigueHoras()
        # Execute a SQL query
        query = f'UPDATE [HorasAdicionales] SET [HorasAdicionales].gspreaded = -1  WHERE [HorasAdicionales].Fecha BETWEEN #{HoraInicial}# AND #{HoraFinal}#'
        cursor.execute(query)
        conn.commit()
    except:
        facturaNumero=None
    else:
        cursor.close()
        conn.close()
    finally:
        pass
    return None

#ultima = traeHorasAdicionales()
