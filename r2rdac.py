from decimal2binary import decimal2binary as d2b
import RPi.GPIO as rpg
rpg.setmode(rpg.BCM)
leds=list(reversed([22,27,17,26,25,21,20,16]))
rpg.setup(leds, rpg.OUT)
try:
    x = float(input('Введите напряжение в Вольтах: '))
    if 0 <= x and x <= 3:
        t = round((x/3.011)*256)
    else:
        print("Напряжение выходит за динамический диапазон ЦАП (0.00 - 3.00 В)")
        print("Устанавливаем 0 В")
        t=0
    b = d2b(t)
    print(f'Число на вход ЦАП: {t}, биты: {b}')
    while True:
        rpg.output(leds, b)
finally:
    rpg.output(leds, 0)
    rpg.cleanup()