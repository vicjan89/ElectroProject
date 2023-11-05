from classes import View
from views.func_graph_elements import *


class Vbox(View):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            i = 0
            self.correspondence = dict()
            while i < len(self.c):
                self.correspondence[self.c[i]] = (i % 2 * 30, - int(i / 2) * 15)
                i += 1

    def draw(self):
        y = self.y - len(self.c) // 2 * 15 + 10
        self.te.lines((self.x, self.y+10), (self.x+30, self.y+10), (self.x+30, y), (self.x, y), cycle=True)
        i = 0
        while i < len(self.c):
            self.te.label(self.x + i % 2 * 30, self.y - i // 2 * 15, getattr(self.e, self.c[i]).name,
                          'w' if i%2 else 'e', 2)
            i += 1
        self.te.label(self.x + 15, self.y + 10, self.e.name, 's')


