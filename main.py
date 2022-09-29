from search import search
from download import download
from sv_ttk import set_theme
from tkinter.ttk import (
    Frame,
    Button,
    Style
)
from tkinter import (
    Tk
)

def buttonPressed(*args, **kwargs):

    print("button pressed")

def main(*args, **kwargs):

    root = Tk()
    root.title("Python Audio YouTube Downloader")
    root.geometry("360x240")

    frame = Frame(root)
    frame.grid(column=0, row=0, sticky="NW")

    s = Style().configure("WBStyle",background="black",foreground="white")

    l = Button(root, text="Starting")
    l.place(relx=0.5, rely=0.5, anchor="center")

    l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
    l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
    l.bind('<ButtonPress-1>', buttonPressed)

    # custom Windows 11-like theme, pretty cool
    set_theme("dark")
    root.mainloop()

if __name__ == "__main__":
    main()