import PIL
from PIL import Image  # Python Image Library - Image Processing
import os
import os.path

sourceFolder = "./convert"
cwd="xxx"

# Get the current working directory
cwd = os.getcwd()

for file in os.listdir(sourceFolder):
    os.chdir(cwd) 
    # Print the current working directory
    #print("Current working directory: {0}".format(cwd))
    f_img = sourceFolder+"/"+file
    print(f_img)
    if file.find(".jfif") == -1:
        print("Not the right file type " + file)
    else:
        print("Found the right file type " + file)
        im = Image.open(sourceFolder+"/"+file)
        rgb_im = im.convert('RGB')
        rgb_im = im.convert('RGB')
        # Output Dir
        MYDIR = ("converted")
        CHECK_FOLDER = os.path.isdir(MYDIR)
        # If Dir doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)
        # Set curr Dir to new Dir
        newDir = os.path.join(os.getcwd(), MYDIR)
        os.chdir(newDir) 
        # Save file
        rgb_im.save(file.replace("jfif", "jpg"), quality=100)