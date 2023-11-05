from dataclasses import dataclass


from classes import *
from textengines.interfaces import TextEngine


from views.VA4 import VA4
from views.VXT import VXT
from views.Vradio_component import *
from views.VSQ import VSQ
from views.Vrelay_component import Vrelay
from views.Vtratsformers import *
from views.Vbox import Vbox


@dataclass
class Vlist:
    num: str
    docitems = []
    docwires = dict()
    project: Element
    te: TextEngine
    classes = {'Wires': Wires,
               'VXT': VXT,
               'VA4': VA4,
               'VDiode_bridge': VDiode_bridge,
               'VSQ': VSQ,
               'Vrelay': Vrelay,
               'VCT': VCT,
               'Vbox': Vbox}

    def av(self, view: View, atr: str = None):
        view.te = self.te
        if atr:
            self.__dict__[atr] = view
        self.docitems.append(view)

    def tw(self, wire_number: int, type_wire: int):
        slug = self.project.wires.slug_wire(wire_number)
        self.docwires[slug] = type_wire

    def search_coords(self, c: Connection):
        for v in self.docitems:
            coord = v.get_coords(c)
            if coord:
                return coord
        return False

    def draw(self):
        self.te.picture_begin()
        for num, wire in enumerate(self.project.wires.wires):
            coord0 = self.search_coords(wire[0])
            coord1 = self.search_coords(wire[1])
            if coord0 and coord1:
                tw = self.docwires.get(self.project.wires.slug_wire(num), 0)
                self.te.wire(coord0, coord1, tw)
        for item in self.docitems:
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
                item['e'] = list(obj)[0]
            self.docitems.append(self.classes[name](te=self.te, **item))
        self.docwires = data.get('docwires', dict())

    @property
    def v(self):
        for num, item in enumerate(self.docitems):
            print(f'{num})\t{item}')

    @property
    def ve(self):
        return self.docitems


    def gef(self, f):
        for item in self.docitems:
            if f(item):
                yield item
