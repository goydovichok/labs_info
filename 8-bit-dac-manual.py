import RPi.GPIO as GPIO

dynamic_range = 3.15

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавлниваем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)


def number_to_dac(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


dac_bits = [22, 27, 17, 26, 25, 21, 20, 16]
dac_bits = dac_bits[::-1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT)
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            GPIO.output(dac_bits, number_to_dac(number))

        except ValueError:
            print("Вы ввели не число, попробуйте еще раз\n")
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()
