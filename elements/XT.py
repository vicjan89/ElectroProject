from classes import Element, Connection, Apparatus

class XT(Element):
    trans = dict()

    def __init__(self, size: int, jumpers: list = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = size
        for i in range(size):
            self.__dict__[f'k{i+1}'] = Connection(name=f'{self.name}-{i+1}', parent=self)
        if not jumpers:
            self.jumpers = [False for _ in range(size)]
        else:
            self.jumpers = jumpers
        self.model = 'Клеммные ряды промежуточных клемм'

    def swop(self, k1: int, k2: int):
        temp_connection_k1 = self.__dict__[f'k{k1}']
        temp_connection_k2 = self.__dict__[f'k{k2}']
        temp_name_k1 = temp_connection_k1.name
        temp_name_k2 = temp_connection_k2.name
        self.__dict__[f'k{k1}'] = temp_connection_k2
        self.__dict__[f'k{k2}'] = temp_connection_k1
        self.__dict__[f'k{k1}'].name = temp_name_k1
        self.__dict__[f'k{k2}'].name = temp_name_k2

    def resize(self, new_size: int):
        if new_size > self.size:
            for i in range(self.size, new_size):
                self.__dict__[f'k{i + 1}'] = Connection(name=f'{self.name}-{i + 1}', parent=self)
                self.jumpers.append(False)
        elif new_size < self.size:
            for i in range(new_size, self.size):
                self.__dict__.pop(f'k{i+1}')
            self.jumpers = self.jumpers[:new_size]
        self.size = new_size


class XTm(Element):
    trans = dict()

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
        self.model = 'Клеммные ряды испытательных клемм'


class Ground(Apparatus):

    trans = (('g', ''),)