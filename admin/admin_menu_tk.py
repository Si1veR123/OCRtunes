from tkinter import *
from .admin_funcs import *

def menu():
    root = Tk()
    root.title('Admin Controls')

    Button(root, text='Add Song', command=add_song).pack()
    Button(root, text='Remove Song', command=remove_song).pack()
    Button(root, text='Remove User', command=remove_user).pack()
    Button(root, text='Get Genres', command=get_genres).pack()

    root.mainloop()