import smbus
import time

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose=True, bus_number=1):
        self.bus_number = bus_number
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
        self.verbose = verbose
        self.dynamic_range = dynamic_range
        
        try:
            self.bus = smbus.SMBus(bus_number)
            if self.verbose:
                print(f"I2C шина {bus_number} успешно открыта")
                self._check_connection()
        except Exception as e:
            print(f"Ошибка при открытии I2C шины {bus_number}: {e}")
            print("Проверьте, что I2C включен: sudo raspi-config -> Interface Options -> I2C -> Enable")
            raise

    def _check_connection(self):
        """Проверяет наличие устройства на I2C шине"""
        try:
            self.bus.write_quick(self.address)
            if self.verbose:
                print(f"Устройство с адресом 0x{self.address:02X} обнаружено")
        except Exception as e:
            print(f"ВНИМАНИЕ: Устройство с адресом 0x{self.address:02X} не отвечает")
            print("Проверьте:")
            print("  1. Правильно ли подключен MCP4725")
            print("  2. Правильный ли адрес устройства (по умолчанию 0x60 или 0x61)")
            print("  3. Проверьте подключение: i2cdetect -y 1")
            raise

    def deinit(self):
        """Закрывает I2C соединение"""
        try:
            self.bus.close()
            if self.verbose:
                print("I2C соединение закрыто")
        except:
            pass

    def set_number(self, number):
        """Устанавливает выходное напряжение по числовому значению (0-4095)"""
        if not isinstance(number, int):
            print("Ошибка: На вход ЦАП можно подавать только целые числа")
            return False

        if not (0 <= number <= 4095):
            print(f"Ошибка: Число {number} выходит за разрядность MCP4725 (12 бит, 0-4095)")
            return False

        first_byte = self.wm | self.pds | (number >> 8)
        second_byte = number & 0xFF
        
        try:
            self.bus.write_byte_data(self.address, first_byte, second_byte)
            if self.verbose:
                print(f"Число: {number}, данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]")
            return True
        except OSError as e:
            print(f"Ошибка I2C при записи: {e}")
            print("Проверьте физическое подключение MCP4725 и питание")
            return False
        except TimeoutError:
            print("Ошибка: Таймаут подключения к устройству")
            print("Проверьте:")
            print("  - Надежность проводов (SDA, SCL, GND, VCC)")
            print("  - Питание MCP4725 (обычно 3.3V или 5V)")
            print("  - Подтягивающие резисторы на линиях SDA/SCL")
            return False

    def set_voltage(self, voltage):
        """Устанавливает выходное напряжение"""
        if voltage < 0.0 or voltage > self.dynamic_range:
            if self.verbose:
                print(f"Ошибка: Напряжение {voltage}V выходит за диапазон (0.00 - {self.dynamic_range:.2f} В)")
            return False
        
        number = int(voltage / self.dynamic_range * 4095)
        success = self.set_number(number)
        
        if success and self.verbose:
            print(f"Установлено напряжение: {voltage:.2f}V")
        
        return success


def scan_i2c_devices():
    """Сканирует I2C шину на наличие устройств"""
    print("\nСканирование I2C устройств...")
    try:
        bus = smbus.SMBus(1)
        devices = []
        for address in range(0x03, 0x78):
            try:
                bus.write_quick(address)
                devices.append(address)
                print(f"Найдено устройство: 0x{address:02X}")
            except:
                pass
        bus.close()
        
        if devices:
            print(f"\nВсего найдено устройств: {len(devices)}")
            print(f"Типичный адрес MCP4725: 0x60 или 0x61")
        else:
            print("Устройства не найдены!")
            print("Проверьте подключение и питание")
        
        return devices
    except Exception as e:
        print(f"Ошибка сканирования: {e}")
        return []


if __name__ == "__main__":
    print("=== MCP4725 ЦАП драйвер ===\n")
    
    # Сканируем I2C устройства для диагностики
    found_devices = scan_i2c_devices()
    
    # Проверяем, есть ли типичный адрес MCP4725
    expected_address = 0x61
    if expected_address not in found_devices:
        print(f"\nВНИМАНИЕ: Адрес 0x{expected_address:02X} не найден!")
        print("Проверьте подключение или попробуйте другие адреса:")
        print("  - 0x60 (адрес по умолчанию, если A0 подключен к GND)")
        print("  - 0x61 (адрес по умолчанию, если A0 подключен к VCC)")
        print("  - 0x62, 0x63 (другие варианты подключения A0)")
        
        # Предлагаем выбрать адрес
        try:
            addr_input = input("\nВведите адрес устройства в HEX (например, 60): ")
            if addr_input:
                expected_address = int(addr_input, 16)
                print(f"Использую адрес: 0x{expected_address:02X}")
        except:
            pass
    
    try:
        # Инициализируем ЦАП
        dac = MCP4725(dynamic_range=4.24, address=expected_address, verbose=True)
        
        print("\nГотов к работе. Введите напряжение от 0 до 4.24 В")
        print("Для выхода введите 'q'\n")
        
        while True:
            try:
                user_input = input("Введите напряжение в Вольтах: ")
                
                if user_input.lower() == 'q':
                    print("Выход...")
                    break
                
                voltage = float(user_input)
                dac.set_voltage(voltage)
                print()  # пустая строка для читаемости
                
            except ValueError:
                print("Ошибка: Введите число или 'q' для выхода\n")
                
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
    finally:
        if 'dac' in locals():
            dac.deinit()
        print("Программа завершена")
