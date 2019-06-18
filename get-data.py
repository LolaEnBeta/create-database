import sqlite3

conn = sqlite3.connect("***/***.db")

query = conn.cursor()

sql = "SELECT * FROM users"

#Execute query
if (query.execute(sql)):
    filas = query.fetchall()
    for fila in filas:
        print(fila[0], fila[1], fila[2])
else:
    print("An error has ocurred")
