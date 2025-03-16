import os
from textRandomiser import select_line
from PIL import Image, ImageDraw, ImageFont

def write_on_image(words, typeface, picture):
    if os.path.isfile(picture):
        with Image.open(picture).convert("RGBA") as base_image:
            
            #initialise blank image for text
            text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))

            #define font to be used
            fnt = ImageFont.truetype(typeface, 40)
            #simplify ImageDraw call, calling our pre-initialised blank image
            d = ImageDraw.Draw(text_image)

            print(words)
            #write text
            d.text((400, 300), "Hello", font=fnt, fill=(0, 0, 0, 255))

            out = Image.alpha_composite(base_image, text_image)

            out.save("test.png")
    else:
        print('No image found!')

useable_text = select_line('text.txt')
font_file = "Fonts/FreeMonospaced-7ZXP.ttf"
image_frame = 'decorative frame 800 x 600.png'
write_on_image(useable_text, font_file, image_frame)