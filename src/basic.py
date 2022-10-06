import os
import pydub
from .resourcepath import resource_path
from .search import search
from .download import download
from sv_ttk import set_theme
from PIL import Image, ImageTk
from urllib.request import urlretrieve
from tkinter.ttk import (
    Frame,
    Button,
    Entry,
    Label,
    Combobox
)
from tkinter import (
    Grid,
    StringVar,
    PhotoImage,
    filedialog,
    messagebox,
    LEFT
)

def close(root, numResults, *args, **kwargs):

    if not numResults:
        root.destroy()
        return

    for i in range(int(numResults)):
        try:
            os.remove(resource_path(f"temp/{i}.png"))
            os.remove(resource_path(f"temp/{i}c.png"))
        except:
            pass
    
    root.destroy()

def searchButtonPressed(root, videoFrame, searchEntryText, numResults, *args, **kwargs):
    
    try:
        int(numResults)
    except ValueError:
        messagebox.showerror("Error", "Number of results must be an integer.")
        return
    
    if int(numResults) > 10:
        messagebox.showerror("Error", "More than 10 results will melt your computer.")
        return

    for widget in videoFrame.winfo_children():
        widget.destroy()

    thumbs, cthumbs, durs, views, channels, titles, fulltitles, ids = search(searchEntryText, numResults)

    frames = [0] * int(numResults)
    
    global idList
    idList = ids

    global ftitleList
    ftitleList = fulltitles

    for i in range(int(numResults)):

        f = Frame(videoFrame, height=50, borderwidth=1, relief="solid")
        f.grid(row=i, column=0, padx=1, pady=1, sticky="nsew")

        f.columnconfigure(2, weight=1)

        urlretrieve(thumbs[i], resource_path(f"temp/{i}.png"))
        img = ImageTk.PhotoImage(Image.open(resource_path(f"temp/{i}.png")).resize((100, 50)))

        urlretrieve(cthumbs[i], resource_path(f"temp/{i}c.png"))
        cimg = ImageTk.PhotoImage(Image.open(resource_path(f"temp/{i}c.png")).resize((50, 50)))

        identifier = Label(f, text=i, font=("Arial", 24))
        identifier.grid(row=0, column=0, rowspan=3, padx=(10,5), pady=5, sticky="nsw")

        thumbnail = Label(f, image=img)
        thumbnail.image = img
        thumbnail.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="nsw")

        ftitle = Label(f, text=titles[i])
        ftitle.grid(row=0, column=2, columnspan=2, padx=2, pady=(2,0), sticky="nw")

        fchannel = Label(f, text=channels[i])
        fchannel.grid(row=1, column=2, columnspan=2, padx=2, sticky="w")

        fduration = Label(f, text=durs[i])
        fduration.grid(row=2, column=2, padx=2, pady=(0,2), sticky="sw") 

        fviews = Label(f, text=views[i])
        fviews.grid(row=2, column=3, padx=2, pady=(0,2), sticky="se")

        fcthumb = Label(f, image=cimg)
        fcthumb.image = cimg
        fcthumb.grid(row=0, column=4, rowspan=3, padx=5, pady=5, sticky="nse")

        frames[i] = f

        root.update()

def directoryButtonPressed(*args, **kwargs):

    global directory
    directory = filedialog.askdirectory(title="Select a folder to save the video to.")

