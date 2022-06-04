'''Модуль прорисовки проектной документации.'''

from src.GraphWithConnection import *

class CircuitDiagram:
    '''Вывод принципиальной схемы в формат DXF.'''
    def __init__(self, wires_list, msp):
        for i in wires_list:
            i.show(msp)
            print(i)

class WiringDiagram:
    '''Вывод монтажной схемы в формат DXF.'''
    def __init__(self, list_elements: list, wires: list, msp):
        for i in list_elements:
            i[0].mov_to(x=i[1][0], y=i[1][1])
            i[0].show(msp)
        coords = []
        for i in wires:
            coords += i.show_wd(msp, coords)


