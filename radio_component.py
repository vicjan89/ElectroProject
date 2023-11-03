from classes import Element, Connection

class Diode(Element):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.anode = Connection(parent=self, name='анод')
        self.cathode = Connection(parent=self, name='катод')

    def encode(self):
        return super().encode('Diode')

class Diode_bridge(Element):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plus = Connection(parent=self, name='+')
        self.minus = Connection(parent=self, name='-')
        self.in1 = Connection(parent=self, name='~1')
        self.in2 = Connection(parent=self, name='~2')

    def encode(self):
        return super().encode('Diode_bridge')