def downloadButtonPressed(root, audioFormat, numResults, videoSelected, directory, *args, **kwargs):
    
    if videoSelected == "":
        messagebox.showerror("Error", "No video selected.")
        return

    try:
        int(videoSelected)
    except ValueError:
        messagebox.showerror("Error", "Video selection must be an integer.")
        return
    
    if int(videoSelected)+1 > int(numResults):
        messagebox.showerror("Error", "Video selection out of range.")
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
    
    try:
        download(idList[int(videoSelected)])
    except FileExistsError:
        messagebox.showerror("Error", "File already exists.")
        return
    except:
        messagebox.showerror("Error", "Error with download. Please try again.")
        return

    # cleanse
    title = (
        ftitleList[int(videoSelected)]
        .replace("/", "-").replace("\\", "-").replace(":", "-")
        .replace("*", "-").replace("?", "-").replace("\"", "-")
        .replace("<", "-").replace(">", "-").replace("|", "-")
        .replace(" ", "_")
    )

    # convert from mp3 if other format selected
    if audioFormat != "mp3":
        
        pydub.AudioSegment.from_file(resource_path("temp/output.mp3")).export(f"{directory}/output.{audioFormat}", format=audioFormat)
        os.remove(resource_path("temp/output.mp3"))
    
    try:
        os.rename(f"{directory}/output.{audioFormat}", f"{directory}/{title}.{audioFormat}")
    except FileExistsError:
        messagebox.showinfo("Error", f"File {title}.{audioFormat} already exists in {directory}. Skipping...")
    
    if messagebox.askquestion("Success", "Download complete. Close program?") == "yes":
        close(root, numResults)
    else:
        pass

def basic(root, *args, **kwargs):

    root.title("Python Audio YouTube Downloader - Basic Mode")
    root.geometry("")
    root.minsize(width=500, height=250)
    
    frame = Frame(root)
    frame.pack(fill="both", expand=True, padx=5)
    
    # fourth frame (video results) expands to fill window
    Grid.rowconfigure(frame, 4, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)

    searchEntryText = StringVar()
    numResults = StringVar()
    videoSelected = StringVar()
    audioFormat = StringVar()
    
    searchEntryLabel = Label(frame, text="Search entry or URL:")
    searchEntryLabel.grid(row=0, column=0, padx=10, pady=(10,0), sticky="new")

    searchEntry = Entry(frame, justify=LEFT, textvariable=searchEntryText)
    searchEntry.grid(row=1, column=0, columnspan=2, padx=10, pady=(5,0), sticky="new")
    
    numResultsLabel = Label(frame, text="Number of results:")
    numResultsLabel.grid(row=2, column=0, padx=10, pady=(10,0), sticky="new")

    resultsEntry = Entry(frame, justify=LEFT, textvariable=numResults)
    resultsEntry.grid(row=3, column=0, padx=10, pady=(5,10), sticky="new")

    searchButton = Button(frame, text="Search", command=lambda: (
        searchButtonPressed(root, videoFrame, searchEntryText.get(), numResults.get())
    ))
    searchButton.grid(row=3, column=1, padx=10, pady=(5,10), sticky="new")
    
    videoFrame = Frame(frame)
    videoFrame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    #videoFrame.grid_rowconfigure(0, weight=1)
    videoFrame.grid_columnconfigure(0, weight=1)

    selectLabel = Label(frame, text="Select video:")
    selectLabel.grid(row=5, column=0, padx=10, pady=(10,0), sticky="new")

    selectEntry = Entry(frame, justify=LEFT, textvariable=videoSelected)
    selectEntry.grid(row=6, column=0, padx=10, pady=(5,10), sticky="new")

    # .subsample is used to resize the image
    folderPhoto = PhotoImage(file=resource_path("./img/yellow.png")).subsample(16,16)

    availableFormats = ["mp3", "wav", "ogg", "flac", "aac"]

    formatDropdown = Combobox(frame, values=availableFormats, textvariable=audioFormat)
    formatDropdown.grid(row=6, column=1, padx=10, pady=(5,10), sticky="new")

    audioFormat.set("Download as...")

    global directory
    directory = ""

    directoryButton = Button(frame, text=" Directory...", image=folderPhoto, compound="left", command=lambda: (
        directoryButtonPressed(),
        directoryButton.config(text=f" {directory}")
    ))
    directoryButton.grid(row=7, column=0, padx=10, pady=(10,20), sticky="sew")

    downloadButton = Button(frame, text="Download", command=lambda: (
        downloadButtonPressed(root, audioFormat.get(), numResults.get(), videoSelected.get(), directory)
    ))
    downloadButton.grid(row=7, column=1, padx=10, pady=(10,20), sticky="sew")

    # custom Windows 11-like theme, pretty cool
    set_theme("dark")

    # on window closing
    root.protocol("WM_DELETE_WINDOW", lambda: close(root, numResults.get()))

    root.mainloop()