import random
from PIL import Image
from escpos.printer import Usb
from addTextToImage import add_text_to_image
from textRandomiser import select_line
from modeClass import PrintMode

# Define USB Vendor ID and Product IDs for both models
vendor_id = 0x04b8  # Epson's Vendor ID
t88v = 0x0e15       # TM-T88V Product ID
t88iv = 0x0202      # TM-T88IV Product ID

# Select the printer model being used
printer = Usb(vendor_id, t88iv, profile="TM-T88IV")

# Print Modes
modes = {
    1: PrintMode("Images/decorative frame.png", select_line("Text/random-text.txt").upper(), "Fonts/Helvetica-Bold.ttf", 72, 7, False),
    2: PrintMode("Images/dancers.png", select_line("Text/textwrapexample.txt"), "Fonts/FreeMonospaced-7ZXP.ttf", 50, 340, False),
    3: PrintMode("Images/bride of dracula.png", select_line("Text/random-text.txt"), "Fonts/Helvetica-Bold.ttf", 60, 340, True),
    4: PrintMode("Images/catndog.png", select_line("Text/bot-oracle.txt"), "Fonts/Helvetica-Bold.ttf", 30, 200, False),
    5: PrintMode("Images/Bartina.png", select_line("Text/barts-words.txt"), "Fonts/Helvetica-Bold.ttf", 35, -158, True),
}

selected_mode = modes[random.randint(1,5)]
#selected_mode = modes[1]

bgImage = selected_mode.load_image()
sentence = selected_mode.text_path
font = selected_mode.font_path
font_size = selected_mode.font_size
manual_offset = selected_mode.offset
dither_flag = selected_mode.dither

# input image and text
#bgImage = Image.open("Images/decorative frame 800 x 600.png")
#sentence = select_line("Text/text.txt").upper()
#font = "Fonts/Helvetica-Bold.ttf"
#font_size = 72
#manual_offset = 7

# print random sentence to be used, to console
print(sentence)
print(f"Dither = {dither_flag}")

# create variable containing the path to a new randomised image
printableImage = add_text_to_image(bgImage, sentence, font, font_size, manual_offset)
# print(printableImage) # print outputh path, for debugging

with Image.open(printableImage) as img:
    if img.height < img.width :
        img = img.transpose(Image.ROTATE_90) # rotate 90 degrees
    img = img.resize((512, img.height * 512 // img.width))  # Scale to fit width
    if dither_flag == True:
        img = img.convert("1", dither=Image.FLOYDSTEINBERG) # Use dither
    else :
        img = img.convert("1") # Convert to black & white
    # img.save("Images/processed_image.bmp")  # Save as BMP for printing
    printer.image(img, center=True)  # Print a raster image

# Cut the receipt
printer.cut()