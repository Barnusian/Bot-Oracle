from addTextToImage import write_on_image
from textRandomiser import select_line

useable_text = select_line('text.txt')
font_file = "Fonts/Helvetica-Bold.ttf"
image_frame = "Images/decorative frame 800 x 600.png"
write_on_image(useable_text, font_file, image_frame)