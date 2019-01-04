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
