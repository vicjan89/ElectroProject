from classes import View
from views.func_graph_elements import *


class VSAC(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (15, 0)}

    def draw(self):
        self.te.lines((self.x, self.y-5), (self.x, self.y+10), (self.x + 15, self.y+10), (self.x+15, self.y-5), cycle=True)
        self.te.lines((self.x+4, self.y-3), (self.x+4, self.y+3))
        self.te.lines((self.x+11, self.y-3), (self.x+11, self.y+3))
        self.te.label(self.x, self.y, getattr(self.e, self.c[0]).name, 'sw', 2)
        self.te.label(self.x+15, self.y, getattr(self.e, self.c[1]).name, 'se', 2)
        self.te.label(self.x+7, self.y+10, self.e.name, 'n')
        self.te.label(self.x+4, self.y+3, 'О', 'n', 2)
        self.te.label(self.x+11, self.y+3, 'В', 'n', 2)
        # self.te.circle(self.x, self.y, 1)
        # self.te.circle(self.x+15, self.y, 1)

class VSACno(VSAC):

    def draw(self):
        super().draw()
        self.te.circle(self.x +11, self.y, 1, black=True)

class VSACnc(VSAC):

    def draw(self):
        super().draw()
        self.te.circle(self.x +4, self.y, 1, black=True)

class VSAC2(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (15, 0),
                                   self.c[2]: (0, -15),
                                   self.c[3]: (15, -15)}

    def draw(self):
        self.te.lines((self.x, self.y-20), (self.x, self.y+10), (self.x + 15, self.y+10), (self.x+15, self.y-20), cycle=True)
        self.te.lines((self.x+4, self.y-18), (self.x+4, self.y+3))
        self.te.lines((self.x+11, self.y-18), (self.x+11, self.y+3))
        self.te.label(self.x, self.y, getattr(self.e, self.c[0]).name, 'sw', 2)
        self.te.label(self.x+15, self.y, getattr(self.e, self.c[1]).name, 'se', 2)
        self.te.label(self.x, self.y-15, getattr(self.e, self.c[2]).name, 'sw', 2)
        self.te.label(self.x+15, self.y-15, getattr(self.e, self.c[3]).name, 'se', 2)
        self.te.label(self.x+7, self.y+10, self.e.name, 'n')
        self.te.label(self.x+4, self.y+3, 'М', 'n', 2)
        self.te.label(self.x+11, self.y+3, 'ТУ', 'n', 2)
        # self.te.circle(self.x, self.y, 1)
        # self.te.circle(self.x+15, self.y, 1)
        # self.te.circle(self.x, self.y-15, 1)
        # self.te.circle(self.x+15, self.y-15, 1)
        self.te.circle(self.x +11, self.y, 1, black=True)
        self.te.circle(self.x +4, self.y-15, 1, black=True)

class VSB(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (16, 0)}

    def draw(self):
        x = self.x
        y = self.y
        self.te.lines((x,y), (x+3,y),(x+13, y+5))
        self.te.lines((x+13, y),(x+16,y))
        self.te.label(x+8, y+7, self.e.name, 'n')
        self.te.label(x, y, getattr(self.e, self.c[0]).name, 's')
        self.te.label(x+16, y, getattr(self.e, self.c[1]).name, 's')

        self.te.lines((x+5, y+6), (x+5, y+7), (x + 11, y+7), (x+11, y+6))
        self.te.lines((x+7, y+2), (x+7, y+7))
        self.te.lines((x+9, y+3), (x+9, y+7))
