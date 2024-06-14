import pickle
from tkinter import *
from emotions import *
from random import sample
from moodtune import *
import os
import sys


# ---------FUNCTIONS--------- #
def save_favorites():
    with open('favorites.pkl', 'wb') as f:
        favorites = {emotion_name: [(pl.title, pl.artist, pl.is_fav) for pl in emotion.playlists]
                     for emotion_name, emotion in {"sad": sad, "happy": happy, "angry": angry}.items()}
        pickle.dump(favorites, f)


def load_favorites():
    try:
        with open('favorites.pkl', 'rb') as f:
            favorites = pickle.load(f)
            for emotion_name, favs in favorites.items():
                for title, artist, is_fav in favs:
                    for pl in globals()[emotion_name].playlists:
                        if pl.title == title and pl.artist == artist:
                            pl.is_fav = is_fav
                            pl.fav_message = '★ discard save' if is_fav else '☆ save to fav'
    except FileNotFoundError:
        pass


def on_closing():
    save_favorites()
    window.destroy()


def restart_program():
    save_favorites()
    window.destroy()
    os.execl(sys.executable, sys.executable, *sys.argv)


def config_canvas(emotion, playlist, col):
    canvas = Canvas(width=200, height=320, bg=emotion.color, highlightthickness=0)
    canvas.create_image(100, 200, image=playlist.cover)
    canvas.create_text(100, 60, text=playlist.title, fill="black", font=("Courier", 12, "bold"))
    canvas.create_text(100, 90, text=playlist.artist, fill="black", font=("Courier", 12))
    canvas.grid(column=col, row=2)

    fav_button = Button(text=playlist.fav_message, highlightthickness=0, font=('Courier', 10, 'bold'), command=lambda: toggle_fav(playlist, fav_button))
    fav_button.grid(column=col, row=3)

    playlist.button = fav_button
    playlist.canvas = canvas


def config_canvas_faw(emotion, playlist, col, my_window):
    canvas = Canvas(width=200, height=320, bg=emotion.color, highlightthickness=0)
    canvas.create_image(100, 200, image=playlist.cover)
    canvas.create_text(100, 60, text=playlist.title, fill="black", font=("Courier", 12, "bold"))
    canvas.create_text(100, 90, text=playlist.artist, fill="black", font=("Courier", 12))
    canvas.grid(column=col, row=2)

    fav_button = Button(text=playlist.fav_message, highlightthickness=0, font=('Courier', 10, 'bold'), command=lambda: discard_fav(playlist, my_window, emotion))
    fav_button.grid(column=col, row=3)

    playlist.button = fav_button
    playlist.canvas = canvas


def refresh(emotion, playlists):
    pl1, pl2, pl3 = sample(range(0, 10), 3)

    for i in range(len(playlists)):
        playlists[i].canvas.delete('all')
        playlists[i].button.destroy()

    playlists[0] = emotion.playlists[pl1]
    playlists[1] = emotion.playlists[pl2]
    playlists[2] = emotion.playlists[pl3]

    for i in range(3):
        config_canvas(current_emotion, playlists[i], i)


def toggle_fav(playlist, button):
    if playlist.is_fav:
        playlist.is_fav = False
        playlist.fav_message = '☆ save to fav'
    else:
        playlist.is_fav = True
        playlist.fav_message = '★ discard save'

    button.config(text=playlist.fav_message)


def discard_fav(playlist, window, emotion):
    if playlist.is_fav:
        playlist.is_fav = False
        playlist.fav_message = '☆ save to fav'
    find_favorites(emotion, window)


def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def find_favorites(emotion, window, page=0):
    clear_window(window)
    window_faw(window, emotion, page)


