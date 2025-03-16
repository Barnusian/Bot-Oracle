from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt
from textRandomiser import select_line

def wrap_text(text, max_width, font):
    lines = []
    words = text.split(' ')
     
    current_line = ''
    for word in words:
        test_line = current_line + word + ' '
        left, top, right, bottom = font.getbbox(test_line)
        line_width = right - left
        if line_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line[:-1])
            current_line = word + ' '
 
    lines.append(current_line[:-1])
    return lines

def add_text_to_image(image, sentence):
     
    # Load a suitable font with the desired size
    font_size = 72
    font = ImageFont.truetype("Fonts/Helvetica-Bold.ttf", font_size)
     
    # Apply line wrap if the text is longer than the image width
    max_width = int(image.width * 0.9)
    wrapped_text = wrap_text(sentence, max_width, font)
     
    draw = ImageDraw.Draw(image)
    line_spacing = 1.3  # Adjust this value based on your needs
    x = (image.width - max_width) // 2
    y = (image.height - int(font_size * len(wrapped_text) * line_spacing)) // 2
    for line in wrapped_text:
        left, top, right, bottom = font.getbbox(line)
        line_width = right - left
        draw.text(((image.width - line_width) // 2, y), line, "Black", font=font)
        y += int(font_size * line_spacing)
 
    # save image to disk
    image.save("Output/output.png")

# input image
image = Image.open("Images/decorative frame 800 x 600.png")
 
#input text to be wrapped on the input image
sentence = select_line("Text/textwrapexample.txt").upper()
print(sentence)
 
add_text_to_image(image, sentence)