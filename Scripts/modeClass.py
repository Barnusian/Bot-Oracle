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

# Dictionary of modes
modes = {
    # Helvetica on frame    
    1 : {
        "image" : "Images/decorative frame.png",
        "text" : "Text/random-text.txt",
        "font" : "Fonts/Helvetica-Bold.ttf",
        "font size" : 72,
        "vertical offset" : 7,
        "dither" : False
    },

    # Star wars guy, vertical text
    2 : {
        "image" : "Images/dancers.png",
        "text" : "Text/random-text.txt",
        "font" : "Fonts/Helvetica-Bold.ttf",
        "font size" : 60,
        "vertical offset" : 340,
        "dither" : True
    },

    # Manga image, text box
    3 : {
        "image" : "Images/bride of dracula.png",
        "text" : "Text/dressforaday.txt",
        "font" : "Fonts/FreeMonospaced-7ZXP.ttf",
        "font size" : 50,
        "vertical offset" : 340,
        "dither" : False
    },

    # cat dog image
    4 : {
        "image" : "Images/catndog.png",
        "text" : "Text/bot-oracle.txt",
        "font" : "Fonts/Helvetica-Bold.ttf",
        "font size" : 30,
        "vertical offset" : 200,
        "dither" : False
    },

    # Bartina
    5 : {
        "image" : "Images/Bartina.png",
        "text" : "Text/barts-words.txt",
        "font" : "Fonts/Helvetica-Bold.ttf",
        "font size" : 35,
        "vertical offset" : -158,
        "dither" : True
    }
}