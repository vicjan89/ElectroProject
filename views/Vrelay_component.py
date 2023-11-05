from classes import View
from views.func_graph_elements import *


class Vrelay(View):

    def __post_init__(self):
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (15, 0)}

    def draw(self):
        self.te.latex(relay(self.x, self.y, self.c[0], self.c[1], self.e.name))

