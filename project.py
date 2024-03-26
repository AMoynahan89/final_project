import sqlite3
import re

def main():
    current_user = input("Enter user name: ")
    current_user_password = input("Enter password: ")
    get_or_create_user(current_user, current_user_password)
    #add_user_data()
    #recall_user_data()

def get_or_create_user(current_user, current_user_password):
    with sqlite3.connect("database/my_database.db") as con:
        cursor = con.cursor()
        username = cursor.execute("SELECT username FROM users")
        users = username.fetchall()
        usernames = [user[0] for user in users]
        if current_user in usernames:
            print(f"{current_user} is a registered user.", end="")
        else:
            print(f"{current_user} is not a registered user.", end="")


#Creates the "users" table.
#cursor.execute("""
#    CREATE TABLE users(
#    user_id INTEGER PRIMARY KEY,
#    username TEXT NOT NULL,
#    password TEXT NOT NULL
#    )
#""")


#Populates "users" table.
#cursor.execute("""
#    INSERT INTO users (username, password) VALUES
#    ('user1', 'password1'),
#    ('user2', 'password2'),
#    ('user3', 'password3'),
#    ('user4', 'password4'),
#    ('user5', 'password5')
#""")

#con.commit()


def add_user_data():
    pass


def recall_user_data():
    pass


if __name__ == "__main__":
    main()
