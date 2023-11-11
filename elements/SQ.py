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


class SQ_VP15(Apparatus):
    '''Концевой выключатель китайский'''

    trans = (('no1', '2'),
             ('no1_', '4'),
             ('nc1', '1'),
             ('nc1_', '3'))

    model = 'Концевой выключатель ВП15'

class SQ_Seom(Apparatus):
    '''Концевой выключатель китайский'''

    trans = (('no1', '1'),
             ('no1_', '2'),
             ('no2', '3'),
             ('no2_', '4'),
             ('no3', '5'),
             ('no3_', '6'),
             ('nc1', '7'),
             ('nc1_', '8'),
             ('nc2', '9'),
             ('nc2_', '10'),
             ('nc3', '11'),
             ('nc3_', '12'))

    model = 'Концевой выключатель'


class Blocklock(Apparatus):
    '''Блок-замок электромагнитной блокировки'''

    model = 'Электромагнитная блокировка ЗБ-1М'
    trans = (('k1','1'),
             ('k2','2'))

