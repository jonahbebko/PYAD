from multiprocessing import resource_tracker
import os
import sys
from src.basic import basic
from src.playlist import playlist
from src.text import text
from sv_ttk import set_theme
from tkinter.ttk import (
    Frame,
    Button,
    Label
)
from tkinter import (
    Tk,
    PhotoImage,
)

try:
    import pydub, PIL, urllib, pytube, youtubesearchpython, spotipy
except ImportError:
    import subprocess
    subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def destroy(root):

    for widget in root.winfo_children():
        widget.destroy()

def main(*args, **kwargs):

    if not os.path.exists(resource_path("temp")):
        os.mkdir(resource_path("temp"))

    root = Tk()
    root.title("Select Mode")
    root.geometry("")
    root.minsize(width=360, height=140)
    root.wm_iconphoto(True, PhotoImage(file=resource_path("img\icon.ico")))

    frame = Frame(root)
    frame.pack(fill="both", expand=True, padx=5)
    
    basicButton = Button(frame, text="Basic", command=lambda: (
        destroy(root),
        basic(root)
    ))
    basicButton.grid(row=0, column=0, padx=5, pady=(10,5), sticky="nsew")

    basicLabel = Label(frame, text="Download a single video.")
    basicLabel.grid(row=0, column=1, padx=5, pady=(10,5), sticky="nsew")

    playlistButton = Button(frame, text="Playlist", command=lambda: (
        destroy(root),
        playlist(root)
    ))
    playlistButton.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    playlistLabel = Label(frame, text="Download a playlist from YouTube or Spotify.")
    playlistLabel.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    textButton = Button(frame, text="Text", command=lambda: (
        destroy(root),
        text(root)
    ))
    textButton.grid(row=2, column=0, padx=5, pady=(5,10), sticky="nsew")

    textLabel = Label(frame, text="Download a list of videos from a text file.")
    textLabel.grid(row=2, column=1, padx=5, pady=(5,10), sticky="nsew")

    set_theme("dark")
    root.mainloop()

if __name__ == "__main__":
    main()