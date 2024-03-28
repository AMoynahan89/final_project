import sqlite3

con = sqlite3.connect("database\my_database.db")

cursor = con.cursor()

#Add program code here



#result = cursor.execute("SELECT name FROM sqlite_master")
#print(result.fetchall())

result = cursor.execute("SELECT user_id, username FROM Users")
print(result.fetchall())

result = cursor.execute("SELECT user_id, question FROM question_answers")
print(result.fetchall())

con.close()
