from classes import View
from views.func_graph_elements import *


class VDiode(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correspondence = {'anode': (0, 0),
                               'cathode': (10, 0)}

    def draw(self):
        self.te.latex(f'\\draw ({self.x}, {self.y}) to[diode] ({self.x + 10}, {self.y});')
        self.te.label(self.x+5, self.y+1, self.e.name, 'n')

class VDiodeL(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correspondence = {'anode': (0, 0),
                               'cathode': (-10, 0)}

    def draw(self):
        self.te.latex(f'\\draw ({self.x}, {self.y}) to[diode] ({self.x - 10}, {self.y});')
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

