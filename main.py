import ezdxf
import math

LEFT = 1
RIGHT = 2
BOTH = 3
UP = 4
DOWN = 5


class Path:
    MOVETO = 1
    LINETO = 2


# Базовый класс

class ElementCircuit:

    def __init__(self, name='', highlight=False):
        self.name = name
        self.__visible = False
        self.__highlight = highlight

    def show(self):
        self.__visible = True

    @property
    def visible(self):
        return self.__visible

    @property
    def highlight(self):
        return self.__highlight

# Базовый класс для графических элементов

class ElementGraph(ElementCircuit):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight)
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
            x = i[0]
            i[0] = math.cos(math.radians(angle)) * x - math.sin(math.radians(angle)) * i[1]
            i[1] = math.sin(math.radians(angle)) * x - math.cos(math.radians(angle)) * i[1]
        for i in self.centers:
            x = i[0]
            i[0] = math.cos(math.radians(angle)) * x - math.sin(math.radians(angle)) * i[1]
            i[1] = math.sin(math.radians(angle)) * x - math.cos(math.radians(angle)) * i[1]
        for i in self.labels_xy:
            x = i[0]
            i[0] = math.cos(math.radians(angle)) * x - math.sin(math.radians(angle)) * i[1]
            i[1] = math.sin(math.radians(angle)) * x - math.cos(math.radians(angle)) * i[1]

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
        if self.highlight:
            lw = 100
        else:
            lw = 0
        if len(self.vertices) > 0:
            path = []
            for i in range(len(self.vertices)):
                if self.codes[i] == Path.MOVETO:
                    if len(path) > 0:
                        ax.add_lwpolyline(path, dxfattribs={'lineweight':lw})
                    path = [self.vertices[i]]
                elif self.codes[i] == Path.LINETO:
                    path.append(self.vertices[i])
                else:
                    raise Exception('Неправильный код пути полилинии!')
                ax.add_lwpolyline(path, dxfattribs={'lineweight':lw})
        for i in range(len(self.centers)):
            ax.add_circle(self.centers[i], radius=self.radii[i], dxfattribs={'lineweight':lw})
        for i in range(len(self.labels_xy)):
            ax.add_text(self.labels[i], dxfattribs={'style' : 'cyrillic_ii'}).set_pos((self.labels_xy[i][0], self.labels_xy[i][1]), align='BOTTOM_CENTER')


# Графические элементы

class ContactOpen(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [15, 5], [15, 0], [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.labels_xy = [[8, 6]]
        self.labels = [name]


class ContactClose(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [16, -5], [15, -5], [15, 0], [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[10, 5]]
        self.labels = [name]


class ContactOpenTimeOn(ContactOpen):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, 3], [9, 8], [11, 2], [11, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 6], [7, 7], [8, 7.7], [9, 8], [11, 8], [12, 7.7], [13, 7], [14, 6]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 10]]


class ContactOpenTimeOff(ContactOpen):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, 3], [9, 8], [11, 2], [11, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 10], [7, 9], [8, 8.3], [9, 8], [11, 8], [12, 8.3], [13, 9], [14, 10]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 11]]


class ContactCloseTimeOn(ContactClose):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, -3], [9, 7], [11, -2], [11, 7]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 5], [7, 6], [8, 6.7], [9, 7], [11, 7], [12, 6.7], [13, 6], [14, 5]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 9]]


