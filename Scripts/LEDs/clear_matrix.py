from Scripts.LEDs.device_setup import get_device
from luma.core.render import canvas

def clear_display():
    device = get_device()
    with canvas(device):
        pass  # clears display by drawing nothing