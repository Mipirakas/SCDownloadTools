import argparse, subprocess, os

parser = argparse.ArgumentParser()
parser.add_argument('file', action='store', type=str, help="The file that has the links you want to download")
parser.add_argument('-d', '--directory', action='store', type=str, nargs='?', default="Music", help="The directory you want the files to be saved in")
args = parser.parse_args()

RDLinksFileName = args.file

if args.directory:
    dirName = args.directory

# Create music directory
dirCount = ''

if os.path.exists(dirName):
    dirCount = 1
while os.path.exists(dirName + str(dirCount)):
    dirCount += 1
dirName = dirName + str(dirCount)
os.mkdir(dirName)

with open(RDLinksFileName, 'r') as file:
    lines = file.readlines()

os.chdir(dirName)

for link in lines:
    url = link.rstrip()
    subprocess.call(["wget", url])
