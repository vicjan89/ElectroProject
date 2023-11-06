from classes import View
from views.func_graph_elements import *


class VPA(View):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (4, 0)}

    def draw(self):
        self.te.circle(self.x+4, self.y, 4)
        self.te.label(self.x, self.y, getattr(self.e, self.c[0]).name, 'sw', 2)
        self.te.label(self.x+8, self.y, getattr(self.e, self.c[1]).name, 'se', 2)
        self.te.label(self.x+4, self.y+4, self.e.name, 'n')
        self.te.label(self.x+4, self.y, 'A', 'c')


