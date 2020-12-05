dirName = 'Music'

from urllib.request import urlopen, urlretrieve
import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', action='store', type=str, help="The file that has the links you want to download")
parser.add_argument('-d', '--directory', action='store', type=str, nargs='?', help="The directory you want the files to be saved in")
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


# Download files
nameCount = 0
sName = ''
downloadCount = 0

with open(RDLinksFileName, 'r') as file:
    lines = file.readlines()

for link in lines:
    link = link.rstrip()
    name = link.rsplit("/", 1)[-1].replace("%20", " ")
    fileName = os.path.join(dirName, name)
    while os.path.isfile(fileName.rsplit(".", 1)[0] + str(sName) + "." + fileName.rsplit(".", 1)[1]):
        nameCount += 1
        sName = "_" + str(nameCount)
    fileName = fileName.rsplit(".", 1)[0] + str(sName) + "." + fileName.rsplit(".", 1)[1]
    urlretrieve(link, fileName)
    print("Downloaded: " + name)
    downloadCount += 1

print("------------------------------------")
print("Downloaded " + str(downloadCount) + " files")
print("------------------------------------")