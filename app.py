from login.main_login import main_login
from songs_db.song_db_funcs import create_song_db
import admin.admin_menu_tk
import playlist.generate_playlist_tk, playlist.user_make_playlist_tk, playlist.view_playlist_tk, playlist.del_pl_tk
import songs_db.view_songs_tk, songs_db.write_txt_tk
import user.user_edit_tk
from tkinter import *

create_song_db()
logged_username = main_login()

def main_app(usern):
    root = Tk()
    root.title('OCRtunes')
    root.geometry('500x320')
    root.resizable(False, False)
    root.config(bg='blue')

    header_frame = Frame()
    header_frame.place(x=200, y=10)
    header_frame.config(bg='blue')

    ocrtunes_label = Label(header_frame, text='OCRtunes', font=(100), bg='blue').pack()
    username_label = Label(header_frame, text='{}'.format(usern), bg='blue').pack()

    body_frame = Frame()
    body_frame.place(x=70, y=100)

    edit_account_button = Button(body_frame, width=50, text='Edit Account', command=lambda:user.user_edit_tk.edit_profile(usern))
    edit_account_button.pack(fill='x')
    view_songs_button = Button(body_frame, width=50, text='View Songs', command=lambda:songs_db.view_songs_tk.view_all_songs_tk()).pack(fill='x')
    create_playlist = Button(body_frame, width=50, text='Create Playlist', command=lambda:playlist.user_make_playlist_tk.user_make_playlist_tk(usern))
    create_playlist.pack(fill='x')
    generate_playlist = Button(body_frame, width=50, text='Auto-Generate Playlist', command=lambda:playlist.generate_playlist_tk.generate_playlist_tk(usern))
    generate_playlist.pack(fill='x')
    show_playlist = Button(body_frame, width=50, text='View Playlist(s)', command=lambda:playlist.view_playlist_tk.view_playlists(usern)).pack(fill='x')
    del_playlist = Button(body_frame, width=50, text='Delete Playlist(s)', command=lambda:playlist.del_pl_tk.delete_playlists_tk(usern)).pack(fill='x')
    save_artist = Button(body_frame, width=50, text='Save Songs', command=lambda:songs_db.write_txt_tk.write_artist_txt()).pack(fill='x')
    quit_button = Button(body_frame, width=50, text='Quit', bg='red', command=quit).pack(fill='x')
    if usern == 'admin':
        admin_button = Button(text='Admin', command=admin.admin_menu_tk.menu).place(x=10, y=290)
        edit_account_button.config(state='disabled', disabledforeground='red')
        create_playlist.config(state='disabled', disabledforeground='red')
        generate_playlist.config(state='disabled', disabledforeground='red')

    root.mainloop()

main_app(logged_username)