from device_setup import get_device
from luma.core.render import canvas

device = get_device()

# Clear the display by opening a canvas and not drawing anything
with canvas(device):
    pass