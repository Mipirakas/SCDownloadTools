import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', action='store', type=str, help="The file you want to extract the links from")
parser.add_argument('-r', '--remove', action='store', type=str, default="", help="The part of the urls that you want to remove (e.g. playlist url)")
parser.add_argument('-s', '--selector', action='store', type=str, default="/", help="The end of the url to select on")
args = parser.parse_args()

SCLinksFileName = args.file
removeString = args.remove
linkSelector = args.selector

with open(SCLinksFileName, 'r') as file:
    lines = file.readlines()

with open("ExtractedLinks.txt", 'w') as file:
    for line in lines:
        if line.rstrip().endswith(linkSelector):
            if not line.startswith("https://soundcloud.com"):
                line = "https://soundcloud.com" + line
            line = line.replace(removeString, "")
            file.write(line)
