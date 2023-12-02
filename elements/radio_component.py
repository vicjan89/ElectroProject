from classes import Element, Connection, Apparatus

class Diode(Apparatus):
    model = 'Диод'
    trans = (('anode', 'анод'),
             ('cathode', 'катод'))


class HL(Apparatus):
    '''Класс описания лампочки сигнальной'''
    model = 'Сигнальная лампа XB5 AVB5 жёлтая'
    trans = (('k1', '1'),
             ('k2', '2'))

class EL(Apparatus):
    '''Класс описания светильника освещения'''
    model = 'Светильник освещения'
    trans = (('k1', '1'),
             ('k2', '2'))

class XS(Apparatus):
    '''Класс описания розетки силовой'''
    model = 'Розетка силовая с заземлением'
    trans = (('k1', '1'),
             ('k2', '2'),
             ('ground', '3'))

class EK(Apparatus):
    '''Класс описания резистора для обогрева'''
    model = 'Резистор С5-35В-50Вт-1,5кОм'
    trans = (('k1', '1'),
             ('k2', '2'))

class HLR(HL):
    model = 'Сигнальная лампа XB5 AVB4 красная'

class HLG(HL):
    model = 'Сигнальная лампа XB5 AVB3 зелёная'


class Diode_bridge(Apparatus):
    model = 'Диодный мост'
    trans = (('plus','+'),
             ('minus','-'),
             ('in1', 'переменный1'),
             ('in2','переменный2'))

