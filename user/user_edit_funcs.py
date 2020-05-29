import sqlite3

class openSQL:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.connection = sqlite3.connect(self.db)
        cursor = self.connection.cursor()
        return cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

def change_artist(user, new_artist):
    with openSQL('users.db') as sql:
        sql.execute('UPDATE user SET artist=? WHERE username=?', (new_artist, user))

def change_genre(user, new_genre):
    with openSQL('users.db') as sql:
        sql.execute('UPDATE user SET genre=? WHERE username=?', (new_genre, user))

def get_genre(user):
    with openSQL('users.db') as sql:
        sql.execute('SELECT genre FROM user WHERE username=?', (user, ))
        data = sql.fetchall()
    return data[0][0]

def get_artist(user):
    with openSQL('users.db') as sql:
        sql.execute('SELECT artist FROM user WHERE username=?', (user, ))
        data = sql.fetchall()
    return data[0][0]
