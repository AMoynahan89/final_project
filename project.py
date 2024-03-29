import sqlite3
import re

# Creates a connection and curesor object which I can pass to functions that need access the database
class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.cursor = self.con.cursor()
    
    # A method to query the database
    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    # A method to commit to the database
    def commit(self):
        self.con.commit()

    # A method to close the database
    def close(self):
        self.con.close()


def main():
    db_manager = DatabaseManager("database/my_database.db")
    
    # Login
    user_response = input("Do you have an account? (yes/no): ").lower()
    while user_response not in ["yes", "no"]:
        print("Please answer with 'yes' or 'no'.")
        user_response = input("Do you have an account? (yes/no): ").lower()
    if user_response == "yes":
        user = login_user(db_manager)
    else:
        user = create_new_user(db_manager)
    #print(user)

    # Main Functionality
    user_id = get_user_id(db_manager, user)
    #print(user_id)
    save_data(user_id)
    #search_data():
    #just_chat()
    db_manager.close()


def create_new_user(db_manager):
    while True:
        print("Create New Account")
        username = validate_credentials("username")
        password = validate_credentials("password")
        if not credentials_exist(db_manager, username):
            db_manager.execute_query("INSERT INTO users (username, password) VALUES(?, ?)", (username, password))
            db_manager.commit()
            return username
        else:
            print(f"The username {username} is already taken. Please chose a different username.")


def login_user(db_manager):
    while True:
        print("Log In")
        username = validate_credentials("username")
        password = validate_credentials("password")
        if credentials_exist(db_manager, username, password):
            return username
        #potentially else block with error message here


# Assures credentials meet regex requirements. Returns users credentials
def validate_credentials(credential_type):
    while True:
        credentials = input(f"Enter your {credential_type}: ")
        if re.fullmatch(r"([a-z0-9_]+)", credentials, re.IGNORECASE):
            return credentials
        else:
            print(f"Invalid {credential_type}. Please use one or more characters, letters, numbers, or underscores only.")


# Checks if entered credentials are in the database already. Returns a Bool value.
def credentials_exist(db_manager, username, password=None):
    if password:
        query = "SELECT username FROM users WHERE username = ? AND password = ?"
        params = [username, password]
    else:
        query = "SELECT username FROM users WHERE username = ?"
        params = [username]
    
    user = db_manager.execute_query(query, params)
    if user:
        return True  # User exists (and, if provided, password matches)
    else:
        return False  # User does not exist (or password does not match if provided)


def get_user_id(db_manager, user):
    print(user)
    user_id = db_manager.execute_query("SELECT user_id FROM users WHERE username = ?", [user])
    return user_id


if __name__ == "__main__":
    main()


def save_data():


#def search_data():


#def just_chat():








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


#Populates "question_answers" table.
#cursor.execute("""
#    INSERT INTO question_answers (user_id, question, answer) VALUES
#    (1, 'Where did you grow up?', 'New York'),
#    (1, 'How many siblings do you have?', '2'),
#    (1, 'What is your favorite hobby?', 'Reading'),
#    (2, 'Where did you grow up?', 'Los Angeles'),
#    (2, 'How many siblings do you have?', '1'),
#    (2, 'What is your favorite hobby?', 'Cooking'),
#    (3, 'Where did you grow up?', 'Chicago'),
#    (3, 'How many siblings do you have?', '3'),
#    (3, 'What is your favorite hobby?', 'Gardening'),
#    (4, 'Where did you grow up?', 'Houston'),
#    (4, 'How many siblings do you have?', '4'),
#    (4, 'What is your favorite hobby?', 'Painting'),
#    (5, 'Where did you grow up?', 'Miami'),
#    (5, 'How many siblings do you have?', '0'),
#    (5, 'What is your favorite hobby?', 'Playing guitar')
#""")

#con.commit()


#result = cursor.execute("SELECT name FROM sqlite_master")
#print(result.fetchall())
    

#Populates "users" table.
#cursor.execute("INSERT INTO users (username, password) VALUES('user1', 'password1')")
