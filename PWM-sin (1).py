import signal_generator as sg
import time
import dac_shim as pwm

amplitude=1
signal_frequency=20
sampling_frequency=500


try:
    p=pwm.PWM_DAC(12,10000,3.15,True)
    while True:
        time=0
        while time<=1/signal_frequency:
            signal=amplitude*sg.get_sin_wave_amplitude(signal_frequency,time)
            p.set_voltage(signal)
            sg.wait_for_sampling_period(sampling_frequency)
            time+=1/sampling_frequency
finally:
    p.deinit()