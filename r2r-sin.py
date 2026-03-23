import r2r_dac as r2r
import signal_generator as sg


amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000
sampling_period = 1.0 / sampling_frequency

if __name__ == "__main__":
    try:
        massive = [16, 20, 21, 25, 26, 17, 27, 22]
        dac = r2r.R2R_DAC(massive, 3.0, True)

        time_counter = 0

        while True:
            normalized_value = sg.get_sin_wave_amplitude(signal_frequency, time_counter)

            voltage = normalized_value * amplitude

            dac.set_voltage(voltage)

            time_counter += sampling_period

            sg.wait_for_sampling_period(sampling_frequency)

    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем")
    finally:
        dac.deinit()
