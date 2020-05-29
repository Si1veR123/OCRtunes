from tkinter import *
from .song_db_funcs import save_artist_txt

def write_artist_txt():
    def pressed():
        save_artist_txt(field.get())

    main = Tk()
    main.title('Write artist to txt')

    label = Label(main, text='Artist')
    field = Entry(main)
    button = Button(main, text='Submit', command=pressed)

    label.grid(column=1, row=1)
    field.grid(column=2, row=1)
    button.grid(column=3, row=1)

    main.update()