import os
import os.path
import sys
import numpy as np

# Assumes images are in 1944x2592 dimensions and in .jpg format
sourceFolder = "./source"



def removeDupe():
    
    for file in os.listdir(sourceFolder):
        f_img = sourceFolder+"/"+file
        if file.find("(1)") == -1:
            print("No 'duplicate' here!" + file)
        else:
            print("Found 'duplicate' in the string." + file)
            os.remove(f_img)
            print("Delted the duplicate file")
        



def main():
    removeDupe()

main()