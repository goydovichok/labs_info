import smbus
class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dyrange = dynamic_range
    def deinit(self):
        self.bus.close()
    def setnum(self, n):
        if not isinstance(n, int):
            print('На вход ЦАП можно подавать только целые числа')
        
        if not (0 <= n <= 2047):
            print("Число выходит за разрядность MCP4752 (12 бит)")
        
        b1 = self.wm | self.pds | n >> 8
        b2 = n & 0xFF
        self.bus.write_byte_data(self.address, b1, b2)

        if self.verbose:
            print(f"Число: {n}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{b1:02X}, 0x{b2:02X}]\n")
        if __name__ == '__main__':
            try:
                dac=MCP4725(5.0)
                dac.setnum(140)
            finally:
                self.deinit()
    def setvol(self, v):
        n=round(v/self.dyrange*2047)
        self.setnum(n)
        if __name__ == '__main__':
            try:
                dac=MCP4725(5.0)
                dac.setvol(3.0)
            finally:
                self.deinit()

class MCPsin:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dyrange = dynamic_range
    def deinit(self):
        self.bus.close()
    def setvol(self, v):
        try:
            n=round(v/self.dyrange*2047)
            b1 = self.wm | self.pds | n >> 8
            b2 = n & 0xFF
            self.bus.write_byte_data(self.address, b1, b2)
        finally:
            self.deinit()
        if __name__ == '__main__':
            try:
                dac=MCP4725(5.0)
                dac.setvol(3.0)
            finally:
                self.deinit()