class ContactCloseTimeOff(ContactClose):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices += [[9, -3], [9, 6], [11, -2], [11, 6]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.vertices += [[6, 8], [7, 7], [8, 6.3], [9, 6], [11, 6], [12, 6.3], [13, 7], [14, 8]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                       Path.LINETO]
        self.labels_xy = [[5, 9]]


class Diode(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [15, 0], [5, 3.5], [10, 0], [5, -3.5], [5, 3.5], [10, 3.5], [10, -35]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.MOVETO,
                      Path.LINETO]
        self.labels_xy = [[10, 4]]
        self.labels = [name]


class Winding(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight)
        self.vertices = [[0, 0], [5, 0], [5, 5], [10, 5], [10, -5], [5, -5], [5, 0], [10, 0], [15, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                      Path.MOVETO, Path.LINETO]
        self.labels_xy = [[7, 6]]
        self.labels = [name]


class CT_W(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [0, 3.5], [4, 3.5], [4, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.centers = [[2, 7]]
        self.radii = [4]
        self.labels_xy = [[0, 12]]
        self.labels = [name]


class ConnectionDetachable(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[5, 5], [0, 0], [5, -5], [7, 5], [2, 0], [7, -5]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[1, 2]]
        self.labels = [name]


# Базовый класс для графичиеских объектов с соединителями

class GraphWithConnection(ElementGraph):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.connections = {}

    def mov_to(self, base_point_key=None, x=0, y=0):
        if base_point_key == None:
            base_point_key = list(self.connections.keys())[0]
        dx = x - self.connections[base_point_key][0][0]
        dy = y - self.connections[base_point_key][0][1]
        super().mov_to(dx, dy)
        for i in self.connections.values():
            i[0][0] += dx
            i[0][1] += dy

    def rotate(self, angle):
        super().rotate(angle)
        for i in self.connections.values():
            i[0][0] = math.cos(math.radians(angle)) * i[0][0] - math.sin(math.radians(angle)) * i[0][1]
            i[0][1] = math.sin(math.radians(angle)) * i[0][0] - math.cos(math.radians(angle)) * i[0][1]
            if angle > 90:
                if i[1] == LEFT:
                    i[1] = RIGHT
                elif i[1] == RIGHT:
                    i[1] = LEFT


# Умный соединитель

class Wire(ElementCircuit):
    '''Умный соединитель'''

    def __init__(self, a, key_a, b, key_b, name='', cable=None, highlight=False):
        super().__init__(name, highlight=highlight)
        self.__a = a
        self.__key_a = key_a
        self.__b = b
        self.__key_b = key_b
        if cable != None:
            cable.add(self)

    def show(self, ax):
        if self.highlight:
            lw = 100
        else:
            lw = 0
        if type(self.__key_a) is int:
            key_a = abs(self.__key_a)
        else:
            key_a = self.__key_a
        if type(self.__key_b) is int:
            key_b = abs(self.__key_b)
        else:
            key_b = self.__key_b
        xa = self.__a.connections[key_a][1].connections[key_a][0][0]
        ya = self.__a.connections[key_a][1].connections[key_a][0][1]
        xb = self.__b.connections[key_b][1].connections[key_b][0][0]
        yb = self.__b.connections[key_b][1].connections[key_b][0][1]
        side_a = self.__a.connections[key_a][1].connections[key_a][1]
        side_b = self.__b.connections[key_b][1].connections[key_b][1]
        visible_a = self.__a.connections[key_a][1].visible
        visible_b = self.__b.connections[key_b][1].visible
        if visible_a and visible_b:
            if xa == xb:
                if side_a == LEFT:
                    dx = -5
                elif side_a == RIGHT:
                    dx = 5
                else:
                    dx = 0
                ax.add_lwpolyline(((xa, ya), (xa + dx, ya), (xb + dx, yb), (xb, yb)), dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa, ya + (yb - ya) / 2))
            else:
                ax.add_lwpolyline(((xa, ya), (xa, yb), (xb, yb)), dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa, yb))
        elif visible_a and not visible_b:
            if side_a == RIGHT or side_a == BOTH:
                xm = xa + 20
                ym = ya
                ax.add_line((xa, ya), (xm, ym), dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa + 5, ya + 5))
            elif side_a == LEFT:
                xm = xa
                ym = ya - 25
                ax.add_lwpolyline([(xa, ya), (xa - 5, ya), (xa - 5, ya - 25), (xm, ym)], dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa, ya - 15))
            self.__b.connections[key_b][1].mov_to(base_point_key=key_b, x=xm, y=ym)
            self.__b.connections[key_b][1].show(ax)
        elif visible_b and not visible_a:
            if side_b == LEFT or side_b == BOTH:
                xm = xb - 20
                ym = yb
                ax.add_line((xb, yb), (xm, ym), dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xb - 10, yb + 5))
            elif side_b == RIGHT:
                xm = xb
                ym = yb - 25
                ax.add_lwpolyline([(xb, yb), (xb + 5, yb), (xb + 5, yb - 25), (xm, ym)], dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xb, yb - 15))
            self.__a.connections[key_a][1].mov_to(base_point_key=key_a, x=xm, y=ym)
            self.__a.connections[key_a][1].show(ax)

    def show_wd(self, ax, coords):
        if self.highlight:
            lw = 100
        else:
            lw = 0
        xa = self.__a.connections[self.__key_a][0][0]
        ya = self.__a.connections[self.__key_a][0][1]
        xb = self.__b.connections[self.__key_b][0][0]
        yb = self.__b.connections[self.__key_b][0][1]
        side_a = self.__a.connections[self.__key_a][2]
        side_b = self.__b.connections[self.__key_b][2]
        visible_a = self.__a.visible
        visible_b = self.__b.visible
        if type(self.__key_a) is int:
            key_a = abs(self.__key_a)
        else:
            key_a = self.__key_a
        if type(self.__key_b) is int:
            key_b = abs(self.__key_b)
        else:
            key_b = self.__key_b
        name_a = self.__a.name + '-' + str(key_a)
        name_b = self.__b.name + '-' + str(key_b)
        list_coords = []
        if visible_a:
            match coords.count((xa, ya)):
                case 0:
                    dy = 0
                case 1:
                    dy = -2
                case 2:
                    dy = 2
            if side_a == LEFT:
                dx = -5
                a = 'BOTTOM_RIGHT'
            elif side_a == RIGHT:
                dx = 5
                a = 'BOTTOM_LEFT'
            ax.add_lwpolyline(((xa, ya), (xa + dx, ya + dy), (xa + 2 * dx + abs(dy) * dx, ya + dy)), dxfattribs={'lineweight':lw})
            ax.add_text(name_b, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa + dx + abs(dy) * dx, ya + dy), align=a)
            list_coords.append((xa, ya))
        if visible_b:
            match coords.count((xb, yb)):
                case 0:
                    dy = 0
                case 1:
                    dy = -2
                case 2:
                    dy = 2
            if side_b == LEFT:
                dx = -5
                a = 'BOTTOM_RIGHT'
            elif side_b == RIGHT:
                dx = 5
                a = 'BOTTOM_LEFT'
            ax.add_lwpolyline(((xb, yb), (xb + dx, yb + dy), (xb + 2 * dx + abs(dy) * dx, yb + dy)), dxfattribs={'lineweight':lw})
            ax.add_text(name_a, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xb + dx + abs(dy) * dx, yb + dy), align=a)
            list_coords.append((xb, yb))
        return list_coords


