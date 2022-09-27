from os import system
from os import name

# fancy operating system detection to clear the terminal
# but this is a windows-only application
# kekw
def clear():
    system("cls" if name in ["nt", "dos"] else "clear")