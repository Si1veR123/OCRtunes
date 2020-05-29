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

def create_song_db():
    with openSQL('songs.db') as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS songs(name text primary key, artist text, length integer, genre text)')

def add_song(name, artist='N/A', length=0, genre='N/A'):
    with openSQL('songs.db') as cursor:
        cursor.execute('SELECT name FROM songs')
        songs = cursor.fetchall()
        for row in songs:
            if name in row:
                print('Song exists')
                break
        else:
            cursor.execute('INSERT INTO songs VALUES(?, ?, ?, ?)', (name.lower(), artist.lower(), length, genre.lower()))

def view_all():
    with openSQL('songs.db') as cursor:
        cursor.execute('SELECT * FROM songs ORDER BY name')
        songs = cursor.fetchall()
    return songs

def save_artist_txt(artist):
    artist = artist.lower()
    with openSQL('songs.db') as sql:
        sql.execute('SELECT name FROM songs WHERE artist=?', (artist, ))
        songs = sql.fetchall()
    all_songs = ''
    for song in songs:
        song = song[0]
        if songs[0][0] == song:
            all_songs = song.title()
        else:
            all_songs = all_songs + ',' + song.title()

    with open('song.txt', 'w') as file:
        file.write(all_songs)