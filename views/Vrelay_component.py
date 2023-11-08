from classes import View
from views.func_graph_elements import *


class Vrelay(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (15, 0)}

    def draw(self):
        self.te.latex(relay(self.x, self.y, getattr(self.e, self.c[0]).name, getattr(self.e, self.c[1]).name, self.e.name))

class VcontNo(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (16, 0)}

    def draw(self):
        self.te.latex(contact_no(self.x, self.y, getattr(self.e, self.c[0]).name, getattr(self.e, self.c[1]).name, self.e.name))

class VcontNc(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (16, 0)}

    def draw(self):
        self.te.latex(contact_nc(self.x, self.y, getattr(self.e, self.c[0]).name, getattr(self.e, self.c[1]).name, self.e.name))

class VcontNoc(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (16, 0),
                                   self.c[2]: (12,-4)}

    def draw(self):
        self.te.latex(contact_noc(self.x, self.y, getattr(self.e, self.c[0]).name, getattr(self.e, self.c[1]).name,
                                  getattr(self.e, self.c[2]).name, self.e.name))
