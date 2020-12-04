SCLinksFileName = "SCLinks.txt"
replaceString = "" # The string you want to remove from the urls (the playlist string such as "?in=AccountName/sets/PlaylistName/"). Some files refuse to download if you don't remove this.

with open(SCLinksFileName, 'r') as file:
    lines = file.readlines()

with open("ExtractedLinks.txt", 'w') as file:
    for line in lines:
        if line.endswith("/\n"):
            if not line.startswith("https://soundcloud.com"):
                line = "https://soundcloud.com" + line
            line = line.replace(replaceString, "")
            file.write(line)