from playlist import *

class Emotions:
    def __init__(self, name, color, label):
        self.name = name
        self.color = color
        self.label = label
        self.playlists = []


def config_sad_playlists(sad):
    sad1 = Playlist(" crying in\nthe chapel", "saima.", "./src/sad1.png")
    sad2 = Playlist("Heartbreak Jazz", "Spotify", "./src/sad2.png")
    sad3 = Playlist("rakı masasında\n  dinlemelik", "İdil Alan", "./src/sad3.png")
    sad4 = Playlist("Gece gece\nağlamalık", "ranaaucar.14", "./src/sad4.png")
    sad5 = Playlist("writing a sad\n love story", "charlie skye ☕️", "./src/sad5.png")
    sad6 = Playlist("Melancholic Solitude", "Isaac Lefohn.", "./src/sad6.png")
    sad7 = Playlist("heart wrenchingly\n sad classical songs", "ola🦈", "./src/sad7.png")
    sad8 = Playlist("Sad Classic Rock", "Graham", "./src/sad8.png")
    sad9 = Playlist("emotional orchestral\n  music/complete", "Kutlay Tumay", "./src/sad9.png")
    sad10 = Playlist("im melancholy woman,\n  that’s what i am", "zehra", "./src/sad10.png")
    sad.playlists.append(sad1)
    sad.playlists.append(sad2)
    sad.playlists.append(sad3)
    sad.playlists.append(sad4)
    sad.playlists.append(sad5)
    sad.playlists.append(sad6)
    sad.playlists.append(sad7)
    sad.playlists.append(sad8)
    sad.playlists.append(sad9)
    sad.playlists.append(sad10)


def config_happy_playlists(happy):
    happy1 = Playlist("spring vibes but\nit's instrumental", "Paige Mathias", "./src/happy1.png")
    happy2 = Playlist("iconic 2000s\n pop songs", "sophia 🌟", "./src/happy2.png")
    happy3 = Playlist(" Türkçe pop 2000'ler\n     2010'lar❤️", "Göksu Tunç", "./src/happy3.png")
    happy4 = Playlist("Funky 70's 80's\nRnB Soul Groove🎸", "manelst", "./src/happy4.png")
    happy5 = Playlist("italiaNostalgia", "benni.mp3", "./src/happy5.png")
    happy6 = Playlist("Happy Feel\nGood Jazz", "Jared Hubbell", "./src/happy6.png")
    happy7 = Playlist("chill summer nights", "emmalarsson", "./src/happy7.png")
    happy8 = Playlist("Mekan", "Spotify", "./src/happy8.png")
    happy9 = Playlist("Energy Booster: R&B", "Spotify", "./src/happy9.png")
    happy10 = Playlist("Chill Happy Kitchen", "Kate Padgitt Bowman", "./src/happy10.png")
    happy.playlists.append(happy1)
    happy.playlists.append(happy2)
    happy.playlists.append(happy3)
    happy.playlists.append(happy4)
    happy.playlists.append(happy5)
    happy.playlists.append(happy6)
    happy.playlists.append(happy7)
    happy.playlists.append(happy8)
    happy.playlists.append(happy9)
    happy.playlists.append(happy10)


def config_angry_playlists(angry):
    angry1 = Playlist("female rage", "✧ maëlie ✧", "./src/angry1.png")
    angry2 = Playlist("metalheads>>", "mia <3", "./src/angry2.png")
    angry3 = Playlist("Rock N' Roll", "Pluttlurven", "./src/angry3.png")
    angry4 = Playlist("Kült Rock", "Spotify", "./src/angry4.png")
    angry5 = Playlist("Hardcore Punk", "Pure Noise Records", "./src/angry5.png")
    angry6 = Playlist("Anger Therapy", "johnwillbraddock", "./src/angry6.png")
    angry7 = Playlist("almanca A1", "zera", "./src/angry7.png")
    angry8 = Playlist("Best of Trash Metal", "Lomprdik", "./src/angry8.png")
    angry9 = Playlist("Old school\nTürkçe rap", "Hamit", "./src/angry9.png")
    angry10 = Playlist("nefretimi kusarken\ndinlediğim şarkılar", "Tuğçe Melek", "./src/angry10.png")
    angry.playlists.append(angry1)
    angry.playlists.append(angry2)
    angry.playlists.append(angry3)
    angry.playlists.append(angry4)
    angry.playlists.append(angry5)
    angry.playlists.append(angry6)
    angry.playlists.append(angry7)
    angry.playlists.append(angry8)
    angry.playlists.append(angry9)
    angry.playlists.append(angry10)