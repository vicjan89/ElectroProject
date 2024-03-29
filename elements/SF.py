from classes import Apparatus


class SF2(Apparatus):
    '''Класс для описания двухполюсного автоматического выключателя'''
    model = 'Автоматический выключатель'
    trans = (('k1', '1'),
             ('k2', '2'),
             ('k3', '3'),
             ('k4', '4'))

class A9N26924(Apparatus):
    '''Класс для описания блокконтакта автоматического выключателя'''
    model = 'Блокконтакт к автоматическому выключателю A9N26924 Schneider Electric'
    trans = (('n', '11'),
             ('nc', '12'),
             ('no', '14'))
