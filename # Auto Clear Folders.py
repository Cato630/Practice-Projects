# Auto Clear Folders
import os
import time
#Get the current date/time group
now = time.time()
#Locate files in the download folder
files=os.listdir("Downloads")
#Scan the files then remove those older than 90 days
for file in files:
    if os.path.getatime(file ) < now - 90 * 24 *60 * 60:
        os.remove(file)