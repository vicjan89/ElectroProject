from classes import View
from views.func_graph_elements import *


class Vrelay(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (15, 0)}

    def draw(self):
        x = self.x
        y = self.y
        self.te.lines((x,y), (x+5, y))
        self.te.lines((x+10, y), (x+15, y))
        self.te.lines((x+5, y-5), (x+5, y+5), (x+10, y+5), (x+10, y-5), cycle=True)
        self.te.label(x+7, y+7, self.e.name, 'n')
        self.te.label(x, y, getattr(self.e, self.c[0]).name, 's')
        self.te.label(x+15, y, getattr(self.e, self.c[1]).name, 's')

class VcontNo(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (16, 0)}
    @staticmethod
    def draw_no(te, x, y, name, name1='', name2=''):
        te.lines((x, y), (x+3, y), (x+13, y+5))
        te.lines((x+13, y), (x+16, y))
        te.label(x+8, y+5, name, 'n')
        te.label(x, y, name1, 's')
        te.label(x+16, y, name2, 's')

    def draw(self):
        self.draw_no(self.te, self.x, self.y, self.e.name, getattr(self.e, self.c[0]).name, getattr(self.e, self.c[1]).name)

class VcontNc(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (16, 0)}

    @staticmethod
    def draw_nc(te, x, y, name, name1='', name2=''):
        te.lines((x, y), (x+3, y), (x+13, y-5))
        te.lines((x+12, y-5), (x+12, y), (x+16, y))
        te.label(x+8, y, name, 'n')
        te.label(x, y, name1, 's')
        te.label(x+16, y, name2, 's')

    def draw(self):
        self.draw_nc(self.te, self.x, self.y, self.e.name, getattr(self.e, self.c[0]).name, getattr(self.e, self.c[1]).name)

class VcontNoc(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (16, 0),
                                   self.c[2]: (12,-4)}

    def draw(self):
        x = self.x
        y = self.y
        self.te.lines((x, y), (x+3, y), (x+13, y-5))
        self.te.lines((x+13, y), (x+16, y))
        self.te.lines((x+12, y-4), (x+12, y-6))
        self.te.label(x+8, y, self.e.name, 'n')
        self.te.label(x, y, getattr(self.e, self.c[0]).name, 's')
        self.te.label(x+16, y, getattr(self.e, self.c[1]).name, 's')
        self.te.label(x+13, y-6, getattr(self.e, self.c[2]).name, 'sw')
