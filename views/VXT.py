from dataclasses import dataclass


from classes import Element, View


class VXT(View):

    def draw(self):
        self.te.circle(self.x, self.y, 1)
        self.te.label(self.x, self.y, self.e.name, s=2)

class VXT1(View):

    def draw(self):
        d = 1.5
        self.te.circle(self.x, self.y, 1)
        self.te.lines((self.x - d, self.y -d), (self.x + d, self.y + d))
        self.te.label(self.x, self.y, self.e.name, s=2)

class VXTcross(View):

    def draw(self):
        self.te.lines((self.x - 4, self.y), (self.x + 4, self.y ))
        self.te.circle(self.x, self.y, 1.2)
        self.te.label(self.x, self.y, self.e.name, s=2)

class VXTm(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (4, 0)}

    def draw(self):
        self.te.lines((self.x, self.y), (self.x + 4, self.y))
        self.te.circle(self.x, self.y, 1)
        self.te.circle(self.x+4, self.y, 1)
        self.te.label(self.x, self.y, getattr(self.e, self.c[0]).name, s=2)


class VG(View):

    def draw(self):
        x, y = self.x, self.y
        self.te.lines((x, y), (x, y-5))
        self.te.lines((x-5, y-5), (x+5, y - 5))
        self.te.lines((x-3, y-6), (x+3, y - 6))
        self.te.lines((x-1, y-7), (x+1, y - 7))
