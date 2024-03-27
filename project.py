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


def create_new_user():
    while True:
        print("Create New Account")
        username = validate_credentials("username")
        password = validate_credentials("password")
        if not check_username_exists(username):
            # Decided to create a DatabaseManager Class to deal with all of the SQL operations and be able to create a cursor object onece for the whole program
            cursor.execute("INSERT INTO users (username, password) VALUES(?, ?)", (username, password))


def login_user():
    while True:
        print("Log In")
        username = validate_credentials("username")
        password = validate_credentials("password")
        if not check_username_exists(username):
            # Decided to create a DatabaseManager Class to deal with all of the SQL operations and be able to create a cursor object onece for the whole program
            cursor.execute("INSERT INTO users (username, password) VALUES(?, ?)", (username, password))


# Returns standardized username/password
def validate_credentials(credential_type):
    while True:
        credentials = input(f"Enter your {credential_type}: ")
        if re.fullmatch(r"([a-z0-9_]+)", credentials, re.IGNORECASE):
            return credentials
        else:
            print(f"Invalid {credential_type}. Please use one or more characters, letters, numbers, or underscores only.")


def check_username_exists(username):
    with sqlite3.connect("my_database.db") as con:
        cursor = con.cursor()
        cursor.execute("SELECT username FROM users")
        users = cursor.fetchall()
        usernames = [user[0] for user in users]
        if username in usernames:
            return True
        else:
            return False


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


#Populates "users" table.
cursor.execute("INSERT INTO users (username, password) VALUES('user1', 'password1')")
