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
