import sqlite3

name = input("Writte name: ")

age = input("Writte age: ")

try:
    age = int(age)
except ValueError:
    print("This value is not a number")
    exit()

#Create connection to database
conn = sqlite3.connect("***/***.db")

#Create cursor
query = conn.cursor()

#Create arguments
arguments = (name, age)

#Create query
sql = """
INSERT INTO users (name, age)
VALUES (?, ?)
"""

#Execute query
if (query.execute(sql, arguments)):
    print("Record saved successfully")
else:
    print("An error has ocurred")

#Close cursor
query.close()

#Save changes
conn.commit()

#Close connection
conn.close()
