'''Модуль прорисовки проектной документации.'''

import ezdxf
from src.GraphWithConnection import *

class CircuitDiagram:
    '''Вывод принципиальной схемы в формат DXF.'''

    def __init__(self, name_file: str, wires_list: list, elements_list, d):
        '''Вывод принципиальной схемы в формат DXF.

        :param name_file: имя файла
        :param wires_list: список проводников.
        '''

        doc = ezdxf.new()
        doc.units = ezdxf.units.MM
        msp = doc.modelspace()

        for i in elements_list:
            d[i[0]].connections[i[1]][1].mov_to(i[1], i[2], i[3])
            d[i[0]].connections[i[1]][1].show(msp)

        for w in wires_list:
            w.show(msp)

        doc.saveas(name_file + '.dxf', encoding='utf-8')





class WiringDiagram:
    '''Вывод монтажной схемы в формат DXF.'''
    def __init__(self, list_elements: list, wires: list, msp):
        for i in list_elements:
            i[0].mov_to(x=i[1][0], y=i[1][1])
            i[0].show(msp)
        coords = []
        for i in wires:
            coords += i.show_wd(msp, coords)


