import os
from PIL import Image
from textRandomiser import select_line

class PrintMode:
    def __init__(self, image_path, text_path, font_path, font_size, offset, dither):
        self.image_path = image_path
        self.text_path = text_path
        self.font_path = font_path
        self.font_size = font_size
        self.offset = offset
        self.dither = dither

    def load_image(self):
        if (os.path.exists(self.image_path)) :
            return Image.open(self.image_path)
        else :
            return Image.open("Images\lemonpig.png")
    
