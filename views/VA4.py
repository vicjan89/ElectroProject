from dataclasses import dataclass


from classes import Element, View


@dataclass
class VA4Seom(View):

    def draw(self):
        self.te.background('A4Seom.pdf')

class VA4(View):

    def draw(self):
        self.te.background('A4.pdf')
