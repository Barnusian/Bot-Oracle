from PIL import Image
from escpos.printer import Usb
from addTextToImage import add_text_to_image
from textRandomiser import select_line

# Define USB Vendor ID and Product IDs for both models
vendor_id = 0x04b8  # Epson's Vendor ID
t88v = 0x0e15       # TM-T88V Product ID
t88iv = 0x0202      # TM-T88IV Product ID

# Select the printer model you are using
printer = Usb(vendor_id, t88iv) # Change to t88iv if using TM-T88IV

# Print some text
# printer.text("Hello World!\n")

# input image and text
bgImage = Image.open("Images/decorative frame 800 x 600.png")
sentence = select_line("Text/text.txt").upper()
font = "Fonts/Helvetica-Bold.ttf"
font_size = 72
manual_offset = 7

print(sentence)
 
printableImage = add_text_to_image(bgImage, sentence, font, font_size, manual_offset)
print(printableImage)

with Image.open(printableImage) as img:
    if img.height < img.width :
        img = img.transpose(Image.ROTATE_90) # rotate 90 degrees
    img = img.resize((512, img.height * 512 // img.width))  # Scale to fit width
    img = img.convert("1") # Convert to black & white
    # img = img.convert("1", dither=Image.FLOYDSTEINBERG)
    # img.save("processed_image.bmp")  # Save as BMP for printing
    printer.image(img)  # Print a raster image


# Cut the receipt
printer.cut()