import search
import download
from tkinter import *
from tkinter import ttk
import sv_ttk

def buttonPressed(*args):

    print("button pressed")

def main():

    root = Tk()
    root.title("Python Audio YouTube Downloader")
    root.geometry("360x240")

    frame = ttk.Frame(root)
    frame.grid(column=0, row=0, sticky="NW")

    s = ttk.Style().configure("WBStyle",background="black",foreground="white")

    l = ttk.Button(root, text="Starting")
    l.place(relx=0.5, rely=0.5, anchor="center")

    l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
    l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
    l.bind('<ButtonPress-1>', buttonPressed)

    # custom Windows 11-like theme, pretty cool
    sv_ttk.set_theme("dark")
    root.mainloop()

if __name__ == "__main__":
    main()