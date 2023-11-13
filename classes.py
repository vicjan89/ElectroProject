from dataclasses import dataclass
import json
import tomllib


from yaml import load, FullLoader, dump
from textengines.interfaces import TextEngine


from interfaces import Storage


@dataclass
class Element:

    def __init__(self, name: str | None = None,
                 storage: Storage | None = None,
                 cabinet: str | None = None,
                 location: str | None = None,
                 model: str | None = None):
        if not hasattr(self, 'name'):
            self.name = name
        else:
            if name:
                self.name = name
        self.storage = storage
        self.cabinet = cabinet
        self.location = location
        if not hasattr(self, 'model'):
            self.model = model
        else:
            if model:
                self.model = model

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, model={self.model}, cabinet={self.cabinet}, ' \
               f'location={self.location})'

    @property
    def attr(self):
        return {'name': self.name,
                'cabinet': self.cabinet,
                'location': self.location}

    def save(self):
        self.storage.write(self.encode())

    def load(self):
        self.decode(self.storage.read())

    def encode(self):
        res = {'class': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if isinstance(value, (int, float, str, dict, tuple, list)):
                res[key] = value
        return res

    def decode(self):
        ...

    def get_connections(self):
        for n, i in self.__dict__.items():
            if isinstance(i, Connection):
                yield i, n
            else:
                if isinstance(i, Element):
                    for j in i.get_connections():
                        yield j

    def ge(self):
        return self.gef(lambda x: True)

    def print_elements(self, elements):
        c = 6
        for i in elements:
            if c:
                sep = '\t'
            else:
                sep = '\n'
                c = 7
            print(i.slug, end=sep)
            c -= 1

    @property
    def el(self):
        self.print_elements(self.gef(lambda e: not isinstance(e, Connection)))


    def gef(self, f):
        res = []
        for n, i in self.__dict__.items():
            if isinstance(i, Element):
                if n not in ('parent', 'wires'):
                    if not f or f(i):
                        res.append(i)
                    res_i = i.gef(f)
                    if res_i:
                        res += res_i
        return res

    def gefc(self, cabinet: str):
        '''
        Возвращает список элементов Element исключая Connections
        :param cabinet: название ячейки или шкафа
        :return:
        '''
        def filter_by_cabinet(o: Element):
            if isinstance(o, Element) and not isinstance(o, Connection):
                return o.cabinet == cabinet

        return self.gef(filter_by_cabinet)

    def fe(self, s: str):
        '''
        Возвращает список элементов в выводе __repr__ которых есть подстрока s
        :param s:
        :return:
        '''
        return self.gef(lambda o: not isinstance(o, Connection) and s in repr(o))

    @property
    def slug(self):
        parent_name = getattr(self, 'parent', False)
        if parent_name:
            parent_name = parent_name.name
        res = tuple(filter(lambda x: x, (self.cabinet, self.location, parent_name, self.name)))
        return '/'.join(res)

    @property
    def tr(self):
        '''Возвращает список названий атрибутов объекта Element'''
        return [c[0] for c in self.trans]

    @property
    def trp(self):
        for n, c in enumerate(self.trans):
            print(f'{n})\t{c[0]}')

    def connected(self, c):
        ...

class Connection(Element):
    
    def __init__(self, parent: Element, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.cabinet = parent.cabinet

    def __eq__(self, other):
        if isinstance(other, Connection):
            return self.slug == other.slug
        return False

    def c(self, to: Element, name: str = ''):
        self.parent.wires.add(self, to, name=name)

    def connected(self):
        return self.parent.wires.get(self)

    @property
    def label(self):
        return f'{self.parent.name}:{self.name}'

    def get_connections(self):
        yield self, ''


class Wires(Element):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wires = []

    def __repr__(self):
        res = ''
        for num, wire in enumerate(self.wires):
            res += f'{num})\t{self.slug_wire(num)}\t{self.wires[num][2]}\n'
        return res

    def without_name(self):
        '''
        Выводит на печать проводники без имени
        :return:
        '''
        for num, wire in enumerate(self.wires):
            if not wire[2]:
                print(f'{num})\t{self.slug_wire(num)}')

    def fill_wire_name(self):
        '''
        Заполняет словарь wires_names названиями цепей на основе анализа фактических соединений схемы
        :return:
        '''
        self.wires_names = dict()
        i = 0
        while i < len(self.wires):
            name = self.wires[i][2]
            if name and i not in self.wires_names:
                self.wires_names[i] = name
                connected = self.get_all(self.wires[i][0])
                for j, wire in enumerate(self.wires):
                    if wire[0] in connected or wire[1] in connected:
                        self.wires_names[j] = name
                        self.wires[j][2] = name
                i = 0
            else:
                i += 1


    def set_name(self, num, name):
        if len(self.wires[num]) == 4:
            self.wires[num].append(name)
        else:
            self.wires[num][4] = name

    def delete(self, num: int):
        '''
        Удаляет проводник из списка
        :param num: номер удаляемого проводника
        :return: список представляющий данные уддалённого проводника
        '''
        return self.wires.pop(num)

    def f(self, s: str):
        '''
        Поиск провода имеющего в label Connection переданную подстроку
        :param s: подстрока для поиска
        :return:  найденные провода в виде строки вывода
        '''
        res = ''
        for num, wire in enumerate(self.wires):
            wire_name = f'{num})\t{self.slug_wire(num)}\n'
            if s in wire_name:
                res += wire_name
        print(res)

    def ac(self, num: int, c: Connection):
        '''
        Разделяет проводник на два с включением посередине коннекшена с
        :param num: номер разделяемого проводника
        :param c: объект Connection вставляемый посередине
        :return: номера и слаги двух новых проводников
        '''
        c2 = self.wires[num][1]
        name = self.wires[num][2]
        self.wires[num][1] = c
        num_last = self.add(c, c2, name)
        print(f'{num}\t{self.slug_wire(num)}\n{num_last})\t{self.slug_wire(num_last)}')


    def encode(self):
        res = {'class': 'Wires', 'wires': []}
        for c1, c2, name in self.wires:
            res['wires'].append([c1.slug, c2.slug, name])
        return res

    def add(self, c1: Connection, c2: Connection, name: str = ''):
        self.wires.append([c1, c2, name])
        return len(self.wires)-1

    def get(self, e: Element):
        '''
        Возвращает список непосредственно подключенных объектов Connection к переданному атрибуту e
        :param e:
        :return:
        '''
        connected = []
        name = ''
        for wire in self.wires:
            f = [wire[0] == e, wire[1] == e]
            if any(f):
                connected.append(wire[f.index(False)])
                name = wire[2]
        return connected, name

    def get_all(self, c: Connection):
        res = [c]
        i = 0
        while i < len(res):
            add_res, _ = self.get(res[i])
            add_by_apparatus = res[i].parent.connected(res[i])
            if add_by_apparatus:
                add_res.extend(add_by_apparatus)
            for next_c in add_res:
                if next_c not in res:
                    res.append(next_c)
            i += 1
        res.remove(c)
        return res


    def slug_wire(self, num):
        wire = self.wires[num]
        return f'{wire[0].slug}~{wire[1].slug}'

class TextStorage(Storage):

    def read(self) -> str:
        with open(self.path, 'r', encoding='utf-8') as f:
            return f.readlines()

    def write(self, text: str):
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(text)

class JsonStorage(Storage):

    def read(self) -> dict:
        with open(self.path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def write(self):
        ...

class YamlStorage(Storage):

    def read(self) -> dict:
        with open(f'{self.path}.yaml', 'r', encoding='utf-8') as f:
            return load(f, Loader=FullLoader)

    def write(self, d: dict):
        with open(f'{self.path}.yaml', 'w', encoding='utf-8') as f:
            dump(d, f)

class TomlStorage(Storage):

    def read(self) -> dict:
        with open(self.path, 'rb') as f:
            return tomllib.load(f)

    def write(self, d: dict):
        ...

class View(Element):

    def __init__(self, c: tuple | list | None = None,
                 e: Element | None = None,
                 x: int | None = None,
                 y: int | None = None,
                 te: TextEngine | None = None,
                 correspondence: dict = None):
        self.e = e
        self.x = x if x else 0
        self.y = y if y else 0
        self.te = te
        self.correspondence = correspondence
        if c:
            self.c = c
        else:
            if self.e and not isinstance(self.e, Connection):
                self.c = self.e.tr
            else:
                self.c = None


    def __repr__(self):
        slug = self.e.slug if self.e else None
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, c={self.c}, e={slug})'

    def __eq__(self, other):
        return self is other

    def get_coords(self, c: Connection):
        if self.e:
            for con, name in self.e.get_connections():
                if c == con:
                    if self.correspondence:
                        coords = self.correspondence.get(name, False)
                        if coords:
                            x, y = coords
                            return x + self.x, y + self.y
                    else:
                        return self.x, self.y

    def xy(self, x, y):
        self.x = x
        self.y = y

    def r(self, d=10):
        self.x += d

    def l(self, d=10):
        self.x -= d

    def u(self, d=10):
        self.y += d

    def d(self, d=10):
        self.y -= d

    def encode(self):
        res = super().encode()
        if self.e:
            res.update({'e': self.e.slug})
        res.pop('correspondence', None)
        return res

class Apparatus(Element):
    '''Класс для описания всех аппаратов'''
    trans = tuple()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        kwargs['parent'] = self
        for con in self.trans:
            kwargs['name'] = con[1]
            self.__dict__[con[0]] = Connection(*args, **kwargs)
