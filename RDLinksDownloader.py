import argparse, subprocess, os

parser = argparse.ArgumentParser()
parser.add_argument('file', action='store', type=str, help="The file that has the links you want to download")
parser.add_argument('-d', '--directory', action='store', type=str, nargs='?', default="Music", help="The directory you want the files to be saved in (default is \"Music\")")
args = parser.parse_args()

RDLinksFileName = args.file
dirName = dirBaseName = args.directory

# Create directory
dirCount = 0

while os.path.exists(dirName):
    dirCount += 1
    dirName = dirBaseName + " - " + str(dirCount)

# Download files
with open(RDLinksFileName, 'r') as file:
    links = file.readlines()

for link in links:
    url = link.rstrip()
    subprocess.call(["wget", url, "-P", dirName])
