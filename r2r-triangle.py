import signal_generator as sg
import time
import R2R_dac2 as r

amplitude=1
signal_frequency=40
sampling_frequency=1000


try:
    r2r=r.R2R_DAC([16,20,21,25,26,17,27,22],3.15,True)
    while True:
        time=0
        while time<=1/signal_frequency:
            signal=amplitude*sg.triangle(signal_frequency,time)
            r2r.set_voltage(signal)
            sg.wait_for_sampling_period(sampling_frequency)
            time+=1/sampling_frequency
finally:
    r2r.deinit()