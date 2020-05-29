from .song_db_funcs import view_all
from tkinter import *

def view_all_songs_tk():
    songs = view_all()

    window = Tk()
    window.title('All Songs')

    Label(window, text='Name', fg='red').grid(column=1, row=1)
    Label(window, text='Artist', fg='red').grid(column=2, row=1)
    Label(window, text='Length', fg='red').grid(column=3, row=1)
    Label(window, text='Genre', fg='red').grid(column=4, row=1)

    for num, song in enumerate(songs):
        Label(window, text=song[0].title()).grid(column=1, row=num+2)
        Label(window, text=song[1].title()).grid(column=2, row=num+2)
        Label(window, text=song[2]).grid(column=3, row=num+2)
        Label(window, text=song[3].title()).grid(column=4, row=num+2)

    window.update()