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
    root.geometry("600x240")
    root.minsize(width=200, height=600)
    root.iconphoto(False, PhotoImage(file = "icon.ico"))

    frame = Frame(root)
    frame.pack()

    s = Style().configure("WBStyle",background="black",foreground="white")

    searchEntryLabel = Label(frame, text="Search entry or URL:")
    searchEntryLabel.pack(fill='x', side=LEFT)

    searchEntryText = StringVar()
    searchEntry = Entry(frame, justify=LEFT, textvariable=searchEntryText)
    searchEntry.pack(fill='x', side=LEFT)
    searchEntry.focus()

    numResultsLabel = Label(frame, text="Number of results:")
    numResultsLabel.pack(fill='x', side=LEFT)

    numResults = StringVar()
    resultsEntry = Entry(frame, justify=LEFT, textvariable=numResults)
    resultsEntry.pack(fill='x', side=LEFT)

    searchButton = Button(text="Search")
    searchButton.pack(fill='x', side=RIGHT)
    searchButton.bind('<ButtonPress-1>', searchButtonPressed)

    # custom Windows 11-like theme, pretty cool
    set_theme("dark")
    root.mainloop()

if __name__ == "__main__":
    main()