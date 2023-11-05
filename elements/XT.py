from classes import Element, Connection, Apparatus

class XT(Element):

    def __init__(self, size: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = size
        for i in range(size):
            self.__dict__[f'k{i+1}'] = Connection(name=f'{self.name}-{i+1}', parent=self)

class Ground(Apparatus):

    trans = (('g', ''),)