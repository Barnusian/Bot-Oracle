import os
import platform
from dotenv import load_dotenv
# install spidev on pi

load_dotenv()

def get_device():
    dev_mode = os.getenv("DEV_MODE", "0") == "1" or platform.system() != "Linux"

    if dev_mode:
        from luma.emulator.device import pygame
        print("🧪 Running in DEV mode with emulator")
        return pygame(width=32, height=8)
    else:
        from luma.core.interface.serial import spi, noop
        from luma.led_matrix.device import max7219
        serial = spi(port=0, device=0, gpio=noop())
        print("🔌 Running on real hardware")
        return max7219(serial, cascaded=4, block_orientation=-90, rotate=0)