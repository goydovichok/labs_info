import signal_generator as sg
import time
import mcp4725_driver as mcp

amplitude=1
signal_frequency=40
sampling_frequency=2000


try:
    m=mcp.MCP4752(5,0x61,True)
    while True:
        time=0
        while time<=1/signal_frequency:
            signal=amplitude*sg.triangle(signal_frequency,time)
            m.set_voltage(signal)
            sg.wait_for_sampling_period(sampling_frequency)
            time+=1/sampling_frequency
finally:
    m.deinit()