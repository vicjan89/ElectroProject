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

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [(0, 0),   (5, 0),      (5, 5),      (15, 0),     (20, 0)]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.label_x = 5
        self.label_y = 6

    @property
    def a(self):
        return *self.vertices[0], True

    @property
    def b(self):
        return *self.vertices[4], False

class ContactClose(ElementPath):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [(0, 0),   (5, 0),      (5, -5),     (4, -5),     (15, 0),     (20, 0)]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.label_x = 5
        self.label_y = 6

    @property
    def a(self):
        return *self.vertices[0], True

    @property
    def b(self):
        return *self.vertices[5], False

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

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [(0, 0),   (5, 0),      (5, 5),      (10, 5),     (10, -5),    (5, -5),     (5, 0),      (10, 0),     (15, 0)]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.label_x = 4
        self.label_y = 7

    @property
    def a(self):
        return *self.vertices[0], True

    @property
    def b(self):
        return *self.vertices[-1], False

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
        dy1 = -10 if self.y1 > self.y2 else 10
        dx2 = -5 if self.side2 else 5
        dy2 = 10 if self.y1 > self.y2 else -10
        p.append((self.x1 + dx1, self.y1 + dy1))
        p.append((self.x1 + dx1, (self.y1 + dx2 + self.y2 + dy2)/2 + self.y1))
        p.append((self.x2 + dx2, (self.y1 + dx2 + self.y2 + dy2) / 2 + self.y1))
        p.append((self.x2 + dx2, self.y2 + dy2))
        p.append((self.x2, self.y2))
        path = Path(p, [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO])
        path_patch = PathPatch(path, fill=False)
        ax.add_patch(path_patch)
        plt.text(self.x1 + dx1, (self.y1 + dx2 + self.y2 + dy2)/2 + self.y1 + 2, self.name, color='black', fontsize=14)

fig,ax = plt.subplots()
ax.set(xlim=(0, 200), ylim=(0, 100))
c = ContactCloseTimeOn('KT1')
c.mov_to(10, 10)
c.show(ax)
d = ContactCloseTimeOff('KT2')
d.mov_to(30, 10)
d.show(ax)
e = ContactOpenTimeOn('KT1')
e.mov_to(50, 10)
e.show(ax)
r = ContactOpenTimeOff('KT2')
r.mov_to(70, 10)
r.show(ax)
b = ContactClose('KH2')
b.mov_to(90, 10)
b.show(ax)
v = ContactOpen('KL1')
v.mov_to(110, 10)
v.show(ax)
w = Winding('KL1')
w.mov_to(160, 50)
w.show(ax)
l = Wire(*v.b, *w.a, 'A401')
l.show(ax)
plt.show()