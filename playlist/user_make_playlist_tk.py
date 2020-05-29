from songs_db.song_db_funcs import view_all
from .playlist_funcs import user_create_playlist
from tkinter import *


def user_make_playlist_tk(user):
    def get_songs_field():
        songs = add_playlist_field.get()
        if songs != '':
            songs = songs.lower()
            comma = 0
            checked_str = ''
            for letter in songs:
                space_after_comma = False

                # if comma is equal to one, letter needs to be checked
                if comma == 1:
                    if letter == ' ':
                        space_after_comma = True
                    comma = 0

                if not space_after_comma:
                    checked_str += letter

                # checks if letter is a comma. This is to remove spaces after commas
                if letter == ',':
                    comma = 1

            full_list = checked_str.split(',')
            full = tuple(full_list)

            user_create_playlist(user, full)

    songs = view_all()

    window = Tk()
    window.title('Create Playlist')

    for num, song in enumerate(songs):
        Label(window, text=song[0].title()).grid(column=1, row=num + 2)
        Label(window, text=song[1].title()).grid(column=2, row=num + 2)
        Label(window, text=song[2]).grid(column=3, row=num + 2)
        Label(window, text=song[3].title()).grid(column=4, row=num + 2)
        max_num = num + 1

    add_playlist_label = Label(window, text="New songs (separate by ','):")
    add_playlist_field = Entry(window)
    add_playlist_button = Button(window, text='Add songs', command=get_songs_field)

    if len(songs) != 0:
        add_playlist_label.grid(column=1, row=max_num + 2)
        add_playlist_field.grid(column=2, row=max_num + 2)
        add_playlist_button.grid(column=3, row=max_num+2)
    else:
        Label(window, text='Empty').pack()

    window.update()