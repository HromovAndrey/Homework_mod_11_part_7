# Завдання 2
# Створіть клас температурного датчика, де обмежується
# температура в межах прийнятних для датчика значень, за
# допомогою property().
class TemperatureSensor:
    def __init__(self):
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if -50 <= value <= 150:
            self._temperature = value
        else:
            print("Error: Temperature out of range. Please provide a temperature between -50°C and 150°C.")

sensor = TemperatureSensor()

sensor.temperature = 25
print("Current temperature:", sensor.temperature)

sensor.temperature = 200
