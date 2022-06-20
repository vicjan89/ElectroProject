'''Модуль прорисовки проектной документации.'''
import random
import ezdxf
import json
from src.GraphWithConnection import *
from ezdxf.tools.standards import linetypes

class Wires:
    '''Класс для управления коллекциями соединителей Wire'''
    def __init__(self, name_file, dict_elements):
        self.__wires = []
        self.__name_file = name_file
        self.__dict_elements = dict_elements

    def add(self,w):
        self.__wires = w

    @property
    def get(self):
        return self.__wires

    def save_json(self):
        with open(self.__name_file + ".json", "w") as write_file:
            json.dump(self.__wires, write_file, default=Wire.encoder, indent=4)

    def load_json(self):
        with open(self.__name_file + ".json", "r") as read_file:
            wires_list = json.load(read_file)
            for i in wires_list:
                i['a'] = self.__dict_elements[i['a']]
                i['b'] = self.__dict_elements[i['b']]
                self.__wires.append(Wire(**i))

class CircuitDiagram:
    '''Вывод принципиальной схемы в формат DXF.'''

    def __init__(self, name_file: str, wires: Wires, d):
        '''Вывод принципиальной схемы в формат DXF.

        :param name_file: имя файла
        :param wires: объект хранения проводников.
        :param d: словарь с элементами схемы.
        '''

        self.name_file = name_file
        self.wires_list = wires.get
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

    def save_json(self):
        out = {}
        out['elements'] = self.dict_el
        out['wires'] = self.wires_list
        print(pickle.dumps(out))

class WiringDiagram:
    '''Вывод монтажной схемы в формат DXF.'''
    def __init__(self, list_elements: list, wires: list, msp):
        for i in list_elements:
            i[0].mov_to(x=i[1][0], y=i[1][1])
            i[0].show(msp)
        coords = []
        for i in wires:
            coords += i.show_wd(msp, coords)



