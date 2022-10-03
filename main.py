import sys, os
from src.basic import basic
from src.playlist import playlist
from src.text import text

def main(*args, **kwargs):

    if len(sys.argv) == 1 or sys.argv[1] in ["-h", "--help"]:

        print("""
./pyad [options] or python3 main.py [options]

Options:
    
    -h or --help - Show this help message
    -v or --version - Show version
    -b or --basic - Basic mode - download one video
    -p or --playlist - Playlist mode - download from YouTube/Spotify playlist
    -t or --text - Text mode - read line-by-line from text file
""")

    elif sys.argv[1] in ["-v", "version"]:

        print("Python YouTube Audio Downloader - version 2.0.1")
        print("http://github.com/jonahbebko/PYAD")

    elif sys.argv[1] in ["-b", "--basic"]:

        basic()
    
    elif sys.argv[1] in ["-p", "--playlist"]:

        playlist()
    
    elif sys.argv[1] in ["-tx", "--text"]:
        
        text()

if __name__ == "__main__":
    main()