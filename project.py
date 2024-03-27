import sqlite3
import re


def main():
    user_response = input("Do you have an account? (yes/no): ").lower()
    while user_response not in ["yes", "no"]:
        print("Please answer with 'yes' or 'no'.")
        user_response = input("Do you have an account? (yes/no): ").lower()
    
    if user_response == "yes":
        login_user()
    else:
        create_new_user()


def validate_credentials(credential_type):
    while True:
        credentials = input(f"Enter your {credential_type}: ")
        if re.fullmatch(r"([a-z0-9_]+)", credentials, re.IGNORECASE):
            return credentials
        else:
            print(f"Invalid {credential_type}. Please use one or more characters, letters, numbers, or underscores only.")
    

def create_new_user():
    print("Create New Account")
    username = validate_credentials("username")
    password = validate_credentials("password")
    # Add code here to insert new user into database if they don't already exist


def login_user():
    print("Log In")
    username = validate_credentials("username")
    password = validate_credentials("password")
    # Add code here to check if user credentials are already in database


def add_new_user(username, password):
    with sqlite3.connect("database/my_database.db") as con:
        cursor = con.cursor()
        username = cursor.execute("SELECT username FROM users")
        users = username.fetchall()
        usernames = [user[0] for user in users]
        if username in usernames:
            print(f"{username} is a registered user.", end="")
        else:
            print(f"{username} is not a registered user.", end="")


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


def add_user_data():
    pass


def recall_user_data():
    pass


if __name__ == "__main__":
    main()


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
            
#result = cursor.execute("SELECT name FROM sqlite_master")
#print(result.fetchall())