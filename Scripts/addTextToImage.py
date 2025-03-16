import os
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

            #write text
            d.text((40, 30), words.upper(), font=fnt, fill=(0, 0, 0, 255))
            
            #merge both images
            out = Image.alpha_composite(base_image, text_image)

            out.save("test.png")
    else:
        print('No image found!')