from dataclasses import dataclass


from classes import Element, View


@dataclass
class VA4(View):

    def draw(self):
        self.te.background('A4.pdf')

    def encode(self):
        return super().encode('VA4')