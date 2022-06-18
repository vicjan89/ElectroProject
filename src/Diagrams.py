'''Модуль прорисовки проектной документации.'''
import random
import ezdxf
from src.GraphWithConnection import *
from ezdxf.tools.standards import linetypes

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
        nx = 0
        ny = 0
        elements = []
        for key, value in self.dict_el.items():
            for key_e, value_e in value.connections.items():
                if value_e[1] not in elements:
                    x = nx * 30
                    y = ny * 30
                    value_e[1].mov(x,y)
                    elements.append(value_e[1])
                    nm = key + '#' + str(key_e)
                    nm = nm.replace(':','@')
                    blk = doc.blocks.new(name=nm)
                    value_e[1].show(blk)
                    msp.add_blockref(nm,(x,y))
                    if nx == 10:
                        nx = 0
                        ny +=1
                    else:
                        nx += 1

        doc.saveas(self.name_file + '.dxf', encoding='utf-8')


    def update_coord_from_dxf(self,name_file):
        doc = ezdxf.readfile(name_file)
        msp = doc.modelspace()
        for e in msp:
            if e.dxftype() == "INSERT":
                key = e.get_dxf_attrib('name').replace('@', ':')
                key,key_e = key.split('#')
                if key_e.isdigit():
                    key_e = int(key_e)
                x = e.get_dxf_attrib('insert').x
                y = e.get_dxf_attrib('insert').y
                self.dict_el[key].connections[key_e][1].mov(dx=x,dy=y)
                self.dict_el[key].connections[key_e][1].visible = True
            if e.dxftype() == 'LWPOLYLINE':
                msp.delete_entity(e)
        for w in self.wires_list:
            w.show(msp)
        doc.saveas(self.name_file + '.dxf', encoding='utf-8')

    def update_elements(self):
        doc = ezdxf.readfile(self.name_file+'.dxf')
        # doc.layers.remove('dotted')
        my_line_types = [
            (
                "DASHED",
                "Dashed . . . . . . . .",
                [5, 3, -2],
            )]
        for name, desc, pattern in my_line_types:
            if name not in doc.linetypes:
                doc.linetypes.add(
                    name=name,
                    pattern=pattern,
                    description=desc,
                )
        msp = doc.modelspace()
        for e in msp:
            if e.dxftype() == "INSERT":
                key = e.get_dxf_attrib('name').replace('@', ':')
                key,key_e = key.split('#')
                if key_e.isdigit():
                    key_e = int(key_e)
                x = e.get_dxf_attrib('insert').x
                y = e.get_dxf_attrib('insert').y
                self.dict_el[key].connections[key_e][1].mov(dx=x,dy=y)
                self.dict_el[key].connections[key_e][1].visible = True
            if e.dxftype() == 'LWPOLYLINE':
                msp.delete_entity(e)
        blocks_names = []
        for block in doc.blocks.block_records:
            blocks_names.append(block.get_dxf_attrib(key='name'))
        for name in blocks_names:
            if name != "*Model_Space" and name != '*Paper_Space':
                key = name.replace('@', ':')
                key, key_e = key.split('#')
                if key_e.isdigit():
                    key_e = int(key_e)
                doc.blocks.delete_block(name=name, safe=False)
                blk = doc.blocks.new(name=name)
                self.dict_el[key].connections[key_e][1].show(blk)
        for w in self.wires_list:
            w.show(msp)
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


