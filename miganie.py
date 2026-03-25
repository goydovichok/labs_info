import smbus
import time

class MCP4725:
    def __init__(self, dynamic_range, address=0x60, verbose=True):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_voltage(self, voltage):
        if voltage < 0:
            voltage = 0
        if voltage > self.dynamic_range:
            voltage = self.dynamic_range
        
        value = int(voltage / self.dynamic_range * 4095)
        
        data = [0x40, (value >> 4) & 0xFF, (value << 4) & 0xFF]
        
        try:
            self.bus.write_i2c_block_data(self.address, data[0], [data[1], data[2]])
            if self.verbose:
                print(f"Установлено напряжение: {voltage:.2f}V (значение: {value})")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    try:
        dac = MCP4725(dynamic_range=4.24)
        
        dac.set_voltage(1.5)
        time.sleep(2)
        dac.set_voltage(2.5)
        time.sleep(2)
        dac.set_voltage(3.3)
        
    finally:
        dac.deinit()
