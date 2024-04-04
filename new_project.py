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


### Authentication Class/Methods ###
class Users:
    def __init__(self, username, password, db_manager):
        self.db_manager = db_manager
        self.username = username
        self.password = password
        self.user_id = None

    # Checks if username is in database. Returns a Boolean value.
    def user_exists(self):
        query = "SELECT username FROM users WHERE username = ?"
        params = [self.username]
        user = self.db_manager.execute_query(query, params)
        if user:
            return True
        else:
            return False

    # Returns actual user_id as int, not a tuple
    def get_user_id(self):
        self.user_id = self.db_manager.execute_query("SELECT user_id FROM users WHERE username = ?", [self.username])
        return self.user_id[0][0] # Ensure user_id[0][0] is used to extract the actual ID from the fetched result



def yes_or_no(question):
    user_response = input(question).lower()
    while user_response not in ["yes", "no"]:
        print("Please answer with 'yes' or 'no'.")
        user_response = input(question).lower()
    return user_response


# Potentially top level main function
def login_user(user):
    if user.user_exists():
        print("yay")
        return user.get_user_id()
    #potentially else block with error message here
    else:
        print("oh no")

def main():
    db_manager = DatabaseManager("database/my_database.db")
    username = input("username: ")
    password = input("password: ")
    user = Users(username, password, db_manager)
    # Login
    user_response = yes_or_no("\nDo you have an account? (yes/no): ")
    if user_response == "yes":
        login_user(user)
    else:
        user.create_new_user()    


if __name__ == "__main__":
    main()


"""
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