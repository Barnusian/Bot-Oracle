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
            return Image.open("Images/lemonpig.png")

# Dictionary of modes
modes = {
    # Helvetica on frame    
    1 : {
        "image_path" : "Images/decorative frame.png",
        "text_path" : "Text/random-text.txt",
        "font_path" : "Fonts/Helvetica-Bold.ttf",
        "font_size" : 72,
        "offset" : 7,
        "dither" : False
    },

    # Star wars guy, vertical text
    2 : {
        "image_path" : "Images/dancers.png",
        "text_path" : "Text/random-text.txt",
        "font_path" : "Fonts/Helvetica-Bold.ttf",
        "font_size" : 60,
        "offset" : 340,
        "dither" : True
    },

    # Manga image, text box
    3 : {
        "image_path" : "Images/bride of dracula.png",
        "text_path" : "Text/dressforaday.txt",
        "font_path" : "Fonts/FreeMonospaced-7ZXP.ttf",
        "font_size" : 50,
        "offset" : 340,
        "dither" : False
    },

    # cat dog image
    4 : {
        "image_path" : "Images/catndog.png",
        "text_path" : "Text/bot-oracle.txt",
        "font_path" : "Fonts/Helvetica-Bold.ttf",
        "font_size" : 30,
        "offset" : 200,
        "dither" : False
    },

    # Bartina
    5 : {
        "image_path" : "Images/Bartina.png",
        "text_path" : "Text/barts-words.txt",
        "font_path" : "Fonts/Helvetica-Bold.ttf",
        "font_size" : 35,
        "offset" : -158,
        "dither" : True
    }
}