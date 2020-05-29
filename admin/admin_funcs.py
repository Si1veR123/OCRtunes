import sqlite3
try:
    from selenium.webdriver import Chrome
except ModuleNotFoundError:
    print('Module unavailable. Don\'t use scraping functionality')

# context manager for SQL
class openSQL:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.connection = sqlite3.connect(self.db)
        cursor = self.connection.cursor()
        return cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print('Error, closing database')
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()

class Locators:
    song_parent = 'div.container div.feed-item'
    song_title = 'cite.title'
    song_artist = 'em.artist'
    song_genre = 'li a'
    first_image = 'div#chart-position-1'

def scrape_top(results_num):
    url = 'http://www.popvortex.com/music/charts/top-100-songs.php'
    chrome_path = 'D:\Documents\Python\OCRtunes Project\chromedriver79.exe'
    browser = Chrome(chrome_path)
    html = browser.get(url)
    parent = browser.find_elements_by_css_selector(Locators.song_parent)
    rows_to_add = []
    for song in range(int(results_num)):
        rows_to_add.append(
            (parent[song].find_element_by_css_selector(Locators.song_artist).text.lower(),
             parent[song].find_element_by_css_selector(Locators.song_title).text.lower(),
             parent[song].find_element_by_css_selector(Locators.song_genre).text.lower(),
             0)
        )

    with openSQL('songs.db') as sql:
        sql.execute('SELECT name FROM songs')
        existing = sql.fetchall()
        for row in rows_to_add:
            found = False
            artist, title, genre, length = row
            for exist_name in existing:
                exist_name = exist_name[0]
                if exist_name == title:
                    found = True
            if not found:
                sql.execute('INSERT INTO songs VALUES(?, ?, ?, ?)', (title, artist, length, genre))
                print("Title:{}\nArtist:{}\nLength:{}\nGenre:{}".format(title, artist, length, genre))
    browser.close()


def add_song():
    song = ''
    while song != 'end':
        song = input("Enter song (name,artist,length,genre) ('end' to finish, 'scrape' to scrape data): ")
        if song != 'end' and song != 'scrape':
            song_list = song.split(',')
            with openSQL('songs.db') as sql:
                try:
                    sql.execute("INSERT INTO songs VALUES(?, ?, ?, ?)", tuple(song_list))
                    print('Added: {}'.format(song_list))
                except sqlite3.ProgrammingError:
                    print('Error. Try entering without spaces or ensure there are 4 values')
        elif song == 'scrape':
            scrape_top(input('Number of results'))

def remove_song():
    song = ''
    while song != 'end':
        song = input("Enter song (name) ('end' to finish): ")
        if song != 'end' and song != 'all':
            with openSQL('songs.db') as sql:
                sql.execute('DELETE FROM songs WHERE name=?', (song, ))
                print('Deleted: {}'.format(song))
        if song == 'all':
            if input('Are you sure? y/n: ') == 'y':
                with openSQL('songs.db') as sql:
                    sql.execute('DROP TABLE songs')

def remove_user():
    user = ''
    while user != 'end':
        user = input("User's name ('end' to finish): ")
        if user != 'admin' and user != 'end':
            with openSQL('users.db') as sql:
                sql.execute('DELETE FROM user WHERE username=?', (user, ))
                print('Deleted: {}'.format(user))
        if user == 'all':
            if input('Are you sure? y/n: ') == 'y':
                with openSQL('users.db') as sql:
                    sql.execute('DROP TABLE user')

def get_genres():
    with openSQL('songs.db') as sql:
        sql.execute('SELECT genre, length FROM songs')
        data = sql.fetchall()
    genre_length = {}
    for row in data:
        if row[0] in genre_length:
            num = genre_length[row[0]][1]
            # add the songs length to corresponding genre
            genre_length[row[0]] = (genre_length[row[0]][0] + row[1], num+1)
        else:
            genre_length[row[0]] = (row[1], 1)

    print(genre_length)
    print('Genre\tAverage')
    for genre, length in genre_length.items():
        average = length[0]/length[1]
        print(genre.title(), '\t', average)
