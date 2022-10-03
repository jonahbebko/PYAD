import sys, os
from src.basic import basic
from src.playlist import playlist
from src.text import text

def main(*args, **kwargs):

    if len(sys.argv) == 1 or sys.argv[1] in ["-h", "--help"]:

        print("usage: ./pyad [options]")
        print("options:")
        print("  -h,  --help: show this help message")
        print("  -v,  --version: show version")
        print("  -b,  --basic: download one file")
        print("  -p,  --playlist: read from youtube or spotify playlist")
        print("  -tx, --text: read and download from titles in text file")

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