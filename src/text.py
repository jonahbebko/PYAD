import os
import pydub
from .search import search
from .download import download
from .cleanse import cleanse
from sv_ttk import set_theme
from tkinter.ttk import (
    Frame,
    Button,
    Label,
    Combobox
)
from tkinter import (
    StringVar,
    PhotoImage,
    filedialog,
    messagebox
)
def close(root, *args, **kwargs):
    
    root.destroy()

def directoryInButtonPressed(*args, **kwargs):

    global inDirectory
    inDirectory = filedialog.askopenfilename(title="Select a file to read from.", filetypes=[("Text files", "*.txt")])

def directoryOutButtonPressed(*args, **kwargs):

    global outDirectory
    outDirectory = filedialog.askdirectory(title="Select a directory to save to.")

def downloadButtonPressed(root, lastDownloaded, audioFormat, inDirectory, outDirectory, *args, **kwargs):

    if audioFormat == "Download as...":
        messagebox.showerror("Error", "Please select an audio format.")
        return
    if audioFormat not in ["mp3", "wav", "ogg", "flac", "aac"]:
        messagebox.showerror("Error", "Invalid audio format.")
        return
    
    if not inDirectory:
        messagebox.showerror("Error", "No input file selected.")
        return
    if not outDirectory:
        messagebox.showerror("Error", "No output directory selected.")
        return
    
    with open(inDirectory, "r") as f:
        lines = [line.replace("\n", "") for line in f if (not line.startswith("#")) or (not line.strip())]
    
    if not lines:
        messagebox.showerror("Error", "Input file is empty.")
        return
    
    for line in lines:

        if not line: continue

        vid = search(line, num=1, idsOnly=True)[0]

        title = cleanse(line)

        # convert to audio format
        try:
            download(id=vid, title="output.mp3", path="temp/")
        except FileExistsError:
            messagebox.showerror("Error", f"File {title} already exists. Skipping...")
            pass

        if audioFormat != "mp3":
        
            f = pydub.AudioSegment.from_mp3("temp/output.mp3")
            f.export(f"{outDirectory}/{title}.{audioFormat}", format=audioFormat)
            os.remove("temp/output.mp3")
        
        else:

            # rename can also be used to move file
            os.rename("temp/output.mp3", f"{outDirectory}/{title}.mp3")

        lastDownloaded.config(text=f"Last downloaded: {title}.{audioFormat}")
        root.update()
    
    if messagebox.askquestion("Success", "Download complete. Close program?") == "yes":
        close(root)
    else:
        pass

def text(root, *args, **kwargs):

    root.title("Python Audio YouTube Downloader - Text Mode")
    root.geometry("")
    root.minsize(width=500, height=145)
    
    frame = Frame(root)
    frame.pack(fill="both", expand=True, padx=5, pady=10)

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    
    # .subsample is used to resize the image
    folderPhoto = PhotoImage(file="./img/yellow.png").subsample(16,16)

    audioFormat = StringVar()

    global inDirectory, outDirectory
    inDirectory = outDirectory = ""

    directoryInButton = Button(frame, text=" File to Read...", image=folderPhoto, compound="left", command=lambda: (
        directoryInButtonPressed(),
        directoryInButton.config(text=f" {inDirectory[:20]}"+("..." if len(inDirectory) > 20 else ""))
    ))
    directoryInButton.grid(row=0, column=0, padx=10, pady=10, sticky="new")

    directoryOutButton = Button(frame, text=" Output Directory...", image=folderPhoto, compound="left", command=lambda: (
        directoryOutButtonPressed(),
        directoryOutButton.config(text=f" {outDirectory[:20]}"+("..." if len(outDirectory) > 20 else ""))
    ))
    directoryOutButton.grid(row=0, column=1, padx=10, pady=10, sticky="new")

    availableFormats = ["mp3", "wav", "ogg", "flac", "aac"]

    formatDropdown = Combobox(frame, values=availableFormats, textvariable=audioFormat)
    formatDropdown.grid(row=1, column=0, padx=10, pady=10, sticky="sew")

    audioFormat.set("Download as...")
    
    downloadButton = Button(frame, text="Download", command=lambda: (
        downloadButtonPressed(root, lastDownloaded, audioFormat.get(), inDirectory, outDirectory)
    ))
    downloadButton.grid(row=1, column=1, padx=10, pady=10, sticky="sew")

    lastDownloaded = Label(frame, text="Last downloaded: None")
    lastDownloaded.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="sew")

    # custom Windows 11-like theme, pretty cool
    set_theme("dark")

    # on window closing
    root.protocol("WM_DELETE_WINDOW", lambda: close(root))

    root.mainloop()