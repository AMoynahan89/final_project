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


# Old code below

#def credentials_exist(username, db_manager):
#        users = db_manager.execute_query("SELECT username FROM users")
#        usernames = [user[0] for user in users]
#        if username in usernames:
#            return True
#        else:
#            return False


#def get_or_create_user(username, password):
#    with sqlite3.connect("database/my_database.db") as con:
#        cursor = con.cursor()
#        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
#        result = cursor.fetchone()
#        if result:
#            if result[0] == password:
#                print(f"{username}, you are logged in!")
                # Continue to the main program
#            else:
#                print("Incorrect password.")
#        else:
#            print(f"{username} does not exist. Creating account...")
#            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#            con.commit()
#            print("Account created. Please log in.")

