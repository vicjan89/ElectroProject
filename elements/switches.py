from classes import Apparatus

transZBE101 = [['no', '3'],
         ['no_', '4']]

transZBE102 = [['nc', '1'],
          ['nc_', '2']]

class XB5AD21_ZBE101(Apparatus):
    '''Класс для описания переключателя с одим НО контактом (контакт нажимается в положении В)'''
    trans = transZBE101
    model = 'Переключатель XB5AD21 + ZBE 101'

class XB5AD21_ZBE101_ZBE102(Apparatus):
    '''Класс для описания переключателя с одим НО и одним НЗ контактом (контакты нажимается в положении В)'''
    trans = transZBE101 + transZBE102
    model = 'Переключатель XB5AD21 + ZBE 101 + ZBE 102'

class XB5AD21_2ZBE101_2ZBE102(Apparatus):
    '''Класс для описания переключателя с двумя пакетами по одному НО и одному НЗ контакту в каждом пакете
    (контакты нажимаются в положении В)'''

    trans = transZBE101 + transZBE102
    trans1 = [[c[0]+'1', c[1]+'`'] for c in trans]
    trans += trans1
    model = 'Переключатель XB5AD21 + 2xZBE 101 + 2xZBE 102'

class XB5AD21_3ZBE101_3ZBE102(Apparatus):
    '''Класс для описания переключателя с тремя пакетами по одному НО и одному НЗ контакту в каждом пакете
    (контакты нажимаются в положении В)'''

    trans = transZBE101 + transZBE102
    trans1 = [[c[0]+'1', c[1]+'`'] for c in trans]
    trans2 = [[c[0]+'2', c[1]+'``'] for c in trans]
    trans += trans1 + trans2
    model = 'Переключатель XB5AD21 + 3xZBE 101 + 3xZBE 102'

class XB5AA33(Apparatus):
    '''Класс для описания зелёной кнопки с двумя НО контактами'''

    model = 'Кнопка XB5 AA33 зелёная (ZB5 AZ101+ZB5AA3+ZBE 101)'
    trans = transZBE101
    trans1 = [[c[0] + '1', c[1] + '`'] for c in trans]
    trans += trans1


class XB5AA43(Apparatus):
    '''Класс для описания красной кнопки с двумя НО контактами'''

    model = 'Кнопка XB5 AA43 красная (ZB5 AZ101+ZB5AA4+ZBE 101)'
    trans = transZBE101
    trans1 = [[c[0] + '1', c[1] + '`'] for c in trans]
    trans += trans1

class SA(Apparatus):
    '''Класс для описания выключателя освещения ячейки'''

    model = 'Выключатель освещения'
    trans = [['no','1'],
             ['no_','2']]
