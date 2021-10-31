# python-image-processing
A method to perform some operations on an image, in order to get an enhanced image or to extract some useful information from it.


## How to use
All functions are written in Python, and each file does a different image processing according to file name.
Once cloning and opening the repo, create a new folder and call it "source". This is where you place images into.
Use images from [here](https://github.com/WathikAhmed/GAN-images)

If converting image types, create a new folder and call it "convert". This is where you place images into.

### main.py
Runs all image cropping and processing functions, and outputs to "./Final".

### removeDuplicateImages.py
Loops through "./source" and removes duplicate images.

### generateCropOnly.py
Generates cropped images and outputs to "./sourceFolderCropped".

### processCroppedImages.py
Processes the images in "./sourceFolderCropped" and outputs to "./Final".
