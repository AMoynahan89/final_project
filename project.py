import sqlite3
import re


class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.cursor = self.con.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def commit(self):
        self.con.commit()

    def close(self):
        self.con.close()


def main():
    db_manager = DatabaseManager("database/my_database.db")

    user_response = input("Do you have an account? (yes/no): ").lower()
    while user_response not in ["yes", "no"]:
        print("Please answer with 'yes' or 'no'.")
        user_response = input("Do you have an account? (yes/no): ").lower()
    
    if user_response == "yes":
        login_user(db_manager)
    else:
        create_new_user(db_manager)

    #get_user_id(db_manager)

    db_manager.close()

def create_new_user(db_manager):
    while True:
        print("Create New Account")
        username = validate_credentials("username")
        password = validate_credentials("password")
        if not check_username_exists(username, db_manager):
            db_manager.execute_query("INSERT INTO users (username, password) VALUES(?, ?)", (username, password))
            db_manager.commit()
            print(db_manager.execute_query("SELECT username FROM users"))
            break


def login_user(db_manager):
    while True:
        print("Log In")
        username = validate_credentials("username")
        password = validate_credentials("password")
        if credentials_exist(db_manager, username, password=None):
            db_manager.execute_query("INSERT INTO users (username, password) VALUES(?, ?)", (username, password))
            break


# Returns standardized username/password
def validate_credentials(credential_type):
    while True:
        credentials = input(f"Enter your {credential_type}: ")
        if re.fullmatch(r"([a-z0-9_]+)", credentials, re.IGNORECASE):
            return credentials
        else:
            print(f"Invalid {credential_type}. Please use one or more characters, letters, numbers, or underscores only.")


#def credentials_exist(username, db_manager):
#        users = db_manager.execute_query("SELECT username FROM users")
#        usernames = [user[0] for user in users]
#        if username in usernames:
#            return True
#        else:
#            return False
        
def credentials_exist(db_manager, username, password=None):
    if password:
        query = "SELECT username FROM users WHERE username = ? AND password = ?"
        params = [username, password]
    else:
        # Check username only
        query = "SELECT username FROM users WHERE username = ?"
        params = [username]
    
    user = db_manager.execute_query(query, params)
    if user:
        print(user)
        return True  # User exists (and, if provided, password matches)
    else:
        print("Doesnt exist")
        return False  # User does not exist (or password does not match if provided)



def add_user_data():
    pass


def recall_user_data():
    pass


if __name__ == "__main__":
    main()


#print(db_manager.execute_query("SELECT username FROM users"))


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
#cursor.execute("INSERT INTO users (username, password) VALUES('user1', 'password1')")
