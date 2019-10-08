"""
This script draws a rectangle and puts text anywhere on the image using PIL. 
The edited image can be viewed during the run-time and saved in the desired location.

Syntax to draw a rectangle on an image:
    PIL.ImageDraw.Draw.rectangle(xy, fill=None, outline=None)
    xy = Four points to define the bounding box. Sequence of either [(x0, y0), (x1, y1)] 
         or [x0, y0, x1, y1]. The second point is just outside the drawn rectangle.

Reference:
    https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html#PIL.ImageDraw.PIL.ImageDraw.Draw.rectangle

Syntax to put a text on an image:
    PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)
    xy = Top left corner of the text.
    text = Text to be drawn. If it contains any newline characters, 
           the text is passed on to mulitiline_text()

Reference:
    https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html#PIL.ImageDraw.PIL.ImageDraw.Draw.text
    
Dimension of the image used here is 1024 * 500
"""


import os
import glob


from PIL import Image, ImageFont, ImageDraw


source = r"C:/Users/Desktop/source"

destination = r"C:/Users/Desktop/destination"
    
    
def main():
    
    for files in glob.glob(source + "/*.png"):
        
        filename, file_extension = os.path.splitext(files)
        image_name = os.path.join(destination, os.path.basename(filename) + '.png')
    
        image = Image.open(files)
        draw_image = ImageDraw.Draw(image)
        
        draw_image.rectangle((594, 400, 944, 460), fill=None, outline="red")
        draw_image.text((594, 390), "Enter Text", fill="red", font = ImageFont.truetype("arial", 75))  # 75 -> fontsize
        
        image.save(image_name)
        image.show()
    
    
if __name__ == '__main__':
    main()
