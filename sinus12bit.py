import numpy as np
import time
from i2cdac import MCPsin
def get_sinus_wave_ampletude(f, t):
    return (np.sin(2*np.pi*f*t)+1)/2
def sinus(f, sf):
    try:
        a=MCPsin(12, 4.8)
        t=0
        while True:
            a.setvol(get_sinus_wave_ampletude(f, t)*a.dyrange)
            t+=1/sf
            time.sleep(1/sf)
    finally:
        a.deinit()