from dataclasses import dataclass


from classes import *
from textengines.interfaces import TextEngine


from views.VA4 import VA4
from views.VXT import *
from views.Vradio_component import *
from views.VSQ import VSQ
from views.Vrelay_component import *
from views.Vtratsformers import *
from views.Vbox import *
from views.Vmeasurements import *
from views.Vswitches import *
from views.VSF import *
from views.tables import *
from elements.XT import *

class Vlist:

    def __init__(self, num: str, project: Element, te: TextEngine, docitems: list | None = None, docwires: dict | None = None):
        self.num = num
        if docitems:
            self.docitems = docitems
        else:
            self.docitems = []
        if docwires:
            self.docwires = docwires
        else:
            self.docwires = dict()
        self.project = project
        self.te = te
        self.classes = {'Wires': Wires,
                   'VXT': VXT,
                   'VXTm': VXTm,
                   'VXTcross': VXTcross,
                   'VXTmount': VXTmount,
                   'VXTmountM': VXTmountM,
                   'Vlbox_mount': Vlbox_mount,
                   'VA4': VA4,
                   'VDiode_bridge': VDiode_bridge,
                   'VHL': VHL,
                   'VSQ': VSQ,
                   'Vrelay': Vrelay,
                   'VcontNo': VcontNo,
                   'VcontNc': VcontNc,
                   'VcontNoc': VcontNoc,
                   'VR': VR,
                   'VCT': VCT,
                   'Vbox': Vbox,
                   'Vlbox': Vlbox,
                   'VboxNo': VboxNo,
                   'VboxNc': VboxNc,
                   'VboxTxt': VboxTxt,
                   'VG': VG,
                   'VSACno': VSACno,
                   'VSACnc': VSACno,
                   'VSAC2': VSAC2,
                   'VSB': VSB,
                   'VPA': VPA,
                   'VSF': VSF,
                   'TableApparatus': TableApparatus}

    def av(self, view: View, atr: str = None):
        view.te = self.te
        if atr:
            self.__dict__[atr] = view
        self.docitems.append(view)

    def tw(self, wire_number: int | list | tuple, type_wire: int | None = None):
        if isinstance(wire_number, int):
            slug = self.project.wires.slug_wire(wire_number)
            if type_wire is None:
                print(f'{wire_number})\t{slug}\t{self.docwires[slug]}')
            else:
                self.docwires[slug] = type_wire
        else:
            for wire in wire_number:
                slug = self.project.wires.slug_wire(wire)
                if type_wire is None:
                    print(f'{wire})\t{slug}\t{self.docwires[slug]}')
                else:
                    self.docwires[slug] = type_wire

    def search_coords(self, c: Connection):
        for v in self.docitems:
            coord = v.get_coords(c)
            if coord:
                return coord
        return False

    def draw_wire(self, c0: Connection, c1: Connection, num: int | None = None, name: str = ''):
        '''Рисует проводник. Тип линии запрашивает по номеру num в словаре типов линий листа.
        Если тип равен 10 то линия не рисуется'''
        if num:
            tw = self.docwires.get(self.project.wires.slug_wire(num), 0)
        else:
            tw = 0
        if tw != 10:
            coord0 = self.search_coords(c0)
            coord1 = self.search_coords(c1)
            if coord0 and coord1:
                self.te.wire(coord0, coord1, tw, name=name)
            elif (coord0 and not coord1) or (not coord0 and coord1):
                if coord0 and not coord1:
                    x1,y1 = coord0
                else:
                    x1,y1 = coord1
                # if tw in (11, 21,15,25):
                #     x2 = x1
                # elif tw in (12,22,13,23,14,24):
                #     x2 = x1 +10
                # else:
                #     x2 = x1 - 10
                # if tw in (13, 23,17,27):
                #     y2 = y1
                # elif tw in (18,28,11,21,12,22):
                #     y2 = y1 +10
                # else:
                #     y2 = y1 - 10
                # arrow = (21 <= tw <= 28)
                # if tw in (11,21,13,23,15,25,17,27):
                #     tw = 0
                # else:
                #     tw = 2
                if abs(x1 - 20) < abs(x1-230):
                    x2 = 30
                else:
                    x2 = 175
                y2 = y1
                self.te.wire((x1,y1), (x2, y2), tw, name=name)

    def draw(self):
        self.te.picture_begin()
        for num, wire in enumerate(self.project.wires.wires):
            name = '' if wire[4] is None else wire[4]
            self.draw_wire(wire[0], wire[1], num=num, name=name)
        for item in self.docitems:
            if not isinstance(item, VXT) and not isinstance(item, VXTm):
                item.draw()
        # рисуем перемычки на клеммниках
        for name, element in self.project.__dict__.items():
            if isinstance(element, XT) or isinstance(element, XTm):
                for num, jum in enumerate(element.jumpers):
                    if jum:
                        self.draw_wire(element.__dict__[f'k{num}'], element.__dict__[f'k{num+1}'])
        for item in self.docitems:
            if isinstance(item, VXT) or isinstance(item, VXTm):
                item.draw()
        self.te.picture_end()

    def encode(self):
        res = {'num': self.num,
               'docitems': list(),
               'docwires': self.docwires
               }
        for view in self.docitems:
            res['docitems'].append(view.encode())
        return res

    def decode(self, data: dict):
        for item in data['docitems']:
            name = item.pop('class')
            slug = item.pop('e', False)
            if slug:
                obj = self.project.gef(lambda x: x.slug == slug)
                if obj:
                    item['e'] = list(obj)[0]
            if name == 'TableApparatus':
                item['e'] = self.project

            self.docitems.append(self.classes[name](te=self.te, **item))
        self.docwires = data.get('docwires', dict())

    @property
    def v(self):
        '''Печатает список графических элементов текущей страницы'''
        for num, item in enumerate(self.docitems):
            print(f'{num})\t{item}')

    @property
    def ve(self):
        return self.docitems


    def gef(self, f):
        '''Возарвщает список графических элементов для которых функция f вернёт True'''
        res = []
        for item in self.docitems:
            if f(item):
                res.append(item)
        return res

    def f(self, s: str):
        '''Печатает список элементов содержащих в выводе __repr__ подстроку s'''
        res = ''
        for num, item in enumerate(self.docitems):
            view_name = f'{num})\t{item}\n'
            if s in view_name:
                res += view_name
        print(res)

    def __repr__(self):
        return f'{self.__class__.__name__}(num={self.num}, docitems={len(self.docitems)}, docwires={len(self.docwires)})'
