import smbus
import time

class MCP4752():
    def __init__(self,dynamic_range,address=0x61,verbose=True):
        self.bus=smbus.SMBus(1)
        time.sleep(1)
        self.address=address
        self.wm=0x00
        self.pds=0x00

        self.verbose=verbose
        self.dynamic_range=dynamic_range
    def deinit(self):
        self.bus.close()
    def set_number(self,number):
        if not isinstance(number,int):
            print("на вход ЦАП можно подавать только целые числа")
        if not ((0<=number) and (number<=3308)):
            print("число выходит за диапазон MCP4752 (0.0-4.2В)")
            return
        
        first_byte=self.wm|self.pds|number>>8
        second_byte=number&0xFF
        self.bus.write_byte_data(0x61,first_byte,second_byte)

        if self.verbose:
            print(f"число: {number}, отправленные пр I2C данные: [0x{(self.address<<1):02X},0x{first_byte:02X},0x{second_byte:02X}]\n")
    def set_voltage(self,voltage):
        value=int(voltage/self.dynamic_range*4095)
        self.set_number(value)

if __name__=="__main__":
    try:
        m=MCP4752(5.2,0x61,True)
        while True:
            try:
                voltage=float(input("Введите напряжение в Вольтах: " ))
                m.set_voltage(voltage)
            except ValueError:
                print("вы ввели не число.")
    finally:
        m.deinit()