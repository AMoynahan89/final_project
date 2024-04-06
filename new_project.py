import sqlite3
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
        hashed = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt())
        self._password = hashed

    # Returns actual user_id as int, not a tuple
    def get_user_id(self):
        user_id = self.db_manager.execute_query("SELECT user_id FROM users WHERE username = ?", [self.username])
        self.user_id = user_id[0][0] # Ensure user_id[0][0] is used to extract the actual ID from the fetched result


class Authenticator:
    def __init__(self, db_manager, user):
        self.db_manager = db_manager
        self.user = user

    # Checks if username is in database. Returns a Boolean value.
    def user_exists(self):
        user = self.db_manager.execute_query("SELECT username FROM users WHERE username = ?", [self.user.username])
        return bool(user)

    def password_matches(self, raw_password):
        result = self.db_manager.execute_query("SELECT password FROM users WHERE username = ?", [self.user.username])
        if result:
            stored_password = result[0][0]
            return bcrypt.checkpw(raw_password.encode("utf-8"), stored_password)
        else:
            return False

    def create_new_user(self):
        if not self.user_exists():
            self.db_manager.execute_query("INSERT INTO users (username, password) VALUES(?, ?)", (self.user.username, self.user.password))
            self.db_manager.commit()
        else:
            # Need to handle taken username better
            print(f"The username {self.user.username} is already taken. Please chose a different username.")

    
# Administrator interface menu
class AdministratorProfile:
    def __init__(self, db_manager, user):
        self.db_manager = db_manager
        self.user = user


    def menu(self):
        while True:
            print("\nHow can I help you?")
            print("(1) Enter important information about patient.")
            #print("(2) Display patient info.")
            #print("(3) Make note of behaviors you would like to track.")
            print("(4) Exit.")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.enter_new_data()
            elif choice == "2":
                self.display_user_q_and_a()
            elif choice == "3":
                self.log_activity()
            elif choice == "4":
                quit()
            else:
                continue


    #Inserts question-answer pairs into database
    def enter_new_data(self):
        question = input("Enter your question: ")
        answer = input("Enter the answer: ")
        self.db_manager.execute_query("INSERT INTO question_answers (user_id, question, answer) VALUES (?, ?, ?)", (self.user.user_id, question, answer))
        self.db_manager.commit()


    def display_user_q_and_a(self):
        pass


    # Keep track of a repedative/interesting behaviour(often asked questions)
    def log_activity(self):
        activity = input("Enter whatever you would like to make note of: ")
        frequency = input("How often does this happen?")
        self.db_manager.execute_query("INSERT INTO activity_log (activity, frequency) VALUES (?, ?, ?)", (self.user.user_id, activity, frequency))
        self.db_manager.commit()


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
        user.username = input("Username: ").lower()
        raw_password = input("Password: ")
        if auth.user_exists() and auth.password_matches(raw_password):
            print("Login succesful!")
        else:
            print("Invalid credentials")
    else:
        user.username = input("Username: ").lower()
        user.password = input("Password: ")
        auth.create_new_user()
        print("New user created!")
    
    user_response = yes_or_no("\nAre you a carteaker? (yes/no): ")
    if user_response == "yes":
        admin_profile = AdministratorProfile(db_manager, user)
        admin_profile.menu()
#    else:
#        user_profile = UserProfile(db_manager, user)
#        user_profile.menu()
    db_manager.close()


if __name__ == "__main__":
    main()



# Assures credentials meet regex requirements. Returns users credentials
#def valid_credentials(self, credentials):
#    match = re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,30}$", credentials)
#    is_match = bool(match)
#    return is_match

"""
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
"""