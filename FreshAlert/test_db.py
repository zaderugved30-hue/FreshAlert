import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL@2026ABC",
   database="fresh_tracker_db"
)

print("Database connected successfully")

db.close()