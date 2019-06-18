import sqlite3

#Create connection
conn = sqlite3.connect("***/***.db")

#Create cursor
query = conn.cursor()

#Writte a query
sql = """
CREATE TABLE users
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (10),
    age INTEGER
    )
"""

#Execute query
if (query.execute(sql)):
    print("Table created successfully")
else:
    print("An error has ocurred")

#Close route
query.close()

#Save changes
conn.commit()

#Close connection
conn.close()
