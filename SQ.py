from classes import Element, Connection



class Contact(Element):
    '''Контакт реле, выключателя...'''

    def __init__(self, type: str, n1='a', n2='b', *args, **kwargs):
        assert type in ('no', 'nc'), 'contact must be no or nc'
        super().__init__(*args, **kwargs)
        self.a = Connection(parent=self, name=n1)
        self.b = Connection(parent=self, name=n2)
        self.type = type

    def encode(self):
        return super().encode('Contact')

class SQ_Seom(Element):
    '''Концевой выключатель'''

    def __init__(self, model: str = 'Концевой выключатель', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.c1 = Contact(type='no', n1='1', n2='2', *args, **kwargs)
        self.c2 = Contact(type='no', n1='3', n2='4', *args, **kwargs)
        self.c3 = Contact(type='no', n1='5', n2='6', *args, **kwargs)
        self.c4 = Contact(type='nc', n1='7', n2='8', *args, **kwargs)
        self.c5 = Contact(type='nc', n1='9', n2='10', *args, **kwargs)
        self.c6 = Contact(type='nc', n1='11', n2='12', *args, **kwargs)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name == 'wires':
            for name, value_attr in self.__dict__.items():
                if value_attr and name != 'wires' and not isinstance(value_attr, (int, str, float)):
                    value_attr.wires = self.wires

    def encode(self):
        return super().encode('SQ_Seom')

class Blocklock(Element):
    '''Блок-замок электромагнитной блокировки'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.k1 = Connection(parent=self, name='1')
        self.k2 = Connection(parent=self, name='2')

    def encode(self):
        return super().encode('Blocklock')
