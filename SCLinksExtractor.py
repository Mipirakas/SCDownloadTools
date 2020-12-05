removeString = "" # The string you want to remove from the urls (the playlist string such as "?in=AccountName/sets/PlaylistName/"). Some files refuse to download if you don't remove this.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', action='store', type=str, help="The file you want to extract the links from")
parser.add_argument('-r', '--remove', action='store', type=str, nargs='?', help="The part of the urls that you want to remove (e.g. playlist url)")
parser.add_argument('-s', '--selector', action='store', type=str, default="/", help="The end of the url to select on")
args = parser.parse_args()

SCLinksFileName = args.file
linkSelector = args.selector

if args.remove:
    removeString = args.remove

with open(SCLinksFileName, 'r') as file:
    lines = file.readlines()

with open("ExtractedLinks.txt", 'w') as file:
    for line in lines:
        if line.rstrip().endswith(linkSelector):
            if not line.startswith("https://soundcloud.com"):
                line = "https://soundcloud.com" + line
            line = line.replace(removeString, "")
            file.write(line)
