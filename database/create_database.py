import sqlite3

# Use these two lines without DatabaseManager
con = sqlite3.connect("my_database.db")
cursor = con.cursor()

"""
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

db_manager = DatabaseManager("my_database.db")
"""


### Need to address case sensitivity issues between program and database. ###



#Creates the "users" table.
cursor.execute("""
    CREATE TABLE users(
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    )
""")

#Populates "users" table.
cursor.execute("""
    INSERT INTO users (username, password) VALUES
    ('user1', 'password1'),
    ('user2', 'password2'),
    ('user3', 'password3'),
    ('user4', 'password4'),
    ('user5', 'password5')
""")

con.commit()

#Creates the "question_answers" table.
cursor.execute("""
    CREATE TABLE question_answers(
    qa_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
""")

#Populates "question_answers" table.
cursor.execute("""
    INSERT INTO question_answers (user_id, question, answer) VALUES
    (1, 'Where did you grow up?', 'New York'),
    (1, 'How many siblings do you have?', '2'),
    (1, 'What is your favorite hobby?', 'Reading'),
    (2, 'Where did you grow up?', 'Los Angeles'),
    (2, 'How many siblings do you have?', '1'),
    (2, 'What is your favorite hobby?', 'Cooking'),
    (3, 'Where did you grow up?', 'Chicago'),
    (3, 'How many siblings do you have?', '3'),
    (3, 'What is your favorite hobby?', 'Gardening'),
    (4, 'Where did you grow up?', 'Houston'),
    (4, 'How many siblings do you have?', '4'),
    (4, 'What is your favorite hobby?', 'Painting'),
    (5, 'Where did you grow up?', 'Miami'),
    (5, 'How many siblings do you have?', '0'),
    (5, 'What is your favorite hobby?', 'Playing guitar')
""")

con.commit()

cursor.execute("""
    CREATE TABLE activity_log(
    activity_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    activity TEXT NOT NULL,
    frequency TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
""")

# Populates "activity_log" table with unique activities and questions for each user.
cursor.execute("""
    INSERT INTO activity_log (user_id, activity, frequency) VALUES
    (1, 'Asks about the current president repeatedly', 'Daily'),
    (1, 'Forgets where they placed their glasses, found in the garden', 'Weekly'),
    (1, 'Reminisces about their wedding day spontaneously', 'Occasionally'),
    (2, 'Repeatedly checks the front door is locked at night', 'Nightly'),
    (2, 'Forgets having eaten breakfast and asks for it', 'Daily'),
    (2, 'Laughs at the same old joke as if hearing it for the first time', 'Frequently'),
    (3, 'Inquires about childhood pet, a golden retriever named Sunny', 'Weekly'),
    (3, 'Starts gardening but forgets what plants they were tending to', 'Occasionally'),
    (3, 'Wears mismatched shoes but doesn't notice or mind', 'Rarely'),
    (4, 'Asks to visit deceased relatives believing they are still alive', 'Monthly'),
    (4, 'Forgets to turn off the TV before going to bed', 'Nightly'),
    (4, 'Keeps recounting stories from their youth as a teacher', 'Daily'),
    (5, 'Mistakes strangers for old friends, leading to friendly conversations', 'Weekly'),
    (5, 'Repeatedly plays their favorite song on the guitar, forgetting they just played it', 'Daily'),
    (5, 'Consistently forgets appointments but remembers to feed the birds', 'Always')
""")
               

con.commit()

result = cursor.execute("SELECT name FROM sqlite_master")
print(result.fetchall())

#result = cursor.execute("SELECT user_id, username FROM Users")
#print(result.fetchall())

#result = cursor.execute("SELECT user_id, question FROM question_answers")
#print(result.fetchall())

#result = cursor.execute("SELECT user_id, answer FROM question_answers")
#print(result.fetchall())

con.close()


# Use these four lines when using DatabaseManager
#query = "SELECT password FROM Users WHERE username = ?"
#params = ["Mama"]
#result = db_manager.execute_query(query, params)
#print(result[0][0])