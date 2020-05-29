from .playlist_funcs import return_playlists
import json
from tkinter import *

def view_playlists(user):
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
    view_playlist.title('All Playlists')

    for num, playlist in enumerate(playlist_json.items()):
        key, songs = playlist
        Label(view_playlist, text=key).grid(column=1, row=num+1)
        Label(view_playlist, text=','.join(songs).title()).grid(column=2, row=num+1)

    view_playlist.update()
