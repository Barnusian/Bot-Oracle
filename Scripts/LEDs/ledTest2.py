from luma.emulator.device import pygame as luma_pygame
from luma.emulator.render import transformer
import pygame  # This is the actual pygame module we need
from luma.core.render import canvas
from PIL import ImageFont

device = luma_pygame(
    width=32,
    height=8,
    scale=8,
    transform=getattr(transformer(pygame, 32, 8, 8), "led_matrix")
)

font = ImageFont.load_default()

with canvas(device) as draw:
    draw.text((0, 0), "Hi!", font=font, fill="white")

input("Press Enter to close...")
