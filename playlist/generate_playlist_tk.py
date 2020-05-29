from .playlist_funcs import generate_playlist
from tkinter import *

def enter_val(input_type, user):
    def get_field():
        choice = input_field.get()
        kwargs_dict = {input_type: choice}
        generate_playlist(input_type, user, **kwargs_dict)

    input_window = Tk()
    input_window.title('Enter')
    input_label = Label(input_window)
    if input_type == 'time':
        input_label.config(text='Input time (s)')
    elif input_type == 'genre':
        input_label.config(text='Input genre')
    input_field = Entry(input_window)

    confirm_button = Button(input_window, text='Enter', command=get_field)

    input_label.grid(column=1, row=1)
    input_field.grid(column=2, row=1)
    confirm_button.grid(column=3, row=1)

    input_window.update()

def generate_playlist_tk(user):
    def time_pressed():
        enter_val('time', user)

    def genre_pressed():
        enter_val('genre', user)



    select_generate_window = Tk()
    select_generate_window.title('Generate Playlist')

    time_button = Button(select_generate_window, text='By time', command=time_pressed).pack()
    genre_button = Button(select_generate_window, text='By genre', command=genre_pressed).pack()

    select_generate_window.update()