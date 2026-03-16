import RPi.GPIO as rpg
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.pin = gpio_pin
        self.freq = pwm_frequency
        self.dyrange = dynamic_range
        self.verbose = verbose

        rpg.setmode(rpg.BCM)
        rpg.setup(self.pin, rpg.OUT, initial = 0)
    def deinit(self):
        rpg.output(self.pin, 0)
        rpg.cleanup()
    def setvol(self, v):
        try:
            p=rpg.PWM(self.pin, self.freq)
            p.start(v/self.dyrange*100)
            input('press enter to stop')
            p.stop()
        finally:
            self.deinit()
        if __name__ == '__main__':
            try:
                dac=PWM_DAC(12, 500, 3.1, True)
                dac.setvol(1.2)
            finally:
                self.deinit()


class PWM_DAC_sin:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.pin = gpio_pin
        self.freq = pwm_frequency
        self.dyrange = dynamic_range
        self.verbose = verbose
        rpg.setmode(rpg.BCM)
        rpg.setup(self.pin, rpg.OUT, initial = 0)
    def deinit(self):
        rpg.output(self.pin, 0)
        rpg.cleanup()
    def setvol(self, v):
        try:
            p=rpg.PWM(self.pin, self.freq)
            p.start(v)
        finally:
            self.deinit()
        if __name__ == '__main__':
            try:
                dac=PWM_DAC(12, 500, 3.1, True)
                dac.setvol(1.2)
            finally:
                self.deinit()