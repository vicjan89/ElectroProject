import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

class ElementCircuit:

    def __init__(self, name=''):
        self.name = name
        self.__visible = False

    def show(self):
        self.__visible = True

    @property
    def visible(self):
        return self.__visible

class Connection(ElementCircuit):

    def __init__(self, name='', x=0, y=0, side=True):
        super().__init__(name)
        self.__x = x
        self.__y = y
        self.__side = side

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def side(self):
        return self.__side

    def mov_to(self, x, y):
        self.__x += x
        self.__y += y

class ElementPath(ElementCircuit):

    def mov_to(self, x, y):
        vertices_new = []
        for i in self.vertices:
            vertices_new.append((i[0] + x, i[1] + y))
        self.vertices = vertices_new
        self.label_x += x
        self.label_y += y

    def show(self, ax):
        path = Path(self.vertices, self.codes)
        path_patch = PathPatch(path, fill=False)
        ax.add_patch(path_patch)
        plt.text(self.label_x, self.label_y, self.name, color='black', fontsize=14)

class ContactOpen(ElementPath):

    def __init__(self, name='', label_a='', label_b=''):
        super().__init__(name)
        self.vertices = [(0, 0),   (5, 0),      (5, 5),      (15, 0),     (20, 0)]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.label_x = 5
        self.label_y = 6
        self.label_a = label_a
        self.label_b = label_b

    def show(self, ax):
        super().show(ax)
        plt.text(self.a[0], self.a[1]-5, self.label_a, color='black', fontsize=12)
        plt.text(self.b[0], self.b[1]-5,  self.label_b, color='black', fontsize=12)

    @property
    def a(self):
        return (self.vertices[0][0], self.vertices[0][1], True)

    @property
    def b(self):
        return (self.vertices[4][0], self.vertices[4][1], False)

class ContactClose(ElementPath):

    def __init__(self, name='', label_a='', label_b=''):
        super().__init__(name)
        self.vertices = [(0, 0),   (5, 0),      (5, -5),     (4, -5),     (15, 0),     (20, 0)]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.label_x = 5
        self.label_y = 6
        self.label_a = label_a
        self.label_b = label_b

    def show(self, ax):
        super().show(ax)
        plt.text(self.a[0]-1, self.a[1]-5, self.label_a, color='black', fontsize=12)
        plt.text(self.b[0]-1, self.b[1]-5,  self.label_b, color='black', fontsize=12)

    @property
    def a(self):
        return (self.vertices[0][0], self.vertices[0][1], True)

    @property
    def b(self):
        return (self.vertices[5][0], self.vertices[5][1], False)

class ContactOpenTimeOn(ContactOpen):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices += [(9, 3),   (9, 8),     (11,2),      (11, 8)]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [(6, 6),     (7, 7),    (8, 7.7),    (9, 8),    (11, 8),   (12, 7.7),    (13, 7),   (14, 6)]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.label_x = 5
        self.label_y = 10

    @property
    def a(self):
        return self.vertices[0]

    @property
    def b(self):
        return self.vertices[4]

class ContactOpenTimeOff(ContactOpen):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices += [(9, 3),   (9, 8),     (11,2),      (11, 8)]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [(6, 10),  (7, 9),    (8, 8.3),    (9, 8),    (11, 8),   (12, 8.3),    (13, 9),   (14, 10)]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.label_x = 5
        self.label_y = 11

    @property
    def a(self):
        return self.vertices[0]

    @property
    def b(self):
        return self.vertices[4]

class ContactCloseTimeOn(ContactClose):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices += [(9, -3),   (9, 7),     (11,-2),      (11, 7)]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [(6, 5),     (7, 6),    (8, 6.7),    (9, 7),    (11, 7),   (12, 6.7),    (13, 6),   (14, 5)]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.label_x = 5
        self.label_y = 9

    @property
    def a(self):
        return self.vertices[0]

    @property
    def b(self):
        return self.vertices[5]

