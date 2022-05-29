'''Модуль для описания графических элементов электрических схем.'''

from BasicElements import *


class ContactOpen(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [15, 5], [15, 0], [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.labels_xy = [[8, 6]]
        self.labels = [name]


class ContactClose(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [16, -5], [15, -5], [15, 0], [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[10, 5]]
        self.labels = [name]


class ContactOpenTimeOn(ContactOpen):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, 3], [9, 8], [11, 2], [11, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 6], [7, 7], [8, 7.7], [9, 8], [11, 8], [12, 7.7], [13, 7], [14, 6]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 10]]


class ContactOpenTimeOff(ContactOpen):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, 3], [9, 8], [11, 2], [11, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 10], [7, 9], [8, 8.3], [9, 8], [11, 8], [12, 8.3], [13, 9], [14, 10]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 11]]


class ContactCloseTimeOn(ContactClose):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, -3], [9, 7], [11, -2], [11, 7]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 5], [7, 6], [8, 6.7], [9, 7], [11, 7], [12, 6.7], [13, 6], [14, 5]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 9]]


class ContactCloseTimeOff(ContactClose):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, -3], [9, 6], [11, -2], [11, 6]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 8], [7, 7], [8, 6.3], [9, 6], [11, 6], [12, 6.3], [13, 7], [14, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 9]]


class Diode(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [15, 0], [5, 3.5], [10, 0], [5, -3.5], [5, 3.5], [10, 3.5], [10, -35]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.MOVETO,
                      Path.LINETO]
        self.labels_xy = [[10, 4]]
        self.labels = [name]


class Winding(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight)
        self.vertices = [[0, 0], [5, 0], [5, 5], [10, 5], [10, -5], [5, -5], [5, 0], [10, 0], [15, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                      Path.MOVETO, Path.LINETO]
        self.labels_xy = [[7, 6]]
        self.labels = [name]


class CT_W(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [0, 3.5], [4, 3.5], [4, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.centers = [[2, 7]]
        self.radii = [4]
        self.labels_xy = [[0, 12]]
        self.labels = [name]


class ConnectionDetachable(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[5, 5], [0, 0], [5, -5], [7, 5], [2, 0], [7, -5]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[1, 2]]
        self.labels = [name]

