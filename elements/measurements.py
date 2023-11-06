from classes import Apparatus


class PIK(Apparatus):
    '''Класс для описания счётчика электроэнергии'''
    trans = (('ia', '1'),
             ('ia_', '3'),
             ('ib', '4'),
             ('ib_', '6'),
             ('ic', '7'),
             ('ic_', '9'),
             ('u0', '10'),
             ('ua', '2'),
             ('ub', '5'),
             ('uc', '8'))


class PA(Apparatus):
    '''Класс для описания амперметра'''
    trans = (('i', '1'),
             ('i_', '2'))


class SGm(Apparatus):
    '''Класс для описания коробки испытательной'''

    trans = (('iaOut', '7'),
             ('iaOut_', '7`'),
             ('iaIn', '6'),
             ('iaIn_', '6`'),
             ('ibOut', '5'),
             ('ibOut_', '5`'),
             ('ibIn', '4'),
             ('ibIn_', '4`'),
             ('icOut', '3'),
             ('icOut_', '3`'),
             ('icIn', '2'),
             ('icIn_', '2`'),
             ('i0In', '1'),
             ('i0In_', '1`'),
             ('u0In', '0'),
             ('u0Out', '0`'),
             ('uaIn', 'A'),
             ('uaOut', 'A`'),
             ('ubIn', 'B'),
             ('ubOut', 'B`'),
             ('ucIn', 'C'),
             ('ucOut', 'C`'))
