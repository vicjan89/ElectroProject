from dataclasses import dataclass


from classes import *
from textengines.interfaces import TextEngine


from views.VA4 import *
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
from views.frames import *
from elements.XT import *

class Vlist:

    def __init__(self,
                 project: Element,
                 te: TextEngine,
                 num: int | None = None,
                 docitems: list | None = None,
                 docwires: dict | None = None,
                 code_list: str = '',
                 cabinet_list: str = '',
                 name_list: str = '',
                 num_lists: int = 1,
                 cross: bool = False
                 ):
        self.code_list = code_list
        self.cabinet_list = cabinet_list
        self.name_list = name_list
        self.num_lists = num_lists
        self.num = num
        self.cross = cross
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
                   'VA4Seom': VA4Seom,
                   'VDiode_bridge': VDiode_bridge,
                   'VDiode': VDiode,
                   'VDiodeL': VDiodeL,
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
                   'TableApparatus': TableApparatus,
                   'Vcabinet': Vcabinet,
                   'VcabinetD': VcabinetD,
                   'Vlabel': Vlabel,
                   'Ruler': Ruler,
                   'Vexplanation': Vexplanation,
                   'Vframe_cross': Vframe_cross}

    def av(self, view: View | list):
        if isinstance(view, View):
            view.te = self.te
            self.docitems.append(view)
        elif isinstance(view, list):
            self.docitems.extend(view)
        else:
            assert False, 'Аргумент должен быть либо View либо list'

    def dv(self, view : View | list):
        if isinstance(view, View):
            self.docitems.remove(view)
        elif isinstance(view, list):
            for v in view:
                self.docitems.remove(v)
        else:
            assert False, 'Аргумент должен быть либо View либо list'

    def replace(self,num: int, new_class: View):
        '''
        Заменяет объект View номер num на другой класс new_class
        :param num: номер заменяемого объекта в списке docitems
        :param new_class: имя нового класса наследника View
        :return: объект нового класса
        '''
        self.docitems[num] = new_class(**self.docitems[num].__dict__)
        return self.docitems[num]

    def clear(self):
        self.docitems = []
        self.docwires = dict()

    def place(self, elements: list[Element]):
        '''
        Размещает на листе елементы из списка с использованием класса Vlbox_mount
        :param elements: список элементов для размещения
        :return:
        '''
        x = 30
        y = 250
        for element in elements:
            if isinstance(element, XT):
                obj = VXTmount(e=element,x=x, y=y)
            elif isinstance(element, XTm):
                obj = VXTmountM(e=element,x=x, y=y)
            else:
                obj = Vlbox_mount(e=element, x=x, y=y)
            h = y - obj.bottom
            y = obj.bottom
            if y < 10:
                x += 60
                y = 250
                obj.x = x
                obj.y = y
                y = y - h
            self.av(obj)
            print(f'Placed {element}')

    def place_cross(self, xts: list | tuple, beg: int = 1, end: int | None = None):
        '''
        Размещает на листе клеммы клеммников в списке args в виде схемы кроссовых шинок
        :param xts: объекты клеммников в нужном порядке
        :param beg: индекс первой клеммы
        :param end: индекс последней клеммы
        :return:
        '''
        x = 20
        dx = 25
        y = 250
        max_end = 0
        for xt in xts:
            end = end if end else xt.size
            if max_end < end:
                max_end = end
            for num in range(beg, end+1):
                self.av(VXT(e=xt.__dict__[f'k{num}'], x=x, y=y))
                y -= 10
            x += dx
            y = 250
        h = (max_end - beg + 3) * 10
        x = 20 - dx / 2
        for num, xt in enumerate(xts):
            self.av(Vframe_cross(x=x, y=265, w=dx, h=h, num=num+1, e=xt))
            x += dx
        self.cross = True


    def tw(self, wire_number: int | list | tuple, type_wire: int | None = None):
        if isinstance(wire_number, int):
            slug = self.project.wires.slug_wire(wire_number)
            if type_wire is None:
                print(f'{wire_number})\t{slug}\t{self.docwires[wire_number]}')
            else:
                self.docwires[wire_number] = type_wire
        else:
            for wire in wire_number:
                slug = self.project.wires.slug_wire(wire)
                if type_wire is None:
                    print(f'{wire})\t{slug}\t{self.docwires[wire]}')
                else:
                    self.docwires[wire] = type_wire

    def search_coords(self, c: Connection):
        '''
        Ищет координаты на листе для переданного объекта c типа Connection
        :param c:
        :return:
        '''
        for v in self.docitems:
            coord = v.get_coords(c)
            if coord:
                return coord
        return False

    def draw_wire(self, c0: Connection, c1: Connection, num: int | None = None, name: str = '', dev_mode = True):
        '''Рисует проводник. Тип линии запрашивает по номеру num в словаре типов линий листа.
        Если тип равен 10 то линия не рисуется
        :param num: номер типа линии'''
        res = False
        if num is None:
            tw = 0
        else:
            tw = self.docwires.get(num, 0)
        num_text = num if num and dev_mode else ''
        if tw != 10:
            coord0 = self.search_coords(c0)
            coord1 = self.search_coords(c1)
            if coord0 and coord1:
                dx = abs(coord0[0] - coord1[0])
                name = name if dx > 5 else ''
                self.te.wire(c1=coord0, c2=coord1, tw=tw, name=name, num=num_text)
                res = True
            elif not self.cross and ((coord0 and not coord1) or (not coord0 and coord1)):
                if coord0:
                    crd = coord0
                    c_for_srch = c0
                else:
                    crd = coord1
                    c_for_srch = c1
                x1, y1 = crd
                if dev_mode:
                    x2 = x1
                    y2 = y1 - 10
                    name = c0.slug if coord1 else c1.slug
                    self.te.wire(c1=(x1,y1), c2=(x2, y2), tw=tw, name=name, num=num_text, arrow=True)
                    res = True
                else:
                    connected = self.project.wires.get_all(c_for_srch)
                    for next_connected in connected:
                        if isinstance(next_connected.parent, XT):
                            crd2 = self.search_coords(next_connected)
                            if crd2:
                                x2, y2 = crd2
                                if x1 < 70:
                                    if x1 < x2:
                                        tw = 1
                                    else:
                                        tw = 2
                                else:
                                    if x1 > x2:
                                        tw = 1
                                    else:
                                        tw = 2
                                self.te.wire(c1=(x1, y1), c2=(x2, y2), tw=tw, name=name, num=num_text)
                                res = True
                                break
        return res

    def draw(self, dev_mode = True):
        self.te.picture_begin()
        if self.cabinet_list:
            self.te.latex(r'\AddToShipoutPicture*{\put(150mm,16mm){\parbox[c]{30mm}{\centering {\normalsize \begin{spacing}{0.7}' +
                          self.cabinet_list + r'\end{spacing}}}}}')
        if self.name_list:
            self.te.latex(r'\AddToShipoutPicture*{\put(148mm,5.5mm){\parbox[c]{35mm}{\centering {\scriptsize \begin{spacing}{0.6}' +
                          self.name_list + r'\end{spacing}}}}}')
        self.te.latex(
            r'\AddToShipoutPicture*{\put(174mm,11mm){\parbox[c]{35mm}{\centering {\scriptsize \begin{spacing}{0.6}' +
            str(self.num) + r'\end{spacing}}}}}')
        self.te.latex(
            r'\AddToShipoutPicture*{\put(188mm,11mm){\parbox[c]{35mm}{\centering {\scriptsize \begin{spacing}{0.6}' +
            str(self.num_lists) + r'\end{spacing}}}}}')
        names = set()
        for num, wire in enumerate(self.project.wires.wires):
            name = '' if wire[2] is None else wire[2]
            if name in names:
                name = ''
            drawed = self.draw_wire(wire[0], wire[1], num=num, name=name, dev_mode=dev_mode)
            if drawed:
                names.add(name)
        for item in self.docitems:
            if not isinstance(item, VXT) and not isinstance(item, VXTm):
                if not isinstance(item, Ruler) or dev_mode:
                    item.draw()
        # рисуем перемычки на клеммниках
        for name, element in self.project.__dict__.items():
            if isinstance(element, XT) or isinstance(element, XTm):
                for num, jum in enumerate(element.jumpers):
                    if jum:
                        self.draw_wire(element.__dict__[f'k{num}'], element.__dict__[f'k{num+1}'], dev_mode=dev_mode)
        for item in self.docitems:
            if isinstance(item, VXT) or isinstance(item, VXTm):
                item.draw()
        self.te.picture_end()

    def encode(self):
        res = {'num': self.num,
               'docitems': list(),
               'docwires': self.docwires,
               'code_list': self.code_list,
               'cabinet_list': self.cabinet_list,
               'name_list': self.name_list,
               'cross': self.cross
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

    @property
    def vl(self):
        return self.docitems[-1]

    def gef(self, f):
        '''Возвращает список графических элементов для которых функция f вернёт True'''
        res = []
        for item in self.docitems:
            if f(item):
                res.append(item)
        return res

    def gebox(self, x: int, y: int, w: int, h: int):
        def box(o):
            res_x = x <= o.x <= x + w
            res_y = y - h <= o.y <= y
            return res_x and res_y
        return self.gef(box)

    def f(self, s: str):
        '''Печатает список элементов содержащих в выводе __repr__ подстроку s'''
        res = ''
        for num, item in enumerate(self.docitems):
            view_name = f'{num})\t{item}\n'
            if s in view_name:
                res += view_name
        print(res)

    def fe(self, s: str):
        '''Возвращает список элементов содержащих в выводе __repr__ подстроку s'''
        res = []
        for num, item in enumerate(self.docitems):
            if s in repr(item):
                res.append(item)
        return res

    def __repr__(self):
        return f'{self.__class__.__name__}(num={self.num}, docitems={len(self.docitems)}, docwires={len(self.docwires)})'
