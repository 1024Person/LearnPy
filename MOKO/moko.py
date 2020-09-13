import pymysql

db = pymysql.connect("localhost", "root", "1234", "tz_db");
cursor = db.cursor()
cursor.execute("SELECT * from student")
data = cursor.fetchone()
while data:
    print(data)
    data = cursor.fetchone()

db.close()