# Составные элементы схемы

class ConnectionTerminal(GraphWithConnection):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.centers = [[0, 0], [0, 0], [0, 0]]
        self.radii = [0.5, 0.3, 0.1]
        self.labels_xy = [[0, -5]]
        self.labels = [name]
        self.connections[name] = [[0, 0], BOTH]


class Connector(GraphWithConnection):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self += ConnectionDetachable()
        self.connections['s' + str(name)] = [[0, 0], LEFT]
        self.connections['p' + str(name)] = [[2, 0], RIGHT]


class Connectors(GraphWithConnection):

    def __init__(self, name='', quantity=32, highlight=False):
        super().__init__(name, highlight=highlight)
        self.n = [None]
        for i in range(1, quantity + 1):
            self.n.append(Connector(i))
            c = ConnectionDetachable(i)
            c.mov_to(0, -i * 12 - 12)
            self += c
            self.connections['s' + str(i)] = [[0, -i * 12 - 12], self.n[-1], LEFT]
            self.connections['p' + str(i)] = [[2, -i * 12 - 12], self.n[-1], RIGHT]


class CT2(GraphWithConnection):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.w1 = GraphWithConnection(highlight=highlight)
        self.w1 += CT_W(name + '-1')
        self.w1.connections['1И1'] = [[0, 0], LEFT]
        self.w1.connections['1И2'] = [[4, 0], RIGHT]
        self.w1.labels += ['1U1', '1U2']
        self.w1.labels_xy += [[-2, -5], [6, -5]]
        self.w2 = GraphWithConnection(highlight=highlight)
        self.w2 += CT_W(name + '-2')
        self.w2.connections['2И1'] = [[0, 0], LEFT]
        self.w2.connections['2И2'] = [[4, 0], RIGHT]
        self.vertices = [[0, 0], [15, 0], [15, -55], [0, -55], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[7, 5], [5, -5], [5, -20], [5, -35], [5, -50]]
        self.labels = [name, '1U1', '1U2', '2U1', '2U2']
        self.connections['1И1'] = [[0, -5], self.w1, LEFT]
        self.connections['1И2'] = [[0, -20], self.w1, LEFT]
        self.connections['2И1'] = [[0, -35], self.w2, LEFT]
        self.connections['2И2'] = [[0, -50], self.w2, LEFT]


