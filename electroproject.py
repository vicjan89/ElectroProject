'''Модуль прорисовки проектной документации.'''

from GraphWithConnection import *

class CircuitDiagram:
    '''Вывод принципиальной схемы в формат DXF.'''
    def __init__(self, wires_list, msp):
        for i in wires_list:
            i.show(msp)
            print(i)

class WiringDiagram:
    '''Вывод монтажной схемы в формат DXF.'''
    def __init__(self, list_elements: list, wires: list, msp):
        x = 0
        y = 0
        for i in list_elements:
            i.mov_to(x=x, y=y)
            i.show(msp)
            x += 70
        coords = []
        for i in wires:
            coords += i.show_wd(msp, coords)


