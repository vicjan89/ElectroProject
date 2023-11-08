from classes import Apparatus


class TGI(Apparatus):
    '''Класс для описания привода выключателя TGI ZPUE'''
    model = 'Коммутационный модуль TGI-24 ZPUE'
    trans = (('yac', 'A10 Вкл.'),
             ('yat', 'A7 Откл.'),
             ('ya', 'A16'),
             ('m', 'A1'),
             ('m_', 'A2'),
             ('nc1', 'A14'),
             ('nc1_', 'A15'),
             ('no1', 'C3'),
             ('no1_', 'C4'),
             ('nc2', 'C5'),
             ('nc2_', 'C6'),
             ('no2', 'C7'),
             ('no2_', 'C8'),
             ('nc3', 'A6'),
             ('nc3_', 'A13'),
             ('no3', 'A11'),
             ('no3_', 'A12'),
             ('n4f', 'A3'),
             ('no4f', 'A4 FC1'),
             ('nc4f', 'A5 FC1'),
             ('sqs_no', 'A8'),
             ('sqs_no_', 'A9'),
             ('sqs_nc', 'C1'),
             ('sqs_nc_', 'C2'))
