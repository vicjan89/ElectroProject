'''Модуль прорисовки проектной документации.'''
import random
import ezdxf
from src.GraphWithConnection import *

class CircuitDiagram:
    '''Вывод принципиальной схемы в формат DXF.'''

    def __init__(self, name_file: str, wires_list: list, d):
        '''Вывод принципиальной схемы в формат DXF.

        :param name_file: имя файла
        :param wires_list: список проводников.
        :param d: словарь с элементами схемы.
        '''

        self.name_file = name_file
        self.wires_list = wires_list
        self.dict_el = d

    def place_elements(self):
        doc = ezdxf.new()
        doc.units = ezdxf.units.MM
        msp = doc.modelspace()
        num = 0
        blocks_list = []
        nx = 0
        ny = 0
        elements = []
        for key, value in self.dict_el.items():
            for key_e, value_e in value.connections.items():
                if value_e[1] not in elements:
                    elements.append(value_e[1])
                    blocks_list.append(doc.blocks.new(name=str(num)))
                    value_e[1].show(blocks_list[-1])
                    x = nx * 30
                    y = ny * 30
                    msp.add_blockref(str(num),(x,y))
                    num += 1
                    if nx == 10:
                        nx = 0
                        ny +=1
                    else:
                        nx += 1

        # for w in wires_list:
        #     w.show(msp)

        doc.saveas(self.name_file + '.dxf', encoding='utf-8')





class WiringDiagram:
    '''Вывод монтажной схемы в формат DXF.'''
    def __init__(self, list_elements: list, wires: list, msp):
        for i in list_elements:
            i[0].mov_to(x=i[1][0], y=i[1][1])
            i[0].show(msp)
        coords = []
        for i in wires:
            coords += i.show_wd(msp, coords)


