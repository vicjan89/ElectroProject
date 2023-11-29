from classes import Element, Connection, Apparatus

class XT(Element):
    '''
    Класс описывает клеммный ряд с перемычками
    в списке jumpers хранятся перемычки в виде значений bool.
    True для индекса i обозначает наличие перемычки между клеммами ki и ki+1
    '''
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

    def connected(self, c: Connection):
        '''
        Возвращает список объектов Connection имеющих элеткрическую связь с переданным в аргумента c
        :param c: объект Connection с которым ищем связь
        :return:
        '''
        res = []
        for i in range(self.size):
            if c == self.__dict__[f'k{i+1}']:
                index = i
                while (index < (self.size-1)) and self.jumpers[index+1]:
                    res.append(self.__dict__[f'k{index+2}'])
                    index += 1
                index = i
                while (index > 0) and self.jumpers[index]:
                    res.append(self.__dict__[f'k{index}'])
                    index -= 1
                break
        return res



    def swop(self, k1: int, k2: int):
        '''
        Меняет между собой две клеммы
        :param k1: номер первой клеммы
        :param k2: номер второй клеммы
        :return:
        '''
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