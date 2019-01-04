"""
热水器：
50-70：可以洗澡
100：可以饮用
"""


class WaterHeater:
    "热水器：战胜寒冬的有力武器。"

    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temp):
        self.__temperature = temp
        print(f'当前温度为：{self.__temperature}')
        self.notifies()

    def add_observer(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer:
    "洗澡模式和引用模式的父类"

    def update(self, waterheater):
        pass


class ShowerMode(Observer):
    "该模式用于洗澡用"

    def update(self, waterheater):
        if 50 <= waterheater.get_temperature() <= 70:
            print('水温正好！可以用来洗澡了。')


class DrinkMode(Observer):
    def update(self, waterheater):
        if waterheater.get_temperature() >= 100:
            print('水已烧开！可以用来饮用了。')


if __name__ == '__main__':

    heater = WaterHeater()
    shower_observer = ShowerMode()
    drink_observer = DrinkMode()
    heater.add_observer(shower_observer)
    heater.add_observer(drink_observer)
    heater.set_temperature(40)
    heater.set_temperature(66)
    heater.set_temperature(100)

"""
当前温度为：40
当前温度为：66
水温正好！可以用来洗澡了。
当前温度为：100
水已烧开！可以用来饮用了。
"""
