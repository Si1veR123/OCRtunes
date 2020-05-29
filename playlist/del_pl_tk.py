from tkinter import *
import json
from .playlist_funcs import del_playlist, return_playlists


def delete_playlists_tk(user):
    def delete():
        field = entry_field.get()
        field = field.split(',')
        full = []
        for pl in field:
            if pl[0] == ' ':
                full.append(pl[1:])
            else:
                full.append(pl)
        del_playlist(user, full)
        view_playlist.destroy()
        delete_playlists_tk(user)

    """
    [ ( [ {1: [songs], 2: [songs], 3: [songs] } ] ) ]
    """

    playlists = return_playlists(user)
    if playlists[0][0] != '{}':
        playlists = playlists[0][0]
        playlist_json = json.loads(playlists)
    else:
        playlist_json = {1: ['Empty']}

    view_playlist = Tk()
    view_playlist.title('Delete Playlist')

    for num, playlist in enumerate(playlist_json.items()):
        key, songs = playlist
        Label(view_playlist, text=key).grid(column=1, row=num+1)
        Label(view_playlist, text=','.join(songs).title()).grid(column=2, row=num+1)
        max_num = num + 2

    entry_label = Label(view_playlist, text='Playlist to delete (e.g. 1,2,3): ')
    entry_label.grid(column=1, row=max_num)

    entry_field = Entry(view_playlist)
    entry_field.grid(column=2, row=max_num)

    entry_button = Button(view_playlist, text='Enter', command=delete)
    entry_button.grid(column=3, row=max_num)

    view_playlist.update()
