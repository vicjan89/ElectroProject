from classes import View
from views.func_graph_elements import *


class VCT(View):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (4, 0)}

    def draw(self):
        self.te.circle(self.x+2, self.y+7, 4)
        self.te.lines((self.x, self.y), (self.x, self.y+3))
        self.te.lines((self.x+4, self.y), (self.x+4, self.y+3))
        self.te.label(self.x, self.y, getattr(self.e, self.c[0]).name, 'sw', 2)
        self.te.label(self.x+4, self.y, getattr(self.e, self.c[1]).name, 'se', 2)
        self.te.label(self.x+6, self.y+7, self.e.name, 'e')


