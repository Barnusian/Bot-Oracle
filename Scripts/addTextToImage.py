from PIL import Image, ImageDraw, ImageFont
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

def add_text_to_image(image, sentence, font_file, font_size, offset):
    # Load a suitable font with the desired size
    font = ImageFont.truetype(font_file, font_size)
     
    # Apply line wrap if the text is longer than the image width
    max_width = int(image.width * 0.9)
    wrapped_text = wrap_text(sentence, max_width, font)
     
    draw = ImageDraw.Draw(image)
    line_spacing = 1.1  # Adjust this value based on your needs
    x = (image.width - max_width) // 2
    
    # Fixed line height based on font size, ignoring ascenders and descenders
    line_height = int(font_size * line_spacing)
    
    # Calculate the total height of the text block without extra space after the last line
    total_text_height = (len(wrapped_text) - 1) * line_height + font_size

    # Calculate the starting y position to center the text block
    y = (image.height - total_text_height) // 2 + offset #Alter this offset for different fonts
    
    # Draw each line of text on the image
    for line in wrapped_text:
        left, top, right, bottom = font.getbbox(line)
        line_width = right - left
        # Draw the line, centre it horizontally and position it vertically
        draw.text(((image.width - line_width) // 2, y), line, "Black", font=font)
        y += line_height  # Move the y position for the next line
 
    # Save the image to disk
    image.save("Output/output.png")