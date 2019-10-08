"""
This script resizes images from a folder. The edited image can be viewed during
 the run-time and saved in another folder with the same image name using 
Python Imaging Library (PIL) - Pillow. 

Syntax to resize an image:
    Image.resize(size, resample=0)
    size = The requested size in pixels, as a 2-tuple: (width, height).

Reference:
    https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#PIL.Image.Image.resize

Dimension of the image used here is 1024 * 500
"""


import os
import glob


from PIL import Image


source = r"C:/Users/Desktop/source"

destination = r"C:/Users/Desktop/destination"


def main():
    
    for files in glob.glob(source + "/*.png"):
        
        filename, file_extension = os.path.splitext(files)
        image_name = os.path.join(destination, os.path.basename(filename) + '.png')
        
        image = Image.open(files)
        image = image.resize((500, 500), Image.ANTIALIAS)
            
        image.save(image_name)
        image.show()
        
        
if __name__ == '__main__':
    main()
