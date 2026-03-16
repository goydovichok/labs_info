import time
from R2R_DAC import r2rsin
def treug_wave(f, sf):
    try:
        a=r2rsin()
        t=0
        while True:
            a.setvol(((t*f)%1)*a.dyrange)
            t+=1/sf
            time.sleep(1/sf)
    finally:
        a.deinit()