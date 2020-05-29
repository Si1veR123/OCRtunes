from tkinter import *
from .user_edit_funcs import *

def edit_profile(user):
    def artist_pressed():
        field = artist_field.get()
        change_artist(user, field)
        current_artist.config(text='Current: {}'.format(field))


    def genre_pressed():
        field = genre_field.get()
        change_genre(user, field)
        current_genre.config(text='Current: {}'.format(field))

    current_g = get_genre(user)
    current_a = get_artist(user)

    ended = False
    main = Tk()
    main.title('Edit Profile')

    artist_label = Label(main, text='Artist').grid(column=1, row=1)
    artist_field = Entry(main)
    artist_field.grid(column=2, row=1)
    artist_submit = Button(main, text='Submit', command=artist_pressed).grid(column=3, row=1)
    current_artist = Label(main, text='Current: {}'.format(current_a))
    current_artist.grid(column=4, row=1)

    genre_label = Label(main, text='Genre').grid(column=1, row=2)
    genre_field = Entry(main)
    genre_field.grid(column=2, row=2)
    genre_submit = Button(main, text='Submit', command=genre_pressed).grid(column=3, row=2)
    current_genre = Label(main, text='Current: {}'.format(current_g))
    current_genre.grid(column=4, row=2)

    main.update()
