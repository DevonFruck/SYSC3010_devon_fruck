#This is Python3 code

import sqlite3

#connect to database file
dbconnect = sqlite3.connect("mydatabase.db")

#set row factory to sqlite3.row class to access columns
dbconnect.row_factory = sqlite3.Row

#creating cursor to work with db
cursor = dbconnect.cursor()
cursor.execute('SELECT * FROM sensors WHERE type="door"')

for row in cursor:
    print(row['sensorID'], row['type'], row['zone'])
    
print() #space between the differnt prints

cursor.execute('SELECT * FROM sensors WHERE zone="kitchen"')
for row in cursor:
    print(row['sensorID'], row['type'], row['zone'])

#close connection
dbconnect.close()