class ContactCloseTimeOff(ContactClose):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices += [(9, -3),   (9, 6),     (11,-2),      (11, 6)]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [(6, 8),  (7, 7),    (8, 6.3),    (9, 6),    (11, 6),   (12, 6.3),    (13, 7),   (14, 8)]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.label_x = 5
        self.label_y = 9

    @property
    def a(self):
        return self.vertices[0]

    @property
    def b(self):
        return self.vertices[5]

class Winding(ElementPath):

    def __init__(self, name='', label_a='', label_b=''):
        super().__init__(name)
        self.vertices = [(0, 0),   (5, 0),      (5, 5),      (10, 5),     (10, -5),    (5, -5),     (5, 0),      (10, 0),     (15, 0)]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.label_x = 4
        self.label_y = 7
        self.__a = Connection(label_a, self.vertices[0][0], True)
        self.__b = Connection(label_b, self.vertices[-1][0], False)

    def show(self, ax):
        super().show(ax)
        plt.text(self.__a.x-5, self.__a.y-5, self.__a.name, color='black', fontsize=12)
        plt.text(self.__b.x-5, self.__b.y-5,  self.__b.name, color='black', fontsize=12)

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

class CT_W(ElementCircuit):

    def __init__(self, name='', label_a='', label_b=''):
        super().__init__(name)
        self.vertices = [[0, 0],   [0, 3.5],      [4, 3.5],     [4, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.centre = [2, 7]
        self.radius = 4
        self.label_a = label_a
        self.label_b = label_b
        self.__a = Connection(label_a, self.vertices[0][0], self.vertices[0][1], True)
        self.__b = Connection(label_b, self.vertices[-1][0], self.vertices[-1][1], False)

    def mov_to(self, x, y):
        for i in self.vertices:
            i[0] += x
            i[1] += y
        self.centre[0] += x
        self.centre[1] += y
        self.__a.mov_to(x, y)
        self.__b.mov_to(x, y)


    def show(self, ax):
        super().show()
        crl = plt.Circle(self.centre, self.radius, fill=False)
        path = Path(self.vertices, self.codes)
        path_patch = PathPatch(path, fill=False)
        ax.add_patch(path_patch)
        ax.add_patch(crl)
        ax.text(self.vertices[0][0] - 4, self.vertices[0][1] - 2, self.label_a, color='black', fontsize=12)
        ax.text(self.vertices[-1][0] + 1, self.vertices[0][1] - 2, self.label_b, color='black', fontsize=12)

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

class ConnectionTerminal(ElementCircuit):

    def __init__(self, name=''):
        super().__init__(name)
        self.centre = (0, 0)
        self.radius = 0.5
        self.__a = Connection('', 0, 0, True)
        self.__b = Connection('', 0, 0, False)

    def show(self, ax):
        crl = plt.Circle(self.centre, self.radius, color='black', fill=True)
        ax.add_patch(crl)
        ax.text(self.centre[0]-1, self.centre[1]-5, self.name, color='black', fontsize=12)

    def mov_to(self, x, y):
        self.centre = (x, y)
        self.__a.mov_to(x, y)
        self.__b.mov_to(x, y)

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

class ConnectionDetachable(ElementPath):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [(5, 5), (0, 0), (5, -5), (7, 5), (2, 0), (7, -5)]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.__a = Connection('', 0, 0, True)
        self.__b = Connection('', 2, 0, False)
        self.label_x = 4
        self.label_y = 10

    def mov_to(self, x, y):
        super().mov_to(x, y)
        self.__a.mov_to(x, y)
        self.__b.mov_to(x, y)

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

class Wire(ElementCircuit):

    def __init__(self, a : Connection, b : Connection, name=''):
        super().__init__(name)
        self.__a = a
        self.__b = b

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
            path = Path([(self.__a.x, self.__a.y), (self.__a.x + 20, self.__a.y)])
            path_patch = PathPatch(path, fill=False)
            ax.add_patch(path_patch)
            plt.text(self.__a.x+5, self.__a.y + 5, self.name, color='black', fontsize=12)

    def mov_to(self, x, y):
        pass

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b if self.__b.visible else Connection('', self.__a.x + 20, self.__a.y, True)

class Apparatus:

    def __init__(self, name=''):
        self.name = name

class RP23_25(Apparatus):

    def __init__(self, name=''):
        super().__init__(name)
        self.__w = Winding(name, '11', '12')
        self.__k1 = ContactClose(name, '1', '2')
        self.__k2 = ContactOpen(name, '3', '4')
        self.__k3 = ContactOpen(name, '5', '6')
        self.__k4 = ContactOpen(name, '7', '8')
        self.__k5 = ContactOpen(name, '9', '10')
        self.vertices = [(0, 0),   (30, 0),      (30, -60),     (0, -60),     (0, 0)]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]

    @property
    def w(self):
        return self.__w

    @property
    def k1(self):
        return self.__k1

    def show(self,ax):
        path = Path(self.vertices, self.codes)
        path_patch = PathPatch(path, fill=False)
        ax.add_patch(path_patch)

class CT2(Apparatus):

    def __init__(self, name=''):
        super().__init__(name)
        self.ct_w1 = CT_W('1')
        self.ct_w2 = CT_W('2')

    def show(self, ax):
        self.ct_w1.show(ax)
        self.ct_w2.show(ax)

class YA(Apparatus):

    def __init__(self, name=''):
        super().__init__(name)
        self.__w = Winding(name)

    def show(self, ax):
        self.__w.show(ax)

    def mov_to(self, x, y):
        self.__w.mov_to(x, y)

    @property
    def a(self):
        return self.__w.a

    @property
    def b(self):
        return self.__w.b

class XT(Apparatus):

    def __init__(self, name='', quantity=50):
        super().__init__(name)
        self.n = []
        for i in range(quantity):
            self.n.append(ConnectionTerminal(str(i)))

class CircuitDiagram():

    def __init__(self):
        self.__list_circuits = []

    def add(self, *args):
        circuit_elements = []
        for i in args:
            circuit_elements.append(i)
        self.__list_circuits.append(circuit_elements)

    def show(self, ax):
        last_x = 20
        last_y = 200
        for i in self.__list_circuits:
            for j in i:
                j.mov_to(last_x, last_y)
                j.show(ax)
                last_x, last_y = j.b.x, j.b.y

fig = plt.figure(figsize=(250, 250))
ax = fig.add_subplot()
ax.set(xlim=(0, 250), ylim=(0, 250))
ct_a = CT2('ТТа')
xt = XT('SX', 50)
w411 = Wire(ct_a.ct_w1.b, xt.n[6].a, 'A411')
xt1 = ConnectionDetachable('XT1/12')
w412 = Wire(xt.n[6].b, xt1.a, '')
yat_a = YA('YAA1')
w413 = Wire(xt1.b, yat_a.a)
'''

yat_c = YA('YAC1')
kl1 = RP361('KL1')
kl2 = RP361('KL2')
a1 = MR5PO50('A1')

w7 = Wire(kl1.k1.b, kl1.w.a, '7')
rel_otc = MountingModule('Релейный отсек')
sh8.add(yat_a, yat_c, kl1, kl2, a1)
'''
cd = CircuitDiagram()
cd.add(ct_a.ct_w1, w411, xt.n[6], w412, xt1, w413, yat_a)
cd.show(ax)
#wd = WiringDiagram()
#wd.add(sh8)
#wd.show(ax)

#cm = CableMagazine()
#cm.add(cab101, cab102, cab103)
#cm.show(ax)

#ci = CableInstallation()
#ci.add(cab101, cab102, cab103)
#ci.show(ax)
plt.show()