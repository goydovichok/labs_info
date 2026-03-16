import time
from i2cdac import MCPsin
def treug_wave(f, sf):
    try:
        a=MCPsin(12, 4.8)
        t=0
        while True:
            a.setvol(((t*f)%1)*a.dyrange)
            t+=1/sf
            time.sleep(1/sf)
    finally:
        a.deinit()