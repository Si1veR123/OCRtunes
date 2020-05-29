import sqlite3, re

"""
Contains all of the functions needed to login
Includes:
    Formatting checks
    Database creation
    Database manipulation
"""

# context manager for SQL
class openSQL:
    def __enter__(self):
        self.connection = sqlite3.connect('users.db')
        cursor = self.connection.cursor()
        return cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print('Error, closing database')
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()


# creates the database if not already created and creates admin account
def create_db():
    with openSQL() as sql:
        sql.execute('CREATE TABLE IF NOT EXISTS user(username text primary key, password text, dob text, artist text, genre text, playlist text)')
        sql.execute("SELECT * FROM user WHERE username='admin'")
        admin_results = sql.fetchall()
        if len(admin_results) == 0:
            sql.execute("INSERT INTO user VALUES('admin', 'ocrtunesadmin', 'admin', 'admin', 'admin', '{}')")

# checks if a user exists
def check_user(checkuser):
    with openSQL() as sql:
        sql.execute('SELECT username FROM user')
        users = sql.fetchall()
        for user in users:
            if checkuser == user[0]:
                return True
        return False

# returns password of given user to verify
def check_user_password(user):
    with openSQL() as sql:
        sql.execute("SELECT password FROM user WHERE username = ?", (user,))
        password = sql.fetchall()
    return password[0][0]

# validate password format
def validate_password(pw):
    upper_letter = False
    lower_letter = False
    number_present = False

    for letter in pw:
        if letter.isupper():
            upper_letter = True
            print('Upper Letter')
        if letter.islower():
            lower_letter = True
            print('Lower Letter')
        try:
            int(letter)
            number_present = True
        except ValueError:
            pass

    if upper_letter and lower_letter and number_present:
        return True
    print('Pw')
    return False

# validate date of birth
def validate_dob(dob):
    valid_match = '[0-9]{2}\.[0-9]{2}\.[0-9]{4}'
    is_valid = re.match(valid_match, dob)
    if is_valid:
        return True
    return False
