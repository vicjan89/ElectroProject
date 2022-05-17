import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

class ElementCircuit:

    def __init__(self, name=''):
        self.name = name

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
        self.label_a = label_a
        self.label_b = label_b

    def show(self, ax):
        super().show(ax)
        plt.text(self.a[0]-5, self.a[1]-5, self.label_a, color='black', fontsize=12)
        plt.text(self.b[0]-5, self.b[1]-5,  self.label_b, color='black', fontsize=12)

    @property
    def a(self):
        return (self.vertices[0][0], self.vertices[0][1], True)

    @property
    def b(self):
        return (self.vertices[-1][0], self.vertices[-1][1], False)

class Wire(ElementCircuit):

    def __init__(self, x1, y1, side1, x2, y2, side2, name=''):
        super().__init__(name)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.side1 = side1
        self.side2 = side2

    def show(self, ax):
        p = [(self.x1, self.y1)]
        dx1 = -5 if self.side1 else 5
        dy1 = -5 if self.y1 > self.y2 else 5
        dx2 = -5 if self.side2 else 5
        dy2 = 5 if self.y1 > self.y2 else -5
        p.append((self.x1 + dx1, self.y1 + dy1))
        p.append((self.x1 + dx1, (self.y1 + dx2 + self.y2 + dy2)/2 + self.y1))
        p.append((self.x2 + dx2, (self.y1 + dx2 + self.y2 + dy2) / 2 + self.y1))
        p.append((self.x2 + dx2, self.y2 + dy2))
        p.append((self.x2, self.y2))
        path = Path(p, [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO])
        path_patch = PathPatch(path, fill=False)
        ax.add_patch(path_patch)
        plt.text(self.x1 + dx1, (self.y1 + dx2 + self.y2 + dy2)/2 + self.y1 + 2, self.name, color='black', fontsize=14)

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

fig = plt.figure(figsize=(200, 100))
ax = fig.add_subplot()
ax.set(xlim=(0, 200), ylim=(0, 100))
kl1 = RP23_25('KL1')
yat = YA('YAT')
yac = YA('YAC')
sac1 = TO2('SAC1')
w7 = Wire(kl1.k1.b, kl1.w.a, '7')
sh8 = MountingModule('Шкаф №8')
sh8.add(kl1, yat, yac, sac1, w7)
cd = CircuitDiagram()
cd.add(sh8)
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