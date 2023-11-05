from dataclasses import dataclass


from classes import Element, View


class VXT(View):

    def draw(self):
        d = 2
        self.te.circle(self.x, self.y, 1.2)
        self.te.lines((self.x - d, self.y -d), (self.x + d, self.y + d))
        self.te.label(self.x, self.y, self.e.name, s=2)


