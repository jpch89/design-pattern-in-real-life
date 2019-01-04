class Observer:
    "观察者的基类"

    def update(self, observer, object):
        pass


class Observable:
    "被观察者的基类"

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    "热水器：战胜寒冬的有力武器。"

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temp):
        self.__temperature = temp
        print(f'当前温度：{self.__temperature}')
        self.notify_observers()


class ShowerMode(Observer):
    "该模式用于洗澡用"

    def update(self, observable, object):
        if (isinstance(observable, WaterHeater) and
                50 <= observable.get_temperature() <= 70):
            print('水温正好！可以用来洗澡了。')


class DrinkMode(Observer):
    def update(self, observable, object):
        if (isinstance(observable, WaterHeater) and
                observable.get_temperature() >= 100):
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
当前温度：40
当前温度：66
水温正好！可以用来洗澡了。
当前温度：100
水已烧开！可以用来饮用了。
"""
