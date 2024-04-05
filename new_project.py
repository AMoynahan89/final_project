import sqlite3
import re
import bcrypt


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
        #hashed_pass = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt())
        #print(hashed_pass)
        #self._password = hashed_pass
        self._password = value

    # Returns actual user_id as int, not a tuple
    def get_user_id(self):
        user_id = self.db_manager.execute_query("SELECT user_id FROM users WHERE username = ?", [self.username])
        return user_id[0][0] # Ensure user_id[0][0] is used to extract the actual ID from the fetched result


class Authenticator:
    def __init__(self, db_manager, user):
        self.db_manager = db_manager
        self.user = user

    # Checks if username is in database. Returns a Boolean value.
    def user_exists(self):
        user = self.db_manager.execute_query("SELECT username FROM users WHERE username = ?", [self.user.username])
        return bool(user)

    def password_mathces(self):
        correct_password = self.db_manager.execute_query("SELECT password FROM users WHERE password = ?", [self.user.password])
        return bool(correct_password)

    def login_user(self):
        if self.user_exists() and self.password_mathces():
            print("yay")
        else:
            # Need to handle login failures better
            print("oh no")

    def create_new_user(self):
        if not self.user_exists():
            self.db_manager.execute_query("INSERT INTO users (username, password) VALUES(?, ?)", (self.user.username, self.user.password))
            self.db_manager.commit()
            print("New user created!")
        else:
            # Need to handle taken username better
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

    user_response = yes_or_no("\nDo you have an account? (yes/no): ")
    if user_response == "yes":
        user.username = input("Username: ")
        user.password = input("Password: ")
        auth.login_user()
    else:
        user.username = input("Username: ")
        user.password = input("Password: ")
        auth.create_new_user()
    db_manager.close()


if __name__ == "__main__":
    main()


"""
>>> import bcrypt
>>> password = b"super secret password"
>>> # Hash a password for the first time, with a randomly-generated salt
>>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
>>> # Check that an unhashed password matches one that has previously been
>>> # hashed
>>> if bcrypt.checkpw(password, hashed):
...     print("It Matches!")
... else:
...     print("It Does not Match :(")

result = db_manager.execute_query("SELECT username, password FROM Users")
print(result)


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