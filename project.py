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
    question = "Are you a carteaker? (yes/no): "
    user_response = yes_or_no(question)
    print(user_response)
   
    # User interface menu
    while True:
        print("\nHow can I help you?")
        print("1. Ask a question")
        print("2. Just chat")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            continue

    # Login
    user_response = yes_or_no("Do you have an account? (yes/no): ")
    if user_response == "yes":
        user = login_user(db_manager)
    else:
        user = create_new_user(db_manager)

    # Main Functionality
    user_id = get_user_id(db_manager, user)
    print(user_id)
    #save_data(db_manager, user_id)
    #search_data(db_manager, user_id):
    #just_chat()
    db_manager.close()

def yes_or_no(question):
    user_response = input(question).lower()
    while user_response not in ["yes", "no"]:
        print("Please answer with 'yes' or 'no'.")
        user_response = input(question).lower()
    return user_response


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

# Returns actual user_id as int, not a tuple
def get_user_id(db_manager, user):
    print(user)
    user_id = db_manager.execute_query("SELECT user_id FROM users WHERE username = ?", [user])
    return user_id[0][0] # Ensure user_id[0][0] is used to extract the actual ID from the fetched result


#Inserts question-answer pairs into database
def save_data(db_manager, user_id):
    question = input("Enter your question: ")
    answer = input("Enter the answer: ")
    db_manager.execute_query("INSERT INTO question_answers (user_id, question, answer) VALUES (?, ?, ?)", (user_id, question, answer))
    db_manager.commit()


def search_data(db_manager, user_id):
    question = input("Enter your question: ")
    db_manager.execute_query("SELECT answer FROM question_answers WHERE user_id = ? AND question = ?", (user_id, question))


if __name__ == "__main__":
    main()


def search_data(db_manager, user_id):
    question = input("Enter your question: ")
    db_manager.execute_query("SELECT answer FROM question_answers WHERE user_id = ? AND question = ?")


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
    

#result = cursor.execute("SELECT name FROM sqlite_master")
#print(result.fetchall())
    

#Populates "users" table.
#cursor.execute("INSERT INTO users (username, password) VALUES('user1', 'password1')")
