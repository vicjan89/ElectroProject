import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import math

#Базовый класс

class ElementCircuit:
    LEFT = True
    RIGHT = False

    def __init__(self, name=''):
        self.name = name
        self.__visible = False

    def show(self):
        self.__visible = True

    @property
    def visible(self):
        return self.__visible

#Базовый класс для графических элементов

class ElementGraph(ElementCircuit):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = []
        self.codes = []
        self.centers = []
        self.radii = []
        self.labels_xy = []
        self.labels = []

    def mov_to(self, dx, dy):
        for i in self.vertices:
            i[0] += dx
            i[1] += dy
        for i in self.centers:
            i[0] += dx
            i[1] += dy
        for i in self.labels_xy:
            i[0] += dx
            i[1] += dy

    def rotate(self, angle):
        for i in self.vertices:
            i[0] = math.cos(math.radians(angle)) * i[0] - math.sin(math.radians(angle)) * i[1]
            i[1] = math.sin(math.radians(angle)) * i[0] - math.cos(math.radians(angle)) * i[1]
        for i in self.centers:
            i[0] = math.cos(math.radians(angle)) * i[0] - math.sin(math.radians(angle)) * i[1]
            i[1] = math.sin(math.radians(angle)) * i[0] - math.cos(math.radians(angle)) * i[1]
        for i in self.labels_xy:
            i[0] = math.cos(math.radians(angle)) * i[0] - math.sin(math.radians(angle)) * i[1]
            i[1] = math.sin(math.radians(angle)) * i[0] - math.cos(math.radians(angle)) * i[1]

    def __add__(self, other):
        self.vertices += other.vertices
        self.codes += other.codes
        self.centers += other.centers
        self.radii += other.radii
        self.labels_xy += other.labels_xy
        self.labels += other.labels
        return self

    def show(self, ax):
        super().show()
        if len(self.vertices) > 0:
            path = Path(self.vertices, self.codes)
            path_patch = PathPatch(path, fill=False)
            ax.add_patch(path_patch)
        for i in range(len(self.centers)):
            crl = plt.Circle(self.centers[i], self.radii[i], fill=False)
            ax.add_patch(crl)
        for i in range(len(self.labels_xy)):
            ax.text(self.labels_xy[i][0] - 10, self.labels_xy[i][1] - 5, self.labels[i], color='black', fontsize=12)

#Графические элементы

class ContactOpen(ElementGraph):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [[0, 0],   [5, 0],      [5, 5],      [15, 0],     [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[5, 6]]
        self.labels = [name]

class ContactClose(ElementGraph):

    def __init__(self, name='', label_a='', label_b=''):
        super().__init__(name)
        self.vertices = [(0, 0),   (5, 0),      (5, -5),     (4, -5),     (15, 0),     (20, 0)]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[5, 6]]
        self.labels = [name]

class ContactOpenTimeOn(ContactOpen):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices += [[9, 3],   [9, 8],     [11,2],      [11, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 6],     [7, 7],    [8, 7.7],    [9, 8],      [11, 8],     [12, 7.7],    [13, 7],   [14, 6]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[5, 10]]

class ContactOpenTimeOff(ContactOpen):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices += [[9, 3],   [9, 8],     [11,2],      [11, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 10],  [7, 9],     [8, 8.3],     [9, 8],      [11, 8],     [12, 8.3],    [13, 9],   [14, 10]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[5, 11]]

class ContactCloseTimeOn(ContactClose):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices += [[9, -3],   [9, 7],     [11,-2],      [11, 7]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 5],     [7, 6],    [8, 6.7],    [9, 7],     [11, 7],     [12, 6.7],    [13, 6],    [14, 5]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[5, 9]]

class ContactCloseTimeOff(ContactClose):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices += [[9, -3],   [9, 6],     [11,-2],      [11, 6]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 8],  [7, 7],    [8, 6.3],    [9, 6],    [11, 6],   [12, 6.3],    [13, 7],   [14, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[5, 9]]

