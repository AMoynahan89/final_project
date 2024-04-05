import sqlite3
import re


### Dtabase functionality ###

# Class for managing all database functionality
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

### User/UserProfile class ###
class User:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self._username = None
        self._password = None
        self.user_id = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    # Returns actual user_id as int, not a tuple
    def get_user_id(self):
        user_id = self.db_manager.execute_query("SELECT user_id FROM users WHERE username = ?", [self._username])
        return user_id[0][0] # Ensure user_id[0][0] is used to extract the actual ID from the fetched result


### Authentication Class/Methods ###
class Authenticator:
    def __init__(self, db_manager, user):
        self.db_manager = db_manager
        self.user = user

    # Checks if username is in database. Returns a Boolean value.
    def user_exists(self):
        query = "SELECT username FROM users WHERE username = ?"
        params = [self.user.username]
        user = self.db_manager.execute_query(query, params)
        if user is not None:
            return user
        else:
            return False
        # list comprehension

    def password_mathces(self):
        query = "SELECT password FROM users WHERE password = ?"
        params = [self.user.password]
        correct_password = self.db_manager.execute_query(query, params)
        if correct_password is not None:
            return correct_password
        else:
            return False        
        # more list comprehension

    # Potentially top level main function
    def login_user(self):
        if self.user_exists() and self.password_mathces():
            print("yay")
        else:
            print("oh no")

    def create_new_user(self):
        if not self.user_exists():
            self.db_manager.execute_query("INSERT INTO users (username, password) VALUES(?, ?)", (self.user.username, self.user.password))
            self.db_manager.commit()
            print("New user created!")
        else:
            print(f"The username {self.user.username} is already taken. Please chose a different username.")


def yes_or_no(question):
    user_response = input(question).lower()
    while user_response not in ["yes", "no"]:
        print("Please answer with 'yes' or 'no'.")
        user_response = input(question).lower()
    return user_response


def main():
    db_manager = DatabaseManager("database/my_database.db")
    user = User(db_manager)
    auth = Authenticator(db_manager, user)
    result = db_manager.execute_query("SELECT username FROM Users")
    print(result)
    result = db_manager.execute_query("SELECT password FROM Users")
    print(result)
    # Login
    user_response = yes_or_no("\nDo you have an account? (yes/no): ")
    if user_response == "yes":
        user.username = input("Username: ")
        user.password = input("Password: ")
        auth.login_user()
    else:
        user.username = input("Username: ")
        user.password = input("Password: ")
        auth.create_new_user()    


if __name__ == "__main__":
    main()


"""

# Current Users table
[('user1',), ('user2',), ('user3',), ('user4',), ('user5',), ('Gramahan',), ('Ashleigh',), ('Arjuna',), ('Faith',)]
[('password1',), ('password2',), ('password3',), ('password4',), ('password5',), ('GramahanPass',), ('Mama',), ('Dada',), ('more',)]


def main():
    db_manager = DatabaseManager("database/my_database.db")
    
    # Login
    user_response = yes_or_no("\nDo you have an account? (yes/no): ")
    if user_response == "yes":
        user = login_user(db_manager)
    else:
        user = create_new_user(db_manager)
    
    user_response = yes_or_no("\nAre you a carteaker? (yes/no): ")
    if user_response == "yes":
        user_id = get_user_id(db_manager, user)
        #print(user_id)
        administrator_menu(db_manager, user_id)
    else:
        user_id = get_user_id(db_manager, user)
        #print(user_id)
        user_menu(db_manager, user_id)

    # Main Functionality
    #search_data(db_manager, user_id):
    #just_chat()
    db_manager.close()



# Assures credentials meet regex requirements. Returns users credentials
def validate_credentials(self):
    credentials = input(f"Enter your {credential_type}: ")
    if re.fullmatch(r"([a-z0-9_]+)", credentials, re.IGNORECASE):
        return credentials
    else:
        print(f"Invalid {credential_type}. Please use one or more characters, letters, numbers, or underscores only.")
"""