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
from elements.relay import *
from elements.SF import *
from elements.CB import *

version = 0.2

class Project(Element):
    '''Функционал управления созанием проекта'''
    classes = {'Terminal': Terminal,
               'XB5AD21_ZBE101': XB5AD21_ZBE101,
               'XB5AD21_ZBE101_ZBE102': XB5AD21_ZBE101_ZBE102,
               'XB5AD21_2ZBE101_2ZBE102': XB5AD21_2ZBE101_2ZBE102,
               'XB5AD21_3ZBE101_3ZBE102': XB5AD21_3ZBE101_3ZBE102,
               'XB5AA33': XB5AA33,
               'XB5AA43': XB5AA43,
               'KL': KL,
               'REU11_24V_DC': REU11_24V_DC,
               'REU11_50mA_DC': REU11_50mA_DC,
               'SF2': SF2,
               'A9N26924': A9N26924,
               'PS4': PS4,
               'MR5PO50': MR5PO50,
               'Diode': Diode,
               'Diode_bridge': Diode_bridge,
               'EL': EL,
               'XS': XS,
               'EK': EK,
               'SA': SA,
               'HL': HL,
               'HLG': HLG,
               'HLR': HLR,
               'XT': XT,
               'XTm': XTm,
               'Ground': Ground,
               'SQ_Seom': SQ_Seom,
               'SQ_VP15': SQ_VP15,
               'Blocklock': Blocklock,
               'Wires': Wires,
               'CT3': CT3,
               'PIK': PIK,
               'PA': PA,
               'SGm': SGm,
               'CT1': CT1,
               'SQGZPUE': SQGZPUE,
               'TGI': TGI}
    trans = dict()

    def __init__(self, te: TextEngine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__['te'] = te
        self.doc = []
        self.wires = Wires()

    def __setattr__(self, name, value):
        if value and name not in ('name', 'storage', 'wires', 'cabinet') and not isinstance(value, (int, float, tuple, str, list, dict)):
            value.wires = self.wires
        self.__dict__[name] = value
        globals()[name] = value

    def replace(self, name_attr: str, new_class: Element):
        temp = self.__dict__[name_attr]
        new_obj = new_class(**temp.attr)
        for key, value in temp.__dict__.items():
            if isinstance(value, Connection) and hasattr(new_obj, key):
                value.name = new_obj.__dict__[key].name
                value.model = new_obj.__dict__[key].model
                new_obj.__dict__[key] = value
        self.__dict__[name_attr] = new_obj


    def al(self, num: str = '',
        code_list: str = '',
        cabinet_list: str = '',
        name_list: str = '',
        num_lists: int = 1):
        '''
        Добавление листа в документ
        :param num: номер добавляемого листа
        :param code_list: код листа согласно проекта
        :param cabinet_list: наименование ячейки, шкафа, оборудования
        :param name_list: название вида схемы
        :return: объект Vlist
        '''
        if not num:
            num = len(self.doc) + 1
        self.doc.append(Vlist(num=num, project=self, te=self.te, code_list=code_list, cabinet_list=cabinet_list,
                              name_list=name_list, num_lists = num_lists))
        name = f'l{len(self.doc)}'
        self.__dict__[name] = self.doc[-1]
        globals()[name] = self.doc[-1]
        return self.doc[-1]



    def draw(self, dev_mode = True):
        self.te.clear()
        first = True
        for l in self.doc:
            if first:
                first = False
            else:
                self.te.newpage()
            l.draw(dev_mode)
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
        res['version'] = version
        return res

    def decode(self, data: dict):
        wires = data.pop('wires')['wires']
        self.docwires = data.pop('docwires', dict()) #TODO: возможно нужно удалить за ненадобностью
        for key, value in data.items():
            if key not in ('doc', 'version'):
                name_class = value.pop('class')
                obj = self.classes[name_class](**value)
                obj.wires = self.wires
                self.__dict__[key] = obj
                for c, _ in obj.get_connections():
                    # label = c.label
                    # for i, wire in enumerate(wires):
                    #     if wire[0] == label and wire[2] == c.cabinet:
                    #         wires[i][0] = c
                    #     if wire[1] == label and wire[3] == c.cabinet:
                    #         wires[i][1] = c
                    for i, wire in enumerate(wires):
                        if wire[0] == c.slug:
                            wires[i][0] = c
                        if wire[1] == c.slug:
                            wires[i][1] = c
        self.wires.wires = wires
        for l in data['doc']:
            if l:
                l['num_lists'] = len(data['doc'])
                data_decode = {'docitems': l.pop('docitems'),
                        'docwires': l.pop('docwires', dict())}
                lst = self.al(**l)
                lst.decode(data_decode)

    def dw(self, num: int):
        deleted = self.wires.delete(num)
        for l in self.doc:
            l.docwires.pop(num, False)
            new_dict = dict()
            indexes_for_delete = []
            for key, value in l.docwires.items():
                if key > num:
                    new_dict[key-1] = value
                    indexes_for_delete.append(key)
            for key in indexes_for_delete:
                l.docwires.pop(key)
            l.docwires.update(new_dict)
        print(deleted)

    def mv(self, view: View | list, l_from: Vlist, l_to: Vlist):
        l_to.av(view)
        l_from.dv(view)
    def convert(self):
        for l in self.doc:
            new_docwires = dict()
            for key in l.docwires:
                value = l.docwires.get(key)
                for num in range(len(self.wires.wires)):
                    sl = self.wires.slug_wire(num)
                    if key == sl:
                        new_docwires[num] = value
            l.docwires = new_docwires
        for num in range(len(self.wires.wires)):
            self.wires.wires[num].pop(2)
            self.wires.wires[num].pop(2)
