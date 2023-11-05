from classes import View
from views.func_graph_elements import *


class VDiode_bridge(View):

    def __post_init__(self):
        self.correspondence = {'plus': (-10, 0),
                          'minus': (10, 0),
                          'in1': (0, -10),
                          'in2': (0, 10)}

    def draw(self):
        self.te.latex(diode_bridge(self.x, self.y, self.e.name))


