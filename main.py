from lib.search import search
from lib.download import download
from sv_ttk import set_theme
from tkinter.ttk import (
    Frame,
    Button,
    Style,
    Entry,
    Label
)
from tkinter import (
    Tk,
    StringVar,
    PhotoImage,
    LEFT, RIGHT
)

def searchButtonPressed(*args, **kwargs):

    print("button pressed")

def main(*args, **kwargs):

    root = Tk()
    root.title("Python Audio YouTube Downloader")
    root.geometry("360x240")
    root.minsize(width=200, height=600)
    root.iconphoto(False, PhotoImage(file = "icon.ico"))

    frame = Frame(root)
    frame.pack(fill="x")

    s = Style().configure("WBStyle",background="black",foreground="white")

    searchEntryLabel = Label(frame, text="Search entry or URL:")
    searchEntryLabel.grid(padx=10, pady=(10,0), row=1, column=1)

    searchEntryText = StringVar()
    searchEntry = Entry(frame, justify=LEFT, textvariable=searchEntryText)
    searchEntry.grid(padx=10, row=2, column=1)
    searchEntry.focus()

    numResultsLabel = Label(frame, text="Number of results:")
    numResultsLabel.grid(padx=10, pady=(10,0), row=3, column=1)

    numResults = StringVar()
    resultsEntry = Entry(frame, justify=LEFT, textvariable=numResults)
    resultsEntry.grid(padx=10, row=4, column=1)

    searchButton = Button(text="Search")
    searchButton.grid(padx=10, row=4, column=2)
    searchButton.bind('<ButtonPress-1>', searchButtonPressed)

    # custom Windows 11-like theme, pretty cool
    set_theme("dark")
    root.mainloop()

if __name__ == "__main__":
    main()