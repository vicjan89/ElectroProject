from classes import Element, Connection, Apparatus

class XT(Element):

    def __init__(self, size: int, jumpers: list = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = size
        for i in range(size):
            self.__dict__[f'k{i+1}'] = Connection(name=f'{self.name}-{i+1}', parent=self)
        if not jumpers:
            self.jumpers = [False for _ in range(size)]
        else:
            self.jumpers = jumpers


class XTm(Element):

    def __init__(self, size: int, jumpers: list = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = size
        for i in range(size):
            self.__dict__[f'k{i+1}'] = Connection(name=f'{self.name}-{i+1}', parent=self)
            self.__dict__[f'k{i + 1}_'] = Connection(name=f'{self.name}-{i + 1}_', parent=self)
        if not jumpers:
            self.jumpers = [False for _ in range(size)]
        else:
            self.jumpers = jumpers


class Ground(Apparatus):

    trans = (('g', ''),)