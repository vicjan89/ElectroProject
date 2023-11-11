from classes import View
from views.func_graph_elements import *


class VSQ(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (16, 0)}
    def draw(self):
        self.te.latex(contact_nc(self.x, self.y, getattr(self.e, self.c[0]).name, getattr(self.e, self.c[1]).name,
                                 self.e.name))