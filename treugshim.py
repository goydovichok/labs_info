import time
from pwm_dac import PWM_DAC_sin
def treug_wave(f, sf):
    try:
        a=PWM_DAC_sin(12, 500, 4.2)
        t=0
        while True:
            a.setvol(((t*f)%1)*a.dyrange)
            t+=1/sf
            time.sleep(1/sf)
    finally:
        a.deinit()