import sqlite3

conn = sqlite3.connect('attendance.db')

cursor = conn.cursor()

cursor.execute("DELETE FROM attendance")
cursor.execute("DELETE FROM employees")

conn.commit()

print("Employees deleted:", cursor.rowcount)

conn.close()

print("All employees deleted successfully!")