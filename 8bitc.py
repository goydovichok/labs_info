import RPi.GPIO as rpg
import time
rpg.setmode(rpg.BCM)
leds=[16,12,25,17,27,23,22,24]
rpg.setup(leds, rpg.OUT)
rpg.output(leds, 0)
while True:
    for led in leds:
        rpg.output(led, 1)
        time.sleep(0.2)
        rpg.output(led, 0)
    for i in range(7, -1, -1):
        led=leds[i]
        rpg.output(led, 1)
        time.sleep(0.2)
        rpg.output(led, 0)