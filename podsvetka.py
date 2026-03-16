import RPi.GPIO as rpg
rpg.setmode(rpg.BCM)
rpg.setup(26, rpg.OUT)
rpg.setup(6, rpg.IN)
while True:
    rpg.output(26, not(rpg.input(6)))
    print(rpg.input(6))