from dataclasses import dataclass


from classes import Element, View


@dataclass
class VXT(View):

    def draw(self):
        d = 2
        self.te.picture(
        self.te.circle(self.x, self.y, 1.5),
        self.te.lines((self.x - d, self.y -d), (self.x + d, self.y + d)),
        self.te.label(self.x, self.y, self.e.name)
        )

    def encode(self):
        return super().encode('VXT')

