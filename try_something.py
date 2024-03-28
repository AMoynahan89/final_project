import sqlite3

con = sqlite3.connect("database\my_database.db")

cursor = con.cursor()

#Add program code here



#result = cursor.execute("SELECT name FROM sqlite_master")
#print(result.fetchall())

result = cursor.execute("SELECT user_id, username, password FROM Users")
print(result.fetchall())

#result = cursor.execute("SELECT user_id, question FROM question_answers")
#print(result.fetchall())

con.close()


# Old code here

#def credentials_exist(username, db_manager):
#        users = db_manager.execute_query("SELECT username FROM users")
#        usernames = [user[0] for user in users]
#        if username in usernames:
#            return True
#        else:
#            return False