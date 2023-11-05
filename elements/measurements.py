from classes import Apparatus


class PIK(Apparatus):
    '''Класс для описания счётчика электроэнергии'''
    trans = (('ia', '1'),
             ('ua', '2'),
             ('ia_', '3'),
             ('ib', '4'),
             ('ub', '5'),
             ('ib_', '6'),
             ('ic', '7'),
             ('uc', '8'),
             ('ic_', '9'),
             ('u0', '10'))

class PA(Apparatus):
    '''Класс для описания амперметра'''
    trans = (('i', '1'),
             ('i_', '2'))


class SGm(Apparatus):
    '''Класс для описания счётчика электроэнергии'''
    trans = (('i0In', '1'),
             ('i0In_', '1'),
             ('icIn', '2'),
             ('icIn_', '2'),
             ('icOut', '3'),
             ('icOut_', '3'),
             ('ibIn', '4'),
             ('ibIn_', '4'),
             ('ibOut', '5'),
             ('ibOut_', '5'),
             ('iaIn', '6'),
             ('iaIn_', '6'),
             ('iaOut', '7'),
             ('iaOut_', '7'),
             ('uaIn', 'A'),
             ('uaOut', 'A'),
             ('ubIn', 'B'),
             ('ubOut', 'B'),
             ('ucIn', 'C'),
             ('ucOut', 'C'),
             ('u0In', '0'),
             ('u0Out', '0'))
