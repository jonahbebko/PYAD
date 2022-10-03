import os
import sys
import subprocess
import pydub
from .search import search
from .download import download
from sv_ttk import set_theme
from tkinter.ttk import (
    Frame,
    Button,
    Entry,
    Label,
    Combobox
)
from tkinter import (
    Tk,
    Grid,
    StringVar,
    PhotoImage,
    filedialog,
    messagebox,
    LEFT
)

# pyinstaller magic, idk
def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def close(root, *args, **kwargs):
    
    root.destroy()

def directoryButtonPressed(*args, **kwargs):

    folderSelected = filedialog.askdirectory()

    if not folderSelected:
        messagebox.showerror("Error", "No directory selected.")
        return
    
    global directory
    directory = folderSelected

def cleanse(title:str, *args, **kwargs):

    for i in ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]:
        title = title.replace(i, "-")
    title = title.replace(" ", "_")

    return title

def downloadButtonPressed(root, audioFormat, searchEntry, directory, *args, **kwargs):
    
    if searchEntry == "":
        messagebox.showerror("Error", "No playlist entered.")
        return

    if audioFormat == "Download as...":
        messagebox.showerror("Error", "Please select an audio format.")
        return
    if audioFormat not in ["mp3", "wav", "ogg", "flac", "aac"]:
        messagebox.showerror("Error", "Invalid audio format.")
        return
    
    if not directory:
        messagebox.showerror("Error", "No directory selected.")
        return
    
    idList = search(title=searchEntry, idsOnly=True, playlist=True)
    if idList == ("error", "collection"):
        messagebox.showerror("Error", "Liked songs are not supported.")
        return
    if idList == ("error", "request"):
        messagebox.showerror("Error", "Request failed, please check your network.")
        return
    if idList == ("error", "playlist"):
        messagebox.showerror("Error", "Invalid playlist.\n" + \
            "For YouTube playlists, please click \"View Full Playlist\" and copy the URL.")
        return
    if idList == "spotify":
        subprocess.Popen(f"spotdl --output-format {audioFormat} -f {searchEntry} -o {directory}", \
            shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for i in idList:

        if idList == "spotify":
            break

        title = cleanse(search(i, num=1, titleOnly=True)[0])
        
        download(i, directory)

        if audioFormat != "mp3":
        
            pydub.AudioSegment.from_file(f"{directory}/output.mp3").export(f"{directory}/output.{audioFormat}", format=audioFormat)
            os.remove(f"{directory}/output.mp3")
        
        try:
            os.rename(f"{directory}/output.{audioFormat}", f"{directory}/{title}.{audioFormat}")
        except FileExistsError:
            messagebox.showinfo("Error", f"File {title}.{audioFormat} already exists in {directory}, skipping...")
    
    if messagebox.askquestion("Success", "Download complete. Close program?") == "yes":
        close(root)
    else:
        pass

def playlist(*args, **kwargs):

    root = Tk()
    root.title("Python Audio YouTube Downloader - Playlist Mode")
    root.geometry("")
    root.minsize(width=500, height=185)
    root.wm_iconphoto(True, PhotoImage(file=resource_path("img/icon.ico")))
    
    frame = Frame(root)
    frame.pack(fill="both", expand=True, padx=5, pady=(0,5))

    frame.grid_columnconfigure(0, weight=1)

    searchEntryText = StringVar()
    audioFormat = StringVar()
    
    searchEntryLabel = Label(frame, text="Playlist URL (YouTube or Spotify):")
    searchEntryLabel.grid(row=0, column=0, padx=10, pady=(10,0), sticky="new")

    searchEntry = Entry(frame, justify=LEFT, textvariable=searchEntryText)
    searchEntry.grid(row=1, column=0, columnspan=2, padx=10, pady=(5,10), sticky="new")

    # .subsample is used to resize the image
    folderPhoto = PhotoImage(file=resource_path("./img/yellow.png")).subsample(16,16)

    availableFormats = ["mp3", "wav", "ogg", "flac", "aac"]

    formatDropdown = Combobox(frame, values=availableFormats, textvariable=audioFormat)
    formatDropdown.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="new")

    audioFormat.set("Download as...")

    global directory
    directory = ""

    directoryButton = Button(frame, text=" Directory...", image=folderPhoto, compound="left", command=lambda: (
        directoryButtonPressed(),
        directoryButton.config(text=f" {directory}")
    ))
    directoryButton.grid(row=4, column=0, padx=10, pady=10, sticky="sew")

    downloadButton = Button(frame, text="Download", command=lambda: (
        downloadButtonPressed(root, audioFormat.get(), searchEntryText.get(), directory)
    ))
    downloadButton.grid(row=4, column=1, padx=10, pady=10, sticky="sew")

    # custom Windows 11-like theme, pretty cool
    set_theme("dark")

    # on window closing
    root.protocol("WM_DELETE_WINDOW", lambda: close(root))

    root.mainloop()