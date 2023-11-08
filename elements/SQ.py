from classes import Element, Connection
from classes import Apparatus


class SQZPUE(Apparatus):
    '''Класс для описания концевого выключателя положения тележки ячейки ZPUE'''
    trans = (('n', '11'),
             ('nc', '8'),
             ('no', '9'))
    name = '4K2'
    model = 'Концевой выключатель положения тележки ZPUE'

class SQGZPUE(Apparatus):
    '''Класс для описания концевого выключателя положения заземляющих ножей ячейки ZPUE'''
    trans = (('no', '1'),
             ('no_', '2'),
             ('nc', '3'),
             ('nc_', '4'))
    name = '89T'
    model = 'Концевой выключатель положения заземляющих ножей ячейки ZPUE'

class Contact(Element):
    '''Контакт реле, выключателя...'''

    def __init__(self, type: str, n1='a', n2='b', *args, **kwargs):
        assert type in ('no', 'nc'), 'contact must be no or nc'
        super().__init__(*args, **kwargs)
        self.a = Connection(parent=self, name=n1)
        self.b = Connection(parent=self, name=n2)
        self.type = type


class SQ_Seom(Element):
    '''Концевой выключатель'''

    def __init__(self, model: str = 'Концевой выключатель', *args, **kwargs):
        kwargs['model'] = model
        super().__init__(*args, **kwargs)
        kwargs['parent'] = self
        for i in range(1,13):
            kwargs['name'] = str(i)
            self.__dict__[f'k{i}'] = Connection(*args, **kwargs)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name == 'wires':
            for name, value_attr in self.__dict__.items():
                if isinstance(value_attr, (Connection)):
                    value_attr.wires = self.wires


class Blocklock(Element):
    '''Блок-замок электромагнитной блокировки'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.k1 = Connection(parent=self, name='1')
        self.k2 = Connection(parent=self, name='2')

