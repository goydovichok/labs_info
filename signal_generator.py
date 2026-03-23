import math
import time


def get_sin_wave_amplitude(frequency, time):
    sin_val = math.sin(2 * math.pi * frequency * time)
    return (sin_val + 1) / 2


def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)
