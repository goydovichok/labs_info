from decimal2binary import decimal2binary as d2b
import RPi.GPIO as rpg
class R2R_DAC:
    def __init__(self, gpio_bits=[22,27,17,26,25,21,20,16], dynamic_range=3.00, verbose = False):
        self.bits = gpio_bits
        self.dyrange = dynamic_range
        self.verbose = verbose

        rpg.setmode(rpg.BCM)
        rpg.setup(self.bits, rpg.OUT, initial = 0)
    def deinit(self):
        rpg.output(self.bits, 0)
        rpg.cleanup()
    def setnum(self, n):
        if n <= 255 and n >=0:
            b=d2b(n)
            print(f'Число на вход ЦАП: {n}, биты: {b}')
            while True:
                try:
                    rpg.output(self.bits, b)
                finally: self.deinit()
        else: print('ERROR! PLS, CHANGE NUMBER')
        if __name__ == "__main__":
            try:
                dac=R2R_DAC()
                dac.setnum(95)
            finally:
                self.deinit(verbose=True)
    def setvol(self, v):
        if v <= self.dyrange and v>=0:
            x=round((v/self.dyrange)*256)
            b=d2b(x)
            print(f'Число на вход ЦАП: {x}, биты: {b}')
            try:
                while True:
                    rpg.output(self.bits, b)
            finally: self.deinit()
        else: print('Dynamic range error')
        if __name__ == "__main__":
            try:
                dac=R2R_DAC(verbose=True)
                dac.setvol(1.2)
            finally:
                self.deinit()



class r2rsin:
    def __init__(self, gpio_bits=list(reversed([22,27,17,26,25,21,20,16])), dynamic_range=3.00, verbose = False):
        self.bits = gpio_bits
        self.dyrange = dynamic_range
        self.verbose = verbose

        rpg.setmode(rpg.BCM)
        rpg.setup(self.bits, rpg.OUT, initial = 0)
    def deinit(self):
        rpg.output(self.bits, 0)
        rpg.cleanup()
    def setvol(self, v):
        x=round((v/self.dyrange)*255)
        b=d2b(x)
        rpg.output(self.bits, b)