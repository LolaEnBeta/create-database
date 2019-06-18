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
