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
        self.te.circle(self.x, self.y, 1)
        self.te.circle(self.x+15, self.y, 1)

class VSACno(VSAC):

    def draw(self):
        super().draw()
        self.te.circle(self.x +11, self.y, 1, black=True)
