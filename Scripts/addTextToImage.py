from PIL import ImageDraw, ImageFont

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
    # Load font with the desired starting font size
    font = ImageFont.truetype(font_file, font_size)
    
    # Apply line wrap if the text is longer than the image width
    max_width = int(image.width * 0.9)
    wrapped_text = wrap_text(sentence, max_width, font)
    
    # Find the initial total height based on the width constraint
    line_spacing = 1.1
    line_height = int(font_size * line_spacing)
    total_text_height = (len(wrapped_text) - 1) * line_height + font_size
    
    # Check if the total height exceeds 90% of the image height
    max_height = int(image.height * 0.9)
    
    # Reduce the font size iteratively if the total text height exceeds the max height
    while total_text_height > max_height:
        font_size = int(font_size * 0.9)  # Reduce font size by 10%
        font = ImageFont.truetype(font_file, font_size)
        wrapped_text = wrap_text(sentence, max_width, font)  # Re-wrap text after reducing font size
        line_height = int(font_size * line_spacing)
        total_text_height = (len(wrapped_text) - 1) * line_height + font_size
    
    # Create the drawing context
    draw = ImageDraw.Draw(image)
    
    # Recalculate max width and line height after adjusting font size
    max_width = int(image.width * 0.9)
    x = (image.width - max_width) // 2
    
    # Calculate the starting y position to center the text block
    y = (image.height - total_text_height) // 2 + offset  # Adjust the offset for different fonts
    
    # Draw each line of text on the image
    for line in wrapped_text:
        left, top, right, bottom = font.getbbox(line)
        line_width = right - left
        # Draw the line, center it horizontally and position it vertically
        draw.text(((image.width - line_width) // 2, y), line, "Black", font=font)
        y += line_height  # Move the y position for the next line
    
    # Save the image to disk
    image.save("Output/output.png")
    return "Output/output.png"