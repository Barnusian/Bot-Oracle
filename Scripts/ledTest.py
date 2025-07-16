import os
from time import sleep
from luma.core.render import canvas
from PIL import ImageFont
from device_setup import get_device  # assuming you save the above in device_setup.py
import warnings

warnings.filterwarnings("ignore", message="pkg_resources is deprecated")

device = get_device()
font = ImageFont.truetype("Fonts\FreeMonospaced-7ZXP.ttf", 8)
msg = "Goosie, Remy and Rambo"

# Make a long enough virtual canvas to scroll text
width = device.width
virtual_width = (len(msg) * 8) + width

while True:
    for ofset in range(0, virtual_width, 2):
        with canvas(device) as draw:
            draw.text((width-ofset, 0), msg, font=font, fill="white")
        sleep(0.08)