class Winding(ElementGraph):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [[0, 0],   [5, 0],      [5, 5],      [10, 5],     [10, -5],    [5, -5],     [5, 0],      [10, 0],     [15, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.labels_xy = [[4, 7]]
        self.labels = [name]

class CT_W(ElementGraph):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [[0, 0],   [0, 3.5],      [4, 3.5],     [4, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.centers = [[2, 7]]
        self.radii = [4]
        self.labels_xy = [[0, 16]]
        self.labels = [name]

class ConnectionDetachable(ElementGraph):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [[5, 5], [0, 0], [5, -5], [7, 5], [2, 0], [7, -5]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[4, 10]]
        self.labels = [name]

#Базовый класс для графичиеских объектов с соединителями

class GraphWithConnection(ElementGraph):

    def __init__(self, name=''):
        super().__init__(name)
        self.connections = {}

    def mov_to(self, base_point_key=None, x=0, y=0):
        if base_point_key == None:
            base_point_key = list(self.connections.keys())[0]
        dx = x - self.connections[base_point_key][0]
        dy = y - self.connections[base_point_key][1]
        super().mov_to(dx, dy)
        for i in self.connections.values():
            i[0] += dx
            i[1] += dy

    def rotate(self, angle):
        super().rotate(angle)
        for i in self.connections.values():
            i[0] = math.cos(math.radians(angle)) * i[0] - math.sin(math.radians(angle)) * i[1]
            i[1] = math.sin(math.radians(angle)) * i[0] - math.cos(math.radians(angle)) * i[1]

#Умный соединитель

class Wire(ElementCircuit):
    '''Умный соединитель'''
    def __init__(self, a, key_a, b, key_b, name='', cable=None):
        super().__init__(name)
        self.__a = a
        self.__key_a = key_a
        self.__b = b
        self.__key_b = key_b
        if cable != None:
            cable.add(self)

    def show(self, ax):
        if self.__b.visible:
            p = [(self.__a.x, self.__a.y)]
            dx1 = -5 if self.__a.side else 5
            dy1 = -5 if self.__a.y > self.__b.y else 5
            dx2 = -5 if self.__b.side else 5
            dy2 = 5 if self.__a.y > self.__b.y else -5
            p.append((self.__a.x + dx1, self.__a.y + dy1))
            p.append((self.__a.x + dx1, (self.__a.y + dx2 + self.__b.y + dy2)/2 + self.__a.y))
            p.append((self.__b.x + dx2, (self.__a.y + dx2 + self.__b.y + dy2) / 2 + self.__a.y))
            p.append((self.__b.x + dx2, self.__b.y + dy2))
            p.append((self.__b.x, self.__b.y))
            path = Path(p, [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO])
            path_patch = PathPatch(path, fill=False)
            ax.add_patch(path_patch)
            plt.text(self.__a.x + dx1, (self.__a.y + dx2 + self.__b.y + dy2) / 2 + self.__a.y + 2, self.name,
                     color='black', fontsize=12)
        else:
            path = Path((self.__a.connections[self.__key_a][1].connections[self.__key_a],
                        (self.__a.connections[self.__key_a][1].connections[self.__key_a][0] + 20,
                         self.__a.connections[self.__key_a][1].connections[self.__key_a][1])), [Path.MOVETO, Path.LINETO])
            path_patch = PathPatch(path, fill=False)
            ax.add_patch(path_patch)
            plt.text(self.__a.connections[self.__key_a][1].connections[self.__key_a][0] + 5,
                         self.__a.connections[self.__key_a][1].connections[self.__key_a][1] + 5,
                     self.name, color='black', fontsize=12)
            self.__b.connections[self.__key_b][1].mov_to(base_point_key=self.__key_b,
                                                        x=self.__a.connections[self.__key_a][1].connections[self.__key_a][0] + 20,
                                                        y=self.__a.connections[self.__key_a][1].connections[self.__key_a][1])

#Составные элементы схемы

class ConnectionTerminal(GraphWithConnection):

    def __init__(self, name=''):
        super().__init__(name)
        self.centers = [[0, 0]]
        self.radii = [0.5]
        self.labels_xy = [[7, -5]]
        self.labels = [name]
        self.connections[name] = [0, 0]

class Connector(GraphWithConnection):

    def __init__(self, name=''):
        super().__init__(name)
        self += ConnectionDetachable()
        self.connections['s' + str(name)] = [0, 0]
        self.connections['p' + str(name)] = [2, 0]

class Connectors(GraphWithConnection):

    def __init__(self, name='', quantity=32):
        super().__init__(name='')
        self.n = [None]
        for i in range(1, quantity+1):
            self.n.append(Connector(i))
            self.connections['s' + str(i)] = [[0, 0], self.n[-1]]
            self.connections['p' + str(i)] = [[2, 0], self.n[-1]]

class CT2(GraphWithConnection):

    def __init__(self, name=''):
        super().__init__(name)
        self.w1 = GraphWithConnection(name + '-1')
        self.w1 += CT_W(self.w1.name)
        self.w1.connections['1И1'] = [0, 0]
        self.w1.connections['1И2'] = [4, 0]
        self.w2 = GraphWithConnection(name + '-2')
        self.w2 += CT_W(self.w2.name)
        self.w2.connections['2И1'] = [0, 0]
        self.w2.connections['2И2'] = [4, 0]
        self.vertices = [[0, 0], [20, 0], [20, -50], [0, -50]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[0, 5]]
        self.labels = [[name]]
        self.connections['1И1'] = [[0, -10], self.w1]
        self.connections['1И2'] = [[20, -10], self.w1]
        self.connections['2И1'] = [[0, -40], self.w2]
        self.connections['2И2'] = [[20, -40], self.w2]

class YA(GraphWithConnection):

    def __init__(self, name=''):
        super().__init__(name)
        self.w = GraphWithConnection(name)
        self.w += Winding(name)
        self.w.connections[1] = [0, 0]
        self.w.connections[2] = [15, 0]
        self.connections[1] = [[0, 0], self.w]
        self.connections[2] = [[15, 0], self.w]

# class RP23_25(ElementCircuit):
#
#     def __init__(self, name=''):
#         super().__init__(name)
#         self.__w = Winding(name)
#         self.__k1 = ContactClose(name, '1', '2')
#         self.__k2 = ContactOpen(name, '3', '4')
#         self.__k3 = ContactOpen(name, '5', '6')
#         self.__k4 = ContactOpen(name, '7', '8')
#         self.__k5 = ContactOpen(name, '9', '10')
#         self.vertices = [(0, 0),   (30, 0),      (30, -60),     (0, -60),     (0, 0)]
#         self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]

class XT(GraphWithConnection):

    def __init__(self, name='', quantity=50):
        super().__init__(name)
        self.n = []
        for i in range(quantity):
            self.n.append(ConnectionTerminal(i))
            self.connections[i] = [[0, 0], self.n[-1]]

class RP361(ElementCircuit):

    def __init__(self, name=''):
        super().__init__(name)
        self.__k1 = ContactOpen(name)
        self.__k2 =ContactClose(name)
        self.w8_14 = Winding(name)

class CircuitDiagram:

    def __init__(self, *args):
        self.__list_circuits = []
        for i in args:
            self.__list_circuits.append(i)

    def show(self, ax):
        self.__list_circuits[0].mov_to(x=20, y=200)
        for i in self.__list_circuits:
            i.show(ax)

class WiringDiagram:

    def __init__(self, *args):
        pass

    def show(self, ax):
        pass

fig = plt.figure()
ax = fig.add_subplot()
ax.set(xlim=(0, 250), ylim=(0, 250))
ct_a = CT2('ТТа')
xt = XT('XT1', 50)
w411 = Wire(ct_a, '1И2', xt, 6,  'A411')
xt1 = Connectors('XT1', 32)
w412 = Wire(xt, 6, xt1, 's12', '')
yat_a = YA('YAA1')
w413 = Wire(xt1, 'p12', yat_a, 1)
xt1.n[13].rotate(180)
w414 = Wire(yat_a, 2, xt1, 'p13')
w415 = Wire(xt1, 's13', xt, 7)
#kl1 = RP361('KL1')
#w416 = Wire(xt.n[7].b, kl1.k1.a)

'''
yat_c = YA('YAC1')
kl1 = RP361('KL1')
kl2 = RP361('KL2')
a1 = MR5PO50('A1')
w7 = Wire(kl1.k1.b, kl1.w.a, '7')
rel_otc = MountingModule('Релейный отсек')
sh8.add(yat_a, yat_c, kl1, kl2, a1)
'''
cd = CircuitDiagram(ct_a.w1, w411, xt.n[6], w412, xt1.n[12], w413, yat_a.w, w414, xt1.n[13], w415, xt.n[7])
cd.show(ax)

wd = WiringDiagram(ct_a)
wd.show(ax)

#cm = CableMagazine()
#cm.add(cab101, cab102, cab103)
#cm.show(ax)

#ci = CableInstallation()
#ci.add(cab101, cab102, cab103)
#ci.show(ax)
plt.show()