import RPi.GPIO as rpg
import time
rpg.setmode(rpg.BCM)
rpg.setup(26, rpg.OUT)
s=False
while True:
    rpg.output(26, s)
    s=not s
    time.sleep(1)
