import pwm_dac as pd
import signal_generator as sg

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000
sampling_period = 1.0 / sampling_frequency
time_counter = 0.0

if __name__ == "__main__":
    try:
        dac = pd.PWM_DAC(12, 1000, 3.3, True)
        while True:
            normalized_value = sg.get_sin_wave_amplitude(signal_frequency, time_counter)

            voltage = normalized_value * amplitude

            dac.set_voltage(voltage)

            time_counter += sampling_period

            sg.wait_for_sampling_period(sampling_frequency)
    except ValueError:
        print("Введите корректное число")
    finally:
        dac.deinit()
