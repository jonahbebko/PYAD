import search
import download
from tkinter import *
from tkinter import ttk

def buttonPressed(*args):

    print("button pressed")

def main():

    root = Tk()
    root.title("Python Audio YouTube Downloader")

    l = ttk.Label(root, text="Starting")
    l.grid()

    l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
    l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
    l.bind('<ButtonPress-1>', buttonPressed)

    root.mainloop()

if __name__ == "__main__":
    main()