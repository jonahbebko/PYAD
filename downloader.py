# welcome to the code
# don't run this file by itself - run the executable

# as of PYAD 1.1.0 this is the source for header functions
# so not main anymore
# don't run pretty please

# create a list of absent libraries, yell at the user to install them
# (this shouldn't be an issue since libraries are automatically added
# to the executable I made)
imports = []
try:
    from pytube import YouTube as yt
except:
    imports += "pytube"

try:
    from youtubesearchpython import VideosSearch as vs
except:
    imports += "youtubesearchpython"

try:
    from getch import pause
except:
    imports += "getch"

import os

if imports:
    print("Install missing libraries with pip and try again:")
    print(", ".join(imports))

# this is a custom-made library, replace colors with empty
# string if absent
try:
    from colors import *
except ImportError:
    RED = YELLOW = GREEN = BLUE = BOLD = RESET = ""

# fancy operating system detection to clear the terminal
# but this is a windows-only application
# kekw
def clear():
    os.system("cls" if os.name in ["nt", "dos"] else "clear")

# color-ify a string
def c(string, color):
    return color + string + RESET

# max function but smaller
def m(l):
    return max([len(i) for i in l])

def search(title:str, num:int=5):

    # initialize lists (yes it hurts to look at, i know)
    durs, views, channels, titles, ids = [], [], [], [], []

    # search for video and add data to lists
    for video in vs(title, limit=num).result()['result']:

        durs.append(video['duration'])
        views.append(video['viewCount']['short'])

        # cut off channel/title if too long
        if len(video['channel']['name']) > 25:
            channels.append(video['channel']['name'][:22] + "...")
        else:
            channels.append(video['channel']['name'])

        if len(video['title']) > 40:
            titles.append(video['title'][:37] + '...')
        else:
            titles.append(video['title'])
        
        ids.append(video['id'])

    # display videos one at a time
    for i in range(num):

        print(BOLD + f"[{i+1}]" + RESET + " < " + \
            c(durs[i], GREEN) + " "*(m(durs) - len(durs[i])) + \
            "  " + \
            c(views[i], BLUE) + " "*(m(views) - len(views[i])) + \
            " > " + \
            c(channels[i], RED) + " "*(m(channels) - len(channels[i])) + \
            " - " + \
            c(titles[i], YELLOW))
    
    # return the id list since it's used for the downloader
    return ids

def main():

    clear()
    print(BGRED+BOLD+" P "+RESET+RED+"ython \n"+ \
        BGORANGE+BOLD+WHITE+" Y "+RESET+ORANGE+"outube \n"+\
        BGYELLOW+BOLD+WHITE+" A "+RESET+YELLOW+"udio \n"+\
        BGGREEN+BOLD+WHITE+" D "+RESET+GREEN+"ownloader \n"+RESET)
    print("No rights reserved. Do what you wish.")
    print("Made by Jonah Bebko, check out my Github")
    title = input(c("\n\n\nSearch query?\n> ", YELLOW))
    
    # inefficient type validation but whatever
    try:
        num = int(input(c("\n\nNumber of videos to display?\n> ", YELLOW)))
    except:
        pause(c("\nInvalid type, must be a number\n", RED+BOLD))
        quit()

    clear()

    ids = search(title, int(num))
    
    try:
        sel = int(input(c(f"\n\nWhich video would you like to download? (1-{num})\n> ", YELLOW)))
    except:
        pause(c("\nInvalid type, must be a number\n", RED+BOLD))
        quit()
    
    if sel > num:
        pause(c("\nSelection over max\n", RED+BOLD))
        quit()

    clear()
    # use ids[sel-1] because indexing starts at 0 but humans start counting at 1
    # (and it looks nicer)
    print(c("Searching for ", YELLOW) + c("https://youtu.be/" + ids[sel-1], GREEN+BOLD) + c(", this may take some time...", YELLOW))

    # single-line operations are pretty cool
    vid = yt("https://youtu.be/" + ids[sel-1]).streams.filter(only_audio=True).first()

    dest = input(c("\n\nVideo found! ", GREEN+BOLD) + c("Enter the destination, or leave blank for current directory: \n> ", YELLOW))
    
    # the directory "." is the current directory
    if not dest: dest = "."

    save = vid.download(output_path=dest)

    # save memory by using a void variable
    # but this is python so who really cares about memory
    # it's about looking cool and smart
    base, _ = os.path.splitext(save)
    os.rename(save, base + ".mp3")

    pause(c("\n\nVideo downloaded successfully! ", GREEN+BOLD) + c("Press any key to exit.", GREEN))