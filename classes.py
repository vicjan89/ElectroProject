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

    def save(self):
        self.storage.write(self.encode())

    def load(self):
        self.decode(self.storage.read())

    def encode(self, cls: str):
        res = {'class': cls}
        for key, value in self.__dict__.items():
            if isinstance(value, (int, float, str, dict)):
                res[key] = value
        return res

    def decode(self):
        ...

    def get_connections(self):
        for n, i in self.__dict__.items():
            if isinstance(i, Connection):
                yield i
            else:
                if isinstance(i, Element):
                    for j in i.get_connections():
                        yield j

    def ge(self):
        for i in self.gef(lambda x: True):
            yield i

    def gef(self, f):
        for n, i in self.__dict__.items():
            if isinstance(i, Element):
                if n not in ('parent', 'wires'):
                    if not f or f(i):
                        yield i
                    for j in i.gef(f):
                        yield j

    @property
    def slag(self):
        parent_name = getattr(self, 'parent', False)
        if parent_name:
            parent_name = parent_name.name
        res = tuple(filter(lambda x: x, (self.cabinet, self.location, parent_name, self.name)))
        return '/'.join(res)

class Connection(Element):
    
    def __init__(self, parent: Element, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.cabinet = parent.cabinet

    def c(self, to: Element):
        self.parent.wires.add(self, to)

    def connected(self):
        return self.parent.wires.get(self)

    @property
    def label(self):
        return f'{self.parent.name}:{self.name}'


class Wires(Element):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wires = []

    def __repr__(self):
        res = ''
        for wire in self.wires:
            res += f'{wire[0].label} / {wire[1].label}\n'
        return res

    def encode(self):
        res = {'class': 'Wires', 'wires': []}
        for c1, c2, *other in self.wires:
            res['wires'].append([c1.label, c2.label, c1.cabinet, c2.cabinet])
        return res

    def add(self, c1: Connection, c2: Connection):
       self.wires.append((c1, c2))

    def get(self, e: Element):
        connected = []
        for wire in self.wires:
            f = filter(lambda c: c == e, wire)
            if any(f):
                connected.append(wire[f.index(False)])
        return connected

# @dataclass
# class Cabinet:
#     name: str
#
#     def __setattr__(self, name, value):
#         if name not in ('name', 'storage', 'wires') and not isinstance(value, (int, float, tuple, str, list, dict)):
#             value.wires = self.wires
#         self.__dict__[name] = value



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
    e: Element | None = None
    x: int | None = None
    y: int | None = None
    te: TextEngine | None = None

