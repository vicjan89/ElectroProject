from textengines.interfaces import TextEngine

from classes import Element, Wires, Connection, View
from MR5PO50 import MR5PO50
from radio_component import *
from XT import XT
from SQ import *
from VA4 import VA4
from VXT import VXT


class Project(Element):
    classes = {'MR5PO50': MR5PO50,
               'Diode': Diode,
               'Diode_bridge': Diode_bridge,
               'XT': XT,
               'SQ_Seom': SQ_Seom,
               'Blocklock': Blocklock,
               'Wires': Wires,
               'VXT': VXT,
               'VA4': VA4}

    def __init__(self, te: TextEngine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__['te'] = te
        self.doc = []

    def __setattr__(self, name, value):
        if value and name not in ('name', 'storage', 'wires', 'cabinet') and not isinstance(value, (int, float, tuple, str, list, dict)):
            value.wires = self.wires
        self.__dict__[name] = value

    def av(self, view: View):
        view.te = self.te
        self.doc.append(view)

    def draw(self):
        for item in self.doc:
            item.draw()
        self.te.save()

    def encode(self):
        res = dict()
        for name, value in self.__dict__.items():
            if name not in ('name', 'storage', 'te', 'doc', 'cabinet', 'location'):
                res[name] = value.encode()
        res['doc'] = []
        for view in self.doc:
            res['doc'].append(view.encode())
        return res

    def decode(self, data: dict):
        wires = data.pop('wires')['wires']
        for key, value in data.items():
            if key == 'doc':
                for item in value:
                    name = item.pop('class')
                    self.doc.append(self.classes[name](te=self.te, **item))
            else:
                name_class = value.pop('class')
                obj = self.classes[name_class](**value)
                obj.wires = self.wires
                self.__dict__[key] = obj
                for c in obj.get_connections():
                    label = c.label
                    for i, wire in enumerate(wires):
                        if wire[0] == label and wire[2] == c.cabinet:
                            wires[i][0] = c
                        if wire[1] == label and wire[3] == c.cabinet:
                            wires[i][1] = c
        self.wires.wires = wires
