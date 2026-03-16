import numpy as np
import time
from R2R_DAC import r2rsin
def get_sinus_wave_ampletude(f, t):
    return (np.sin(2*np.pi*f*t)+1)/2
def sinus(f, sf):
    try:
        a=r2rsin()
        t=0
        while True:
            a.setvol(get_sinus_wave_ampletude(f, t)*a.dyrange)
            t+=1/sf
            time.sleep(1/sf)
    finally:
        a.deinit()