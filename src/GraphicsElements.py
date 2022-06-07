'''Модуль для описания графических элементов электрических схем.'''

from src.BasicElements import *


class ContactOpen(ElementGraph):
    '''Контакт нормально-разомкнутый.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [15, 5], [15, 0], [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.labels_xy = [[8, 6]]
        self.labels = [name]


class ContactClose(ElementGraph):
    '''Контакт нормально-замкнутый.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [16, -5], [15, -5], [15, 0], [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[10, 5]]
        self.labels = [name]


class ContactOpenClose(ElementGraph):
    '''Контакт перекидной.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [15, 5], [15, 0], [20, 0], [14,4],[14,10],[20,10]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO,Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[8, 6]]
        self.labels = [name]


class ContactOpenTimeOn(ContactOpen):
    '''Контакт нормально-разомкнутый с задержкой на срабатывание.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, 3], [9, 8], [11, 2], [11, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 6], [7, 7], [8, 7.7], [9, 8], [11, 8], [12, 7.7], [13, 7], [14, 6]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 10]]


class ContactOpenTimeOff(ContactOpen):
    '''Контакт нормально-разомкнутый с задержкой на возврат.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, 3], [9, 8], [11, 2], [11, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 10], [7, 9], [8, 8.3], [9, 8], [11, 8], [12, 8.3], [13, 9], [14, 10]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 11]]


class ContactCloseTimeOn(ContactClose):
    '''Контакт нормально-замкнутый с задержкой на срабатывание.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, -3], [9, 7], [11, -2], [11, 7]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 5], [7, 6], [8, 6.7], [9, 7], [11, 7], [12, 6.7], [13, 6], [14, 5]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 9]]


class ContactCloseTimeOff(ContactClose):
    '''Контакт нормально-замкнутый с задержкой на возврат.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, -3], [9, 6], [11, -2], [11, 6]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 8], [7, 7], [8, 6.3], [9, 6], [11, 6], [12, 6.3], [13, 7], [14, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 9]]


class Diode(ElementGraph):
    '''Диод.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [15, 0], [5, 3.5], [10, 0], [5, -3.5], [5, 3.5], [10, 3.5], [10, -35]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.MOVETO,
                      Path.LINETO]
        self.labels_xy = [[10, 4]]
        self.labels = [name]


class Winding(ElementGraph):
    '''Обмотка реле.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight)
        self.vertices = [[0, 0], [5, 0], [5, 5], [10, 5], [10, -5], [5, -5], [5, 0], [10, 0], [15, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                      Path.MOVETO, Path.LINETO]
        self.labels_xy = [[7, 6]]
        self.labels = [name]


class CT_W(ElementGraph):
    '''Обмотка трансформатора тока.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [0, 3.5], [4, 3.5], [4, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.centers = [[2, 7]]
        self.radii = [4]
        self.labels_xy = [[0, 12]]
        self.labels = [name]


class ConnectionDetachable(ElementGraph):
    '''Разъёмное соединение.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[5, 5], [0, 0], [5, -5], [7, 5], [2, 0], [7, -5]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[1, 2]]
        self.labels = [name]


class Resistor(ElementGraph):
    '''Резистор.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [5, -2.5], [5, 2.5], [15, 2.5], [15,-2.5],[5,-2.5],[15,0],[20,0]]
        self.codes = [Path.MOVETO, Path.LINETO,Path.MOVETO,Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,Path.MOVETO,Path.LINETO]
        self.labels_xy = [[8, 3]]
        self.labels = [name]


class Capacitor(ElementGraph):
    '''Конденсатор.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [5, -5], [5, 5], [6, -5], [6,5],[6,0],[11,0]]
        self.codes = [Path.MOVETO, Path.LINETO,Path.MOVETO,Path.LINETO, Path.MOVETO,Path.LINETO, Path.MOVETO,Path.LINETO]
        self.labels_xy = [[8, 2]]
        self.labels = [name]


class Ground(ElementGraph):
    '''Заземление.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [0, -5], [-5, -5], [5, -5], [-3, -6], [3,-6],[-1,-7],[1,-7]]
        self.codes = [Path.MOVETO, Path.LINETO,Path.MOVETO,Path.LINETO, Path.MOVETO,Path.LINETO, Path.MOVETO,Path.LINETO]


class BI(ElementGraph):
    '''Дискретный вход.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [5, 5], [15, 5], [15, -5], [5, -5], [5, 5], [15, 0], [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                      Path.MOVETO, Path.LINETO]
        self.labels_xy = [[10, 0]]
        self.labels = [name]

class Power(ElementGraph):
    '''Блок питания устройства.'''

    def __init__(self, name='',highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [5, 5], [15, 5], [15, -5], [5, -5], [5, 5], [15, 0], [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                      Path.MOVETO, Path.LINETO]
        self.labels_xy = [[10, 0]]
        self.labels = [name]

class Measurement(ElementGraph):
    '''Измерительный прибор.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.centers = [[4, 0]]
        self.radii = [4]
        self.labels_xy = [[4, 0]]
        self.labels = [name]

class ButtonOpen(ContactOpen):
    '''Кнопка управления нормально-разомкнутая.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[10, 2.5], [10, 3.5], [10, 4.5], [10, 5.5],[7,5],[7,5.5],[13,5.5],[13,5]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO,Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[8, 6]]
        self.labels = [name]

class ButtonClose(ContactClose):
    '''Кнопка управления нормально-замкнутая.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[10,-1.5],[10,-0.5],[10,0.5],[10,1.5],[10, 2.5], [10, 3.5], [10, 4.5], [10, 5.5],[7,5],[7,5.5],[13,5.5],[13,5]]
        self.codes += [Path.MOVETO, Path.LINETO,Path.MOVETO, Path.LINETO,Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO,Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[8, 6]]
        self.labels = [name]

class Bulb(ElementGraph):
    '''Лампочка сигнальная.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.centers = [[10, 0]]
        self.radii = [4]
        self.vertices += [[0,0],[6,0],[20,0],[14,0],[7.2,2.8],[12.8,-2.8],[7.2,-2.8],[12.8,2.8]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.MOVETO,Path.LINETO,Path.MOVETO,Path.LINETO,Path.MOVETO,Path.LINETO,Path.MOVETO,Path.LINETO]
        self.labels_xy = [[10, 4]]
        self.labels = [name]