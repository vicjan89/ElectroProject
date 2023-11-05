from classes import Apparatus


class Terminal(Apparatus):
    '''Класс для описания микропроцессорного реле'''
    trans = (('Ia', 'Ia'),
             ('Ia5', 'Ia5'),
             ('Ia1', 'Ia1'),
             ('Ib', 'Ib'),
             ('Ib5', 'Ib5'),
             ('Ib1', 'Ib1'),
             ('Ic', 'Ic'),
             ('Ic5', 'Ic5'),
             ('Ic1', 'Ic1'),
             ('In', 'In'),
             ('In5', 'In5'),
             ('In1', 'In1'))


class MR5PO50(Terminal):
    '''Класс для описания микропроцессорного реле МР5ПО50'''
    trans = (('Ia', 'X8-1'),
             ('Ia5', 'X8-2'),
             ('Ia1', 'X8-3'),
             ('Ib', 'X8-4'),
             ('Ib5', 'X8-5'),
             ('Ib1', 'X8-6'),
             ('Ic', 'X8-7'),
             ('Ic5', 'X8-8'),
             ('Ic1', 'X8-9'),
             ('In', 'X8-10'),
             ('In5', 'X8-11'),
             ('In1', 'X8-12'))
