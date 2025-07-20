from gpiozero import LED
from time import sleep

# Use GPIO pin 17 (change if your LED is connected elsewhere)
led = LED(17)

led.on()
sleep(1)
led.off()