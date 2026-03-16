import numpy as np
import time
from pwm_dac import PWM_DAC_sin
def get_sinus_wave_ampletude(f, t):
    return (np.sin(2*np.pi*f*t)+1)/2
def sinus(f, sf):
    try:
        a=PWM_DAC_sin(12, 500, 4.2)
        t=0
        while True:
            a.setvol(get_sinus_wave_ampletude(f, t)*a.dyrange)
            t+=1/sf
            time.sleep(1/sf)
    finally:
        a.deinit()