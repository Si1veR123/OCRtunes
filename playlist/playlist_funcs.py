import sqlite3, json

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

def add_playlist_content(new_data, user):
    # get the current playlist contents
    with openSQL('users.db') as user_cursor:
        user_cursor.execute('SELECT playlist FROM user WHERE username = ?', (user,))
        current_playlist = user_cursor.fetchall()[0][0]

    # gets the dictionaries of playlists, or if empty, creates new
    if current_playlist != 'pl':
        json_current = json.loads(current_playlist)
        previous_playlist_contents = json_current
    else:
        previous_playlist_contents = {}

    # get new playlist number
    old_length_playlist = len(previous_playlist_contents)
    # add to playlist
    previous_playlist_contents[old_length_playlist + 1] = new_data

    # gets json string to update to SQL
    playlist_to_update = json.dumps(previous_playlist_contents)

    # update SQL
    with openSQL('users.db') as user_sql:
        user_sql.execute('UPDATE user SET playlist = ? WHERE username = ?', (playlist_to_update, user))

def user_create_playlist(user, songs):

    """
    Gets user's playlist details
    Get all song names in database
    Add songs to playlist
    Update playlist

    Playlist in format: {1: [songs], 2: [songs], 3: [songs]}
    Playlists are json strings
    """

    with openSQL('songs.db') as song_cursor:
        song_cursor.execute('SELECT name FROM songs')
        song_info = song_cursor.fetchall()

    new_data = []

    for song in song_info:
        song = song[0]
        if song in songs:
            new_data.append(song)

    add_playlist_content(new_data, user)


def generate_playlist(type_pl, user, time=None, genre=None):
    if type_pl == 'time':
        with openSQL('songs.db') as sql:
            sql.execute('SELECT name, length FROM songs')
            all_songs = sql.fetchall()

        songs_to_add = []
        current_time = 0
        time = int(time)
        for song in all_songs:
            if current_time + song[1] > time:
                break
            current_time += song[1]
            songs_to_add.append(song[0])
        add_playlist_content(songs_to_add, user)

    elif type_pl == 'genre':
        genre = genre.lower()
        with openSQL('songs.db') as sql:
            sql.execute('SELECT name FROM songs WHERE genre = ?', (genre, ))
            songs = sql.fetchall()

        songs_to_add = []
        counter = 0
        for song in songs:
            if counter == 5:
                break
            song = song[0]
            songs_to_add.append(song)
            counter += 1
        add_playlist_content(songs_to_add, user)

def return_playlists(user):
    with openSQL('users.db') as sql:
        sql.execute('SELECT playlist FROM user WHERE username=?', (user, ))
        playlists = sql.fetchall()
    return playlists

def del_playlist(user, pl):
    with openSQL('users.db') as sql:
        sql.execute('SELECT playlist FROM user WHERE username=?', (user, ))
        before_playlists = sql.fetchall()[0][0]
    before_playlists_json = json.loads(before_playlists)
    after_playlists = {
                    k: v
                    for k, v in before_playlists_json.items()
                    if k not in pl
                }
    after_playlists_str = json.dumps(after_playlists)
    with openSQL('users.db') as sql:
        sql.execute('UPDATE user SET playlist = ? WHERE username=?', (after_playlists_str, user))