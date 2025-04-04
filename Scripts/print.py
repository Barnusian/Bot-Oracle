from PIL import Image
from addTextToImage import add_text_to_image
from textRandomiser import select_line

# input image and text
bgImage = Image.open("Images/decorative frame 800 x 600.png")
sentence = select_line("Text/text.txt").upper()
font = "Fonts/Helvetica-Bold.ttf"
font_size = 72
manual_offset = 7

print(sentence)
 
printableImage = add_text_to_image(bgImage, sentence, font, font_size, manual_offset)

print(printableImage)