import RPi.GPIO as r

class PWM_DAC():
    def __init__(self,gpio_pin,pwm_frequency,dynamic_range,verbose=False):
        self.gpio_pin=gpio_pin
        self.pwm_frequency=pwm_frequency
        self.dynamic_range=dynamic_range
        self.verbose=verbose


        r.setmode(r.BCM)
        r.setup(self.gpio_pin,r.OUT)
        self.pwm=r.PWM(self.gpio_pin,self.pwm_frequency)
        self.pwm.start(0)
    def deinit(self):
        r.output(self.gpio_pin,0)
        r.cleanup()
    def set_voltage(self,voltage):
    
        
        
        if ((voltage<=self.dynamic_range) and (voltage>=0)):
            duty=((voltage/self.dynamic_range)*100)
            #print(duty)
            self.pwm.ChangeDutyCycle(duty)
            return
            
        
        print("напряжение вне рабочего диапазона.")
        print("Устанавливаем напряжение 0.0В")
        self.pwm.ChangeDutyCycle(0)
        return
            
        
       
    



if __name__=="__main__":
    try:
        dac=PWM_DAC(12,200,3.15,True)
        while True:
            try:

                voltage=float(input("введите напряжение в Вольтах: "))
                
                dac.set_voltage(voltage)
                
            except ValueError:
                print("вы ввели не число")
    finally:
        dac.deinit()