class YA(GraphWithConnection):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.w = GraphWithConnection(highlight=highlight)
        self.w += Winding(name)
        self.w.connections[1] = [[0, 0], LEFT]
        self.w.connections[2] = [[15, 0], RIGHT]
        self += Winding(name)
        self.connections[1] = [[0, 0], self.w, LEFT]
        self.connections[2] = [[15, 0], self.w, RIGHT]


class Power(GraphWithConnection):

    def __init__(self, name='',highlight=False):
        super().__init__(name, highlight=highlight)
        self.vertices = [[0, 0], [5, 0], [5, 5], [15, 5], [15, -5], [5, -5], [5, 5], [15, 0], [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
                      Path.MOVETO, Path.LINETO]
        self.labels_xy = [[10, 6]]
        self.labels = [name]


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

    def __init__(self, name='', quantity=50, highlight=False):
        super().__init__(name, highlight=highlight)
        self.n = [None]
        h = 6
        for i in range(1, quantity + 1):
            self.n.append(ConnectionTerminal(i, highlight=highlight))
            self.connections[i] = [[0, -i * h - 3], self.n[-1], LEFT]
            self.connections[-i] = [[20, -i * h - 3], self.n[-1], RIGHT]
            self.vertices += [[0, -i * h], [20, -i * h], [20, -i * h - h], [0, -i * h - h], [0, -i * h]]
            self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
            self.labels += [i]
            self.labels_xy += [[10, -i * h - h + 1]]
        self.labels += [name]
        self.labels_xy += [[10, 0]]


class SF(GraphWithConnection):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k1_2 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name)
        k.rotate(90)
        k.labels_xy[0][0] += 10
        k.mov_to(0, -20)
        k.vertices += [[-1.5, -12], [-2.9, -12.7], [-4.6, -9.3], [-3.2, -8.6]]
        k.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.k1_2 += k
        self.k1_2.connections[1] = [[0, 0], UP]
        self.k1_2.connections[2] = [[0, -20], DOWN]
        self.k1_2.labels += [1, 2]
        self.k1_2.labels_xy += [[1, -2], [1, -22]]


