# The function of this python script is to remove any duplicate files in a folder.
# run using: py removeDuplicateImages.py
import os
import os.path
import sys
import numpy as np

# Assumes images are in a folder called "source"
sourceFolder = "./source"


for file in os.listdir(sourceFolder):
    f_img = sourceFolder+"/"+file
    if file.find("(1)") == -1:
        print("No 'duplicate' here!" + file)
    else:
        print("Found 'duplicate' in the string." + file)
        os.remove(f_img)
        print("Delted the duplicate file")
