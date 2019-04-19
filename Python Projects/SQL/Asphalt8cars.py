
import sqlite3

connection = sqlite3.connect("Asphalt8cars.sql")
cursor = connection.cursor()
cursor.execute("SELECT MODEL, BRAND FROM CARS;")
results = cursor.fetchall()
for r in results:
    print(r)
cursor.close()
connection.close()
