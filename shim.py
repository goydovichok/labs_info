import RPi.GPIO as rpg
import time
rpg.setmode(rpg.BCM)
rpg.setup(26, rpg.OUT)
pwm=rpg.PWM(26, 200)
duty = 0.0
pwm.start(duty)
while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty+=1.0
    if duty > 100.0:
        duty=0.0