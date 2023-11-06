import os


from textengines.interfaces import TextEngine


from classes import *
from Vlist import *
from elements.Terminal import *
from elements.radio_component import *
from elements.XT import *
from elements.SQ import *
from elements.CT import *
from elements.measurements import *
from elements.switches import *

class Project(Element):
    '''Функционал управления созанием проекта'''
    classes = {'Terminal': Terminal,
               'XB5AD21_ZBE102': XB5AD21_ZBE102,
               'PS4': PS4,
               'MR5PO50': MR5PO50,
               'Diode': Diode,
               'Diode_bridge': Diode_bridge,
               'XT': XT,
               'XTm': XTm,
               'Ground': Ground,
               'SQ_Seom': SQ_Seom,
               'Blocklock': Blocklock,
               'Wires': Wires,
               'CT3': CT3,
               'PIK': PIK,
               'PA': PA,
               'SGm': SGm,
               'CT1': CT1}
    def __init__(self, te: TextEngine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__['te'] = te
        self.doc = []
        self.wires = Wires()

    def __setattr__(self, name, value):
        if value and name not in ('name', 'storage', 'wires', 'cabinet') and not isinstance(value, (int, float, tuple, str, list, dict)):
            value.wires = self.wires
        self.__dict__[name] = value


    def al(self, num: str = ''):
        if not num:
            num = len(self.doc) + 1
        self.doc.append(Vlist(num=num, project=self, te=self.te))
        self.__dict__[f'l{len(self.doc)}'] = self.doc[-1]
        return self.doc[-1]



    def draw(self):
        self.te.clear()
        first = True
        for l in self.doc:
            if first:
                first = False
            else:
                self.te.newpage()
            l.draw()
        self.te.save()
        os.system(f'pdflatex "{self.te.path}"')
            # print('Документ сформирован')

    def encode(self):
        res = dict()
        for name, value in self.__dict__.items():
            if isinstance(value, Element):
                res[name] = value.encode()
        res['doc'] = []
        for l in self.doc:
            res['doc'].append(l.encode())
        return res

    def decode(self, data: dict):
        wires = data.pop('wires')['wires']
        self.docwires = data.pop('docwires', dict())
        for key, value in data.items():
            if key != 'doc':
                name_class = value.pop('class')
                obj = self.classes[name_class](**value)
                obj.wires = self.wires
                self.__dict__[key] = obj
                for c, _ in obj.get_connections():
                    label = c.label
                    for i, wire in enumerate(wires):
                        if wire[0] == label and wire[2] == c.cabinet:
                            wires[i][0] = c
                        if wire[1] == label and wire[3] == c.cabinet:
                            wires[i][1] = c
        self.wires.wires = wires
        for l in data['doc']:
            if l:
                lst = self.al(l['num'])
                lst.decode(l)

