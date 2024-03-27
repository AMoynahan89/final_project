import sqlite3

con = sqlite3.connect("my_database.db")

cursor = con.cursor()


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


#Creates the "question_answers" table.
#cursor.execute("""
#    CREATE TABLE question_answers(
#    qa_id INTEGER PRIMARY KEY,
#    user_id INTEGER,
#    question TEXT NOT NULL,
#    answer TEXT NOT NULL,
#    FOREIGN KEY (user_id) REFERENCES users(user_id)
#    )
#""")


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

#result = cursor.execute("SELECT user_id, username FROM Users")
#print(result.fetchall())

#result = cursor.execute("SELECT user_id, question FROM question_answers")
#print(result.fetchall())

#con.close()
