from tkinter import PhotoImage


class Playlist:
    def __init__(self, title, artist, cover):
        self.title = title
        self.artist = artist
        self.cover = PhotoImage(file=cover)
        self.is_fav = False
        self.fav_message = '☆ save to fav'
        self.canvas = 0
        self.button = 0