class RP361(GraphWithConnection):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k2_4_6 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name)
        k.rotate(180)
        k.mov_to(20, 0)
        self.k2_4_6 += k
        k = ContactClose(name)
        k.rotate(180)
        k.mov_to(20, 20)
        self.k2_4_6 += k
        self.k2_4_6.vertices += [[20, 0], [20, 20]]
        self.k2_4_6.codes += [Path.MOVETO, Path.LINETO]
        self.k2_4_6.connections[2] = [[0, 0], LEFT]
        self.k2_4_6.connections[4] = [[20, 0], RIGHT]
        self.k2_4_6.connections[6] = [[0, 20], LEFT]
        self.k2_4_6.labels += [2, 4, 6]
        self.k2_4_6.labels_xy += [[0, -4], [20, -4], [0, 16]]
        self.w8_14 = GraphWithConnection(highlight=highlight)
        self.w8_14 += Winding(name)
        self.w8_14.connections[8] = [[0, 0], LEFT]
        self.w8_14.connections[14] = [[15, 0], RIGHT]
        self.w8_14.labels += [8, 14]
        self.w8_14.labels_xy += [[0, -4], [15, -4]]
        self.vertices = [[0, 0], [20, 0], [20, -70], [0, -70], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels = [name, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'РП-361']
        self.labels_xy = [[10, 0], [17, -7], [3, -7], [17, -17], [3, -17], [17, -27], [3, -27], [17, -37], [3, -37],
                          [17, -47], [3, -47],
                          [17, -57], [3, -57], [17, -67], [3, -67], [10, -5]]
        self.connections[1] = [[20, -5], self.k2_4_6, RIGHT]
        self.connections[2] = [[0, -5], self.k2_4_6, LEFT]
        self.connections[3] = [[20, -15], self.k2_4_6, RIGHT]
        self.connections[4] = [[0, -15], self.k2_4_6, LEFT]
        self.connections[5] = [[20, -25], self.k2_4_6, RIGHT]
        self.connections[6] = [[0, -25], self.k2_4_6, LEFT]
        self.connections[7] = [[30, -35], self.k2_4_6, RIGHT]
        self.connections[8] = [[0, -35], self.w8_14, LEFT]
        self.connections[9] = [[30, -45], self.k2_4_6, RIGHT]
        self.connections[10] = [[0, -45], self.k2_4_6, LEFT]
        self.connections[11] = [[30, -55], self.k2_4_6, RIGHT]
        self.connections[12] = [[0, -55], self.k2_4_6, LEFT]
        self.connections[13] = [[30, -65], self.k2_4_6, RIGHT]
        self.connections[14] = [[0, -65], self.w8_14, LEFT]


class BPT615(GraphWithConnection):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k1_2 = GraphWithConnection(highlight=highlight)
        self.k1_2 += Winding(name)
        self.k1_2.connections[2] = [[0, 0], LEFT]
        self.k1_2.connections[1] = [[15, 0], RIGHT]
        self.k1_2.labels += [2, 1]
        self.k1_2.labels_xy += [[0, -4], [15, -4]]
        self.k3_4 = GraphWithConnection(highlight=highlight)
        self.k3_4 += Winding(name)
        self.k3_4.connections[4] = [[0, 0], LEFT]
        self.k3_4.connections[3] = [[15, 0], RIGHT]
        self.k3_4.labels += [4, 3]
        self.k3_4.labels_xy += [[0, -4], [15, -4]]
        self.vertices = [[0, 0], [20, 0], [20, -120], [0, -120], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels = [name, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 'БПТ-615']
        self.labels_xy = [[10, 0], [17, -65], [17, -55], [17, -45], [17, -35], [3, -115], [3, -105], [3, -95], [3, -85],
                          [3, -75], [3, -65], [3, -55], [3, -45], [3, -35], [3, -25], [3, -15], [3, -5], [15, -5]]
        self.connections[1] = [[20, -65], self.k1_2, RIGHT]
        self.connections[2] = [[20, -55], self.k1_2, RIGHT]
        self.connections[3] = [[20, -45], self.k3_4, RIGHT]
        self.connections[4] = [[20, -35], self.k3_4, RIGHT]
        self.connections[5] = [[0, -115], self.k1_2, LEFT]
        self.connections[6] = [[0, -105], self.k1_2, LEFT]
        self.connections[7] = [[0, -95], self.k3_4, LEFT]
        self.connections[8] = [[0, -85], self.k3_4, LEFT]
        self.connections[9] = [[0, -75], self.k1_2, LEFT]
        self.connections[10] = [[0, -65], self.k1_2, LEFT]
        self.connections[11] = [[0, -55], self.k3_4, LEFT]
        self.connections[12] = [[0, -45], self.k3_4, LEFT]
        self.connections[13] = [[0, -35], self.k1_2, LEFT]
        self.connections[14] = [[0, -25], self.k1_2, LEFT]
        self.connections[15] = [[0, -15], self.k3_4, LEFT]
        self.connections[16] = [[0, -5], self.k3_4, LEFT]


class MR5PO50(GraphWithConnection):

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight)
        self.x8 = GraphWithConnection(highlight=highlight)
        self.x8.vertices += [[0, 0], [25, 0], [25, -150], [0, -150], [0, 0]]
        self.x8.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.x8.connections['X8:1'] = [[0, -12], LEFT]
        self.x8.connections['X8:2'] = [[25, -12], RIGHT]
        self.x8.connections['X8:4'] = [[0, -37], LEFT]
        self.x8.connections['X8:5'] = [[25, -37], RIGHT]
        self.x8.connections['X8:7'] = [[0, -62], LEFT]
        self.x8.connections['X8:8'] = [[25, -62], RIGHT]
        self.x8.connections['X8:10'] = [[0, -112], LEFT]
        self.x8.connections['X8:11'] = [[0, -137], LEFT]
        self.x8.connections['X8:12'] = [[25, -112], RIGHT]
        self.x8.labels += [name, 'X8:1', 'X8:2', 'X8:4', 'X8:5', 'X8:7', 'X8:8', 'X8:10', 'X8:11', 'X8:12', 'Ia', 'Ib',
                           'Ic', 'In']
        self.x8.labels_xy += [[12, 5], [5, -14], [20, -14], [5, -39], [20, -39], [5, -64], [20, -64], [5, -114],
                              [20, -139], [20, -114],
                              [12, -10], [12, -35], [12, -60], [12, -110]]
        self.x2_1_2 = GraphWithConnection(highlight=highlight)
        self.x2_1_2 += ContactClose('Рн')
        self.x2_1_2.labels += ['X2:1', 'X2:2']
        self.x2_1_2.labels_xy += [[0, -4], [20, -4]]
        self.x2_1_2.connections['X2:1'] = [[0, 0], LEFT]
        self.x2_1_2.connections['X2:2'] = [[20, 0], RIGHT]
        self.x2_3_4 = GraphWithConnection(highlight=highlight)
        self.x2_3_4 += ContactOpen('Рвкл')
        self.x2_3_4.labels += ['X2:3', 'X2:3']
        self.x2_3_4.labels_xy += [[0, -4], [20, -4]]
        self.x2_3_4.connections['X2:3'] = [[0, 0], LEFT]
        self.x2_3_4.connections['X2:4'] = [[20, 0], RIGHT]
        self.x2_5_6 = GraphWithConnection(highlight=highlight)
        self.x2_5_6 += ContactOpen('Роткл1')
        self.x2_5_6.labels += ['X2:5', 'X2:6']
        self.x2_5_6.labels_xy += [[0, -4], [20, -4]]
        self.x2_5_6.connections['X2:5'] = [[0, 0], LEFT]
        self.x2_5_6.connections['X2:6'] = [[20, 0], RIGHT]
        self.x2_7_8 = GraphWithConnection(highlight=highlight)
        self.x2_7_8 += ContactOpen('Роткл2')
        self.x2_7_8.labels += ['X2:7', 'X2:8']
        self.x2_7_8.labels_xy += [[0, -4], [20, -4]]
        self.x2_7_8.connections['X2:7'] = [[0, 0], LEFT]
        self.x2_7_8.connections['X2:8'] = [[20, 0], RIGHT]
        self.x1_1_2 = GraphWithConnection(highlight=highlight)
        self.x1_1_2 = Power(name)
        self.x1_1_2.labels += ['Uп', 'X1:1', 'X1:2']
        self.x1_1_2.labels_xy += [[10, 0], [0, -4], [20, -4]]
        self.x1_1_2.connections['X1:1'] = [[0, 0], LEFT]
        self.x1_1_2.connections['X1:2'] = [[20, 0], RIGHT]
        self.x4 = []
        self.x5 = []
        self.x6 = []
        for i in range(8):
            self.x4.append(GraphWithConnection(highlight=highlight))
            self.x4[i] += ContactOpen(name + 'Р' + str(i + 1))
            self.x4[i].labels += ['X4:' + str(i * 2 + 1), 'X4:' + str(i * 2 + 2)]
            self.x4[i].labels_xy += [[0, -2],[20,-2]]
            self.x4[i].connections['X4:' + str(i * 2 + 1)] = [[0,0],LEFT]
            self.x4[i].connections['X4:' + str(i * 2 + 2)] = [[20, 0], RIGHT]
            self.connections['X4:' + str(i * 2 + 1)] = [[0, -225 - i * 20], self.x4[i], LEFT]
            self.connections['X4:' + str(i * 2 + 2)] = [[0, -235 - i * 20], self.x4[i], LEFT]
            self.x5.append(Power(name + 'Д' + str(i + 1),highlight=highlight))
            self.x5[i].labels += ['X5:' + str(i * 2 + 1), 'X5:' + str(i * 2 + 2)]
            self.x5[i].labels_xy += [[0, -2],[20,-2]]
            self.x5[i].connections['X5:' + str(i * 2 + 1)] = [[0,0],LEFT]
            self.x5[i].connections['X5:' + str(i * 2 + 2)] = [[20, 0], RIGHT]
            self.connections['X5:' + str(i * 2 + 1)] = [[25, -225 - i * 20], self.x5[i], RIGHT]
            self.connections['X5:' + str(i * 2 + 2)] = [[25, -235 - i * 20], self.x5[i], RIGHT]
            self.x6.append(Power(name + 'Д' + str(i + 9),highlight=highlight))
            self.x6[i].labels += ['X6:' + str(i * 2 + 9), 'X6:' + str(i * 2 + 10)]
            self.x6[i].labels_xy += [[0, -2],[20,-2]]
            self.x6[i].connections['X6:' + str(i * 2 + 9)] = [[0,0],LEFT]
            self.x6[i].connections['X6:' + str(i * 2 + 10)] = [[20, 0], RIGHT]
            self.connections['X6:' + str(i * 2 + 9)] = [[25, -5 - i * 20], self.x6[i], RIGHT]
            self.connections['X6:' + str(i * 2 + 10)] = [[25, -15 - i * 20], self.x6[i], RIGHT]
        self.connections['X1:1'] = [[0, -195], self.x1_1_2, LEFT]
        self.connections['X1:2'] = [[0, -205], self.x1_1_2, LEFT]
        self.connections['X2:1'] = [[0, -105], self.x2_1_2, LEFT]
        self.connections['X2:2'] = [[0, -115], self.x2_1_2, LEFT]
        self.connections['X2:3'] = [[0, -125], self.x2_3_4, LEFT]
        self.connections['X2:4'] = [[0, -135], self.x2_3_4, LEFT]
        self.connections['X2:5'] = [[0, -145], self.x2_5_6, LEFT]
        self.connections['X2:6'] = [[0, -155], self.x2_5_6, LEFT]
        self.connections['X2:7'] = [[0, -165], self.x2_7_8, LEFT]
        self.connections['X2:8'] = [[0, -175], self.x2_7_8, LEFT]
        self.connections['X8:1'] = [[0, -5], self.x8, LEFT]
        self.connections['X8:2'] = [[0, -15], self.x8, LEFT]
        self.connections['X8:4'] = [[0, -25], self.x8, LEFT]
        self.connections['X8:5'] = [[0, -35], self.x8, LEFT]
        self.connections['X8:7'] = [[0, -45], self.x8, LEFT]
        self.connections['X8:8'] = [[0, -55], self.x8, LEFT]
        self.connections['X8:10'] = [[0, -65], self.x8, LEFT]
        self.connections['X8:11'] = [[0, -75], self.x8, LEFT]
        self.connections['X8:12'] = [[0, -85], self.x8, LEFT]
        self.vertices += [[0,5],[25,5],[25,-380],[0,-380],[0,5]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += [name, 'МР5ПО50']
        self.labels_xy += [[12,5], [12,0]]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 4 if value[0][0] == 0 else -4
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


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

    def __init__(self, list_elements: list, wires: dict):
        self.__list_circuits = list_elements
        self.__wires = wires.values()

    def show(self, ax):
        x = 0
        y = 0
        self.__list_circuits[0].mov_to(x=x, y=y)
        for i in self.__list_circuits:
            i.mov_to(x=x, y=y)
            i.show(ax)
            x += 70
        coords = []
        for i in self.__wires:
            coords += i.show_wd(ax, coords)


doc = ezdxf.new()
doc.units = ezdxf.units.MM
msp = doc.modelspace()

ct_a = CT2('TTa', highlight=True)
ct_c = CT2('TTc')
xt = XT('XT', 50, highlight=True)
xt1 = Connectors('XT1', 20, highlight=True)
yat_a = YA('YAA1', highlight=True)
yat_c = YA('YAC1')
xt1.n[13].rotate(180)
xt1.n[15].rotate(180)
kl1 = RP361('KL1', highlight=True)
kl2 = RP361('KL2')
a2 = BPT615('A2', highlight=True)
a1 = MR5PO50('A1',highlight=True)
sf = SF('SF1', highlight=True)

w = {}
w['1'] = Wire(ct_a, '1И1', ct_c, '1И1')
w['a411'] = Wire(ct_a, '1И2', xt, -6, 'A411', highlight=True)
w['a412'] = Wire(xt, 6, xt1, 's12', '')
w['a413'] = Wire(xt1, 'p12', yat_a, 1)
w['a414'] = Wire(yat_a, 2, xt1, 'p13')
w['a415'] = Wire(xt1, 's13', xt, 7)
w['a416'] = Wire(xt, -7, kl1, 2)
w['a417'] = Wire(kl1, 4, kl1, 8)
w['a418'] = Wire(kl1, 14, a2, 2)
w['a419'] = Wire(a2, 1, a1, 'X8:1')
w['c411'] = Wire(ct_c, '1И2', xt, -8, 'C411')
w['c412'] = Wire(xt, 8, xt1, 's14', '')
w['c413'] = Wire(xt1, 'p14', yat_c, 1)
w['c414'] = Wire(yat_c, 2, xt1, 'p15')
w['c415'] = Wire(xt1, 's15', xt, 9)
w['c416'] = Wire(xt, 9, kl2, 2)
w['c417'] = Wire(kl2, 4, kl2, 8)
w['c418'] = Wire(kl2, 14, a2, 4)
w['c419'] = Wire(a2, 3, a1, 'X8:7')
w['a420'] = Wire(xt, 6, kl1, 6)
w['c420'] = Wire(xt, 8, kl2, 6)
w['2'] = Wire(ct_a, '1И1', a1, 'X8:4')
w['3'] = Wire(a1, 'X8:2', a1, 'X8:5')
w['4'] = Wire(a1, 'X8:5', a1, 'X8:8')
'''
rel_otc = MountingModule('Релейный отсек')
sh8.add(yat_a, yat_c, kl1, kl2, a1)
'''

cd = CircuitDiagram(
    ct_a.w1, w['a411'], w['a412'], w['a413'], w['a414'], w['a415'], w['a416'], w['a417'], w['a418'],w['a419'],w['c419'],w['c418'],
    w['c417'],w['c416'],w['c415'],w['c414'],w['c413'],w['c412'], w['c411'],w['1'],w['a420'],w['c420'], w['2'],w['3'],w['4'],
    sf.k1_2)
cd.show(msp)


# wd = WiringDiagram([ct_a,ct_c,xt, xt1,yat_a,yat_c, kl1, kl2,a2, a1],w)
# wd.show(msp)
doc.saveas("Diagram.dxf", encoding='utf-8')
# cm = CableMagazine()
# cm.add(cab101, cab102, cab103)
# cm.show(ax)

# ci = CableInstallation()
# ci.add(cab101, cab102, cab103)
# ci.show(ax)

print('Чертёжи сформированы.')
