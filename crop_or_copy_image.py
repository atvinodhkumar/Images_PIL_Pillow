"""
This script crops images from a folder. The edited image can be viewed during 
the run-time and saved in another folder with the same image name using 
Python Imaging Library (PIL) - Pillow. 

Syntax to crop an image:
    
    Image.crop(box=None)
    box = The crop rectangle, as a (left, upper, right, lower)-tuple.
    
    Returns a rectangular region from this image. The box is a 4-tuple defining 
    the left, upper, right, and lower pixel coordinate.
    
Reference:
    https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#PIL.Image.Image.crop
    
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
        image = image.crop((50, 140, 1000, 400))  # (left, upper, right, lower)
            
        image.save(image_name)
        image.show()
        
        
if __name__ == '__main__':
    main()
    