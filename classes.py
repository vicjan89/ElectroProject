from dataclasses import dataclass
import json
import tomllib


from yaml import load, FullLoader, dump
from textengines.interfaces import TextEngine


from interfaces import Storage


@dataclass
class Element:
    name: str | None = None
    storage: Storage | None = None
    cabinet: str | None = None
    location: str | None = None
    model: str | None = None

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
    def e(self):
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
            res += f'{num})\t{wire[0].label}\t/\t{wire[1].label}\n'
        return res

    def set_name(self, num, name):
        if len(self.wires[num]) == 4:
            self.wires[num].append(name)
        else:
            self.wires[num][4] = name

    def f(self, s: str):
        '''
        Поиск провода имеющего в label Connection переданную подстроку
        :param s: подстрока для поиска
        :return:  найденные провода в виде строки вывода
        '''
        res = ''
        for num, wire in enumerate(self.wires):
            wire_name =  f'{num})\t{wire[0].label}\t/\t{wire[1].label}\n'
            if s in wire_name:
                res += wire_name
        print(res)


    def encode(self):
        res = {'class': 'Wires', 'wires': []}
        for c1, c2, _, _, name in self.wires:
            res['wires'].append([c1.label, c2.label, c1.cabinet, c2.cabinet, name]) #TODO: потом переделать на слаги
        return res

    def add(self, c1: Connection, c2: Connection, name: str = ''):
       self.wires.append([c1, c2, None, None, name])

    def get(self, e: Element):
        connected = []
        for wire in self.wires:
            f = filter(lambda c: c == e, wire)
            if any(f):
                connected.append(wire[f.index(False)])
        return connected

    def slug_wire(self, num):
        wire = self.wires[num]
        return f'{wire[0].slug}/{wire[1].slug}'

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

@dataclass
class View(Element):
    c: tuple | list | None = None
    e: Element | None = None
    x: int | None = None
    y: int | None = None
    te: TextEngine | None = None
    correspondence: dict = None

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, c={self.c}, e={self.e.slug})'

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