def call_main_window(window):
    clear_window(window)
    window.config(bg=current_emotion.color)

    pl1, pl2, pl3 = sample(range(0, 10), 3)

    playlists = [current_emotion.playlists[pl1], current_emotion.playlists[pl2], current_emotion.playlists[pl3]]

    go_back = Button(text='back', highlightthickness=0, font=('Courier', 10), command=restart_program)
    go_back.grid(column=0, row=0)

    go_fav = Button(text='✦favs', highlightthickness=0, font=('Courier', 10), command=lambda: window_faw(window, current_emotion))
    go_fav.grid(column=2, row=0)

    title_label = Label(text=current_emotion.label, fg="black", bg=current_emotion.color, font=('Courier', 20, 'bold'))
    title_label.grid(column=1, row=1)

    config_canvas(current_emotion, playlists[0], 0)
    config_canvas(current_emotion, playlists[1], 1)
    config_canvas(current_emotion, playlists[2], 2)

    padding = Canvas(width=200, height=75, bg=current_emotion.color, highlightthickness=0)
    padding.grid(column=1, row=4)

    refresh_button = Button(text="refresh", highlightthickness=0, font=('Courier', 12, "bold"), command=lambda: refresh(current_emotion, playlists))
    refresh_button.grid(column=1, row=5)


def window_faw(my_window, emotion, page=0):
    clear_window(my_window)
    my_window.config(bg=emotion.color)

    go_back = Button(text='back', highlightthickness=0, font=('Courier', 10), command=lambda: call_main_window(my_window))
    go_back.grid(column=0, row=0)

    title_label = Label(text='SAVED FAVORITES', fg="black", bg=emotion.color, font=('Courier', 20, 'bold'))
    title_label.grid(column=1, row=1)

    favorites = []
    for i in range(len(emotion.playlists)):
        if emotion.playlists[i].is_fav:
            favorites.append(emotion.playlists[i])

    start_index = page * 3
    end_index = start_index + 3
    displayed_favorites = favorites[start_index:end_index]

    if len(displayed_favorites) == 0:
        padding2 = Canvas(width=200, height=320, bg=emotion.color, highlightthickness=0)
        padding2.grid(column=0, row=3)
        no_fav_label = Label(text='No saved favorites.', fg="black", bg=emotion.color, font=('Courier', 16))
        no_fav_label.grid(column=1, row=4)
    else:
        for i, favorite in enumerate(displayed_favorites):
            config_canvas_faw(emotion, favorite, i, my_window)

    if page > 0:
        arrow_left_button = Button(text="←", highlightthickness=0, font=('Courier', 12, "bold"), command=lambda: find_favorites(emotion, my_window, page-1))
        arrow_left_button.grid(column=0, row=5)

    if end_index < len(favorites):
        arrow_right_button = Button(text="→", highlightthickness=0, font=('Courier', 12, "bold"), command=lambda: find_favorites(emotion, my_window, page+1))
        arrow_right_button.grid(column=2, row=5)

    padding = Canvas(width=200, height=75, bg=emotion.color, highlightthickness=0)
    padding.grid(column=1, row=5)

    sad_button = Button(text="sad", highlightthickness=0, font=('Courier', 12, "bold"), command=lambda: find_favorites(sad, my_window))
    sad_button.grid(column=0, row=6)
    happy_button = Button(text="happy", highlightthickness=0, font=('Courier', 12, "bold"), command=lambda: find_favorites(happy, my_window))
    happy_button.grid(column=1, row=6)
    angry_button = Button(text="angry", highlightthickness=0, font=('Courier', 12, "bold"), command=lambda: find_favorites(angry, my_window))
    angry_button.grid(column=2, row=6)


# -------EMOTIONS------- #
sad = Emotions('sad', '#A9BCFF', "I SEE YOU FEEL BLUE")
happy = Emotions('happy', '#FFFFAD', "I SEE YOU FEEL YELLOW")
angry = Emotions('angry', '#FF9F8C', "I SEE YOU FEEL RED")

# -------UI SETUP-------- #

detected_emotion = find_emotion()
while (detected_emotion == -1):
    detected_emotion = find_emotion()

if detected_emotion == sad.name:
    current_emotion = sad
elif detected_emotion == happy.name:
    current_emotion = happy
else:
    current_emotion = angry

window = Tk()
window.title("Moodtune")
window.config(padx=70, pady=10, bg=current_emotion.color)
window.geometry("830x550")
window.resizable(False, False)

config_sad_playlists(sad)
config_happy_playlists(happy)
config_angry_playlists(angry)

load_favorites()
call_main_window(window)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.grid_propagate(False)
window.mainloop()
