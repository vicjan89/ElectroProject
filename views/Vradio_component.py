from classes import View
from views.func_graph_elements import *
from views.Vrelay_component import VcontNo


class VDiode(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correspondence = {'anode': (0, 0),
                               'cathode': (10, 0)}

    def draw(self):
        x = self.x
        y = self.y
        self.te.lines((x, y), (x+10, y))
        self.te.lines((x+2,y-3), (x+2, y+3), (x+7, y), cycle=True)
        self.te.lines((x+7, y-3), (x+7, y+3))
        self.te.label(self.x+5, self.y+1, self.e.name, 'n')

class VDiodeB(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correspondence = {'anode': (0, 0),
                               'cathode': (0, -10)}

    @staticmethod
    def draw_(te, x, y, name):
        te.lines((x, y), (x, y-10))
        te.lines((x-3,y-2), (x+3, y-2), (x, y-7), cycle=True)
        te.lines((x+3, y-7), (x-3, y-7))
        te.label(x+3, y-5, name, 'e')

    def draw(self):
        self.draw_(self.te, self.x, self.y, self.e.name)

class VDiodeL(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correspondence = {'anode': (0, 0),
                               'cathode': (-10, 0)}

    def draw(self):
        x = self.x
        y = self.y
        self.te.lines((x, y), (x-10, y))
        self.te.lines((x-2,y-3), (x-2, y+3), (x-7, y), cycle=True)
        self.te.lines((x-7, y-3), (x-7, y+3))
        self.te.label(self.x-5, self.y+1, self.e.name, 'n')

class VDiode_bridge(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correspondence = {'plus': (-10, 0),
                          'minus': (10, 0),
                          'in1': (0, -10),
                          'in2': (0, 10)}

    def draw(self):
        self.te.latex(diode_bridge(self.x, self.y, self.e.name))


class VHL(View):
    '''Класс для визуализации лампы как сигнальной так и освещения'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correspondence = {'k1': (0, 0),
                               'k2': (10, 0)}

    def draw(self):
        d = 3.54
        self.te.circle(self.x+5, self.y, 5)
        self.te.lines((self.x-d+5, self.y-d), (self.x+d+5, self.y+d))
        self.te.lines((self.x-d+5, self.y+d), (self.x+d+5, self.y-d))
        self.te.label(self.x, self.y, getattr(self.e, self.c[0]).name, 'sw', 2)
        self.te.label(self.x+10, self.y, getattr(self.e, self.c[1]).name, 'se', 2)
        self.te.label(self.x+5, self.y+5, self.e.name, 'n')

class VHL_SA(View):
    '''Класс для визуализации лампы освещения с выключателем'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correspondence = {'k1': (0, 0),
                               'k2': (28, 0)}

    def draw(self):
        d = 3.54
        self.te.circle(self.x+21, self.y, 5)
        self.te.lines((self.x-d+21, self.y-d), (self.x+d+21, self.y+d))
        self.te.lines((self.x-d+21, self.y+d), (self.x+d+21, self.y-d))
        self.te.lines((self.x+26, self.y), (self.x+28, self.y))
        self.te.lines((self.x, self.y-6), (self.x, self.y+6), (self.x+28, self.y+6), (self.x+28, self.y-6), cycle=True)
        VcontNo.draw_no(self.te, self.x, self.y, '')
        self.te.label(self.x, self.y, getattr(self.e, self.c[0]).name, 'sw', 2)
        self.te.label(self.x+28, self.y, getattr(self.e, self.c[1]).name, 'se', 2)
        self.te.label(self.x+13, self.y+5, self.e.name, 'n')

class VR(View):
    '''Класс для визуализации резистора'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correspondence = {'k1': (0, 0),
                               'k2': (10, 0)}

    def draw(self):
        self.te.lines((self.x, self.y-2.5), (self.x, self.y+2.5),(self.x+10, self.y+2.5), (self.x+10,self.y-2.5),
                      cycle=True)
        self.te.label(self.x, self.y, getattr(self.e, self.c[0]).name, 'sw', 2)
        self.te.label(self.x+10, self.y, getattr(self.e, self.c[1]).name, 'se', 2)
        self.te.label(self.x+5, self.y+2.5, self.e.name, 'n')

