import sqlite3

conn = sqlite3.connect("***/***.db")

query = conn.cursor()

sql = "SELECT * FROM users"
