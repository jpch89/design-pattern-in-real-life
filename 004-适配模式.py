class IHeightPerson:
    "接口类，提供空实现的方法，由子类去实现"

    def get_name(self):
        '获取姓名'
        pass

    def get_height(self):
        '获取身高'
        pass


class HighPerson(IHeightPerson):
    '个高的人'

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_height(self):
        return 170


class ShortPerson(IHeightPerson):
    '个矮的人'

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_real_height(self):
        return 160

    def get_shoes_height(self):
        return 6


class DecoratePerson(ShortPerson, IHeightPerson):
    '有高跟鞋搭配的人'

    def get_height(self):
        return super().get_real_height() + super().get_shoes_height()


def can_be_receptionist(person):
    """
    是否可以成为（高级酒店）接待员
    :param person: IHeightPerson 的对象
    :return: 是否符合做接待员的条件
    """
    return person.get_height() >= 165


if __name__ == '__main__':
    lira = HighPerson('Lira')
    print(lira.get_name() + '身高' + str(lira.get_height()) +
          '，完美如你，天生的美女！')
    print('是否适合做接待员:',
          '符合' if can_be_receptionist(lira) else '不符合')

    print()
    demi = DecoratePerson('Demi')
    print(demi.get_name() + '身高' + str(demi.get_height()) +
          '，在高跟鞋的适配下，你身高不输高圆圆，气质不输范冰冰！')
    print('是否适合做接待员:',
          '符合' if can_be_receptionist(demi) else '不符合')

"""
Lira身高170，完美如你，天生的美女！
是否适合做接待员: 符合

Demi身高166，在高跟鞋的适配下，你身高不输高圆圆，气质不输范冰冰！
是否适合做接待员: 符合
"""
