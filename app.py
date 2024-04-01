from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3
import re

app = Flask(__name__)
app.secret_key = '123'  # Needed for session management and flashing messages


### Database functionality ###

# Class for managing all database functionality
class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name, check_same_thread=False) 
        self.cursor = self.con.cursor()
    
    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.con.commit()  # Moved commit here for "write" operations; might want a separate method for "read" operations that doesn't commit.
        return self.cursor.fetchall()

    def close(self):
        self.con.close()

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if credentials_exist(username, password):
            return redirect(url_for('home'))  # Ensure you have a view function for 'home'
        else:
            flash('Invalid username or password')
            return redirect(url_for('login_user'))
    return render_template('login.html')

def credentials_exist(username, password=None):
    query = "SELECT username FROM users WHERE username = ?" + (" AND password = ?" if password else "")
    params = (username,) if password is None else (username, password)
    
    user = db_manager.execute_query(query, params)
    return bool(user)

# Placeholder for home page route
@app.route('/home')
def home():
    return "<p>Welcome Home!</p>"

db_manager = DatabaseManager("database/my_database.db")

if __name__ == "__main__":
    app.run(debug=True)  # Added 'debug=True' for development convenience
