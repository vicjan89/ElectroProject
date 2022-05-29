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
    def __init__(self, list_elements: list, wires: dict):
        self.__list_circuits = list_elements
        self.__wires = wires.values()

    def show(self, ax):
        x = 0
        y = 0
        self.__list_circuits[0].mov_to(x=x, y=y)
        for i in self.__list_circuits:
            i.mov_to(x=x, y=y)
            i.show(ax)
            x += 70
        coords = []
        for i in self.__wires:
            coords += i.show_wd(ax, coords)


