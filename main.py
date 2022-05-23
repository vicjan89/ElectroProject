import ezdxf
import math
LEFT=1
RIGHT=2
class Path:
    MOVETO = 1
    LINETO = 2

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
            path = []
            for i in range(len(self.vertices)):
                if self.codes[i] == Path.MOVETO:
                    if len(path) > 0:
                        ax.add_lwpolyline(path)
                    path = [self.vertices[i]]
                elif self.codes[i] == Path.LINETO:
                    path.append(self.vertices[i])
                else:
                    raise Exception('Неправильный код пути полилинии!')
                ax.add_lwpolyline(path)
        for i in range(len(self.centers)):
            crl = ax.add_circle(self.centers[i], radius=self.radii[i])
        for i in range(len(self.labels_xy)):
            ax.add_text(self.labels[i]).set_pos((self.labels_xy[i][0], self.labels_xy[i][1]), align='BOTTOM_CENTER')

#Графические элементы

class ContactOpen(ElementGraph):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [[0, 0],   [5, 0],      [15, 5],      [15, 0],     [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.labels_xy = [[10, 6]]
        self.labels = [name]

class ContactClose(ElementGraph):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [[0, 0],   [5, 0],      [16, -5],     [15, -5],     [15, 0],     [20, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[10, 6]]
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
        self.labels_xy = [[7, 6]]
        self.labels = [name]

class CT_W(ElementGraph):

    def __init__(self, name=''):
        super().__init__(name)
        self.vertices = [[0, 0],   [0, 3.5],      [4, 3.5],     [4, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.centers = [[2, 7]]
        self.radii = [4]
        self.labels_xy = [[0, 12]]
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
            if angle>90:
                if i[1]==LEFT:
                    i[1]=RIGHT
                elif i[1]==RIGHT:
                    i[1]=LEFT

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
        xa = self.__a.connections[self.__key_a][1].connections[self.__key_a][0][0]
        ya = self.__a.connections[self.__key_a][1].connections[self.__key_a][0][1]
        xb = self.__b.connections[self.__key_b][1].connections[self.__key_b][0][0]
        yb = self.__b.connections[self.__key_b][1].connections[self.__key_b][0][1]
        site_a = self.__a.connections[self.__key_a][1].connections[self.__key_a][1]
        site_b = self.__b.connections[self.__key_b][1].connections[self.__key_b][1]
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
            if site_a == RIGHT:
                xm = xa + 20
                ym = ya
                ax.add_line((xa,ya),(xm,ym))
                ax.add_text(self.name).set_pos((xa + 5,ya+5))
            elif site_a == LEFT:
                xm = xa
                ym = ya-25
                ax.add_lwpolyline([(xa,ya),(xa-5,ya),(xa-5,ya-25),(xm,ym)])
                ax.add_text(self.name).set_pos((xa, ya - 15))
            self.__b.connections[self.__key_b][1].mov_to(base_point_key=self.__key_b, x=xm, y=ym)

#Составные элементы схемы

class ConnectionTerminal(GraphWithConnection):

    def __init__(self, name=''):
        super().__init__(name)
        self.centers = [[0, 0], [0, 0], [0, 0]]
        self.radii = [0.5, 0.3, 0.1]
        self.labels_xy = [[0, -5]]
        self.labels = [name]
        self.connections[name] = [[0, 0],RIGHT]

class Connector(GraphWithConnection):

    def __init__(self, name=''):
        super().__init__(name)
        self += ConnectionDetachable()
        self.connections['s' + str(name)] = [[0, 0],LEFT]
        self.connections['p' + str(name)] = [[2, 0],RIGHT]

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
        self.w1 = GraphWithConnection()
        self.w1 += CT_W(name + '-1')
        self.w1.connections['1И1'] = [[0, 0],LEFT]
        self.w1.connections['1И2'] = [[4, 0],RIGHT]
        self.w1.labels += ['1U1', '1U2']
        self.w1.labels_xy += [[-2, -5], [6, -5]]
        self.w2 = GraphWithConnection(name + '-2')
        self.w2 += CT_W(name + '-2')
        self.w2.connections['2И1'] = [[0, 0],LEFT]
        self.w2.connections['2И2'] = [[4, 0],RIGHT]
        self.vertices = [[0, 0], [20, 0], [20, -50], [0, -50]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[0, 5]]
        self.labels = [[name]]
        self.connections['1И1'] = [[0, -10], self.w1,LEFT]
        self.connections['1И2'] = [[20, -10], self.w1,RIGHT]
        self.connections['2И1'] = [[0, -40], self.w2,LEFT]
        self.connections['2И2'] = [[20, -40], self.w2,RIGHT]

class YA(GraphWithConnection):

    def __init__(self, name=''):
        super().__init__(name)
        self.w = GraphWithConnection(name)
        self.w += Winding(name)
        self.w.connections[1] = [[0, 0],LEFT]
        self.w.connections[2] = [[15, 0],RIGHT]
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

class RP361(GraphWithConnection):

    def __init__(self, name=''):
        super().__init__(name)
        self.k2_4_6 = GraphWithConnection()
        k =  ContactOpen(name)
        k.rotate(180)
        k.mov_to(20, 0)
        self.k2_4_6 += k
        k = ContactClose(name)
        k.rotate(180)
        k.mov_to(20, 20)
        self.k2_4_6 += k
        self.k2_4_6.vertices += [[20, 0], [20, 20]]
        self.k2_4_6.codes += [Path.MOVETO, Path.LINETO]
        self.k2_4_6.connections[2] = [[0, 0],LEFT]
        self.k2_4_6.connections[4] = [[20, 0],RIGHT]
        self.k2_4_6.connections[6] = [[0, 15],LEFT]
        self.k2_4_6.labels += [2,4,6]
        self.k2_4_6.labels_xy += [[0,-4],[20,-4],[0,16]]
        self.w8_14 = GraphWithConnection()
        self.w8_14 += Winding(name)
        self.w8_14.connections[8] = [[0, 0],LEFT]
        self.w8_14.connections[14] = [[15, 0],RIGHT]
        self.w8_14.labels += [8, 14]
        self.w8_14.labels_xy += [[0, -4], [20, -4]]
        self.connections[2] = [[0, 0], self.k2_4_6]
        self.connections[4] = [[0, 0], self.k2_4_6]
        self.connections[6] = [[0, 0], self.k2_4_6]
        self.connections[8] = [[0, 0], self.w8_14]
        self.connections[14] = [[0, 0], self.w8_14]

class MR5PO50(GraphWithConnection):

    def __init__(self, name=''):
        super().__init__(name)
        self.x8 = GraphWithConnection()
        self.x8.vertices += [[0,0], [25,0], [25,-150],[0,-150],[0,0]]
        self.x8.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.x8.connections['X8:1'] = [[0, -12],LEFT]
        self.x8.connections['X8:2'] = [[25, -12],RIGHT]
        self.x8.connections['X8:4'] = [[0, -37],LEFT]
        self.x8.connections['X8:5'] = [[25, -37],RIGHT]
        self.x8.connections['X8:7'] = [[0, -62],LEFT]
        self.x8.connections['X8:8'] = [[25, -62],RIGHT]
        self.x8.connections['X8:10'] = [[0, -112],LEFT]
        self.x8.connections['X8:11'] = [[0, -137],LEFT]
        self.x8.connections['X8:12'] = [[25, -112],RIGHT]
        self.x8.labels += [name, 'X8:1','X8:2','X8:4','X8:5','X8:7','X8:8','X8:10','X8:11','X8:12']
        self.x8.labels_xy += [[12, 10],[5,-14],[20,-14],[5,-39],[20,-39],[5,-64],[20,-64],[5,-114],[20,-139],[20,-114]]
        self.connections['X8:1'] = [[0, 12], self.x8]
        self.connections['X8:2'] = [[25, 12], self.x8]
        self.connections['X8:4'] = [[0, 37], self.x8]
        self.connections['X8:5'] = [[25, 37], self.x8]
        self.connections['X8:7'] = [[0, 62], self.x8]
        self.connections['X8:8'] = [[25, 62], self.x8]
        self.connections['X8:10'] = [[0, 112], self.x8]
        self.connections['X8:11'] = [[0, 137], self.x8]
        self.connections['X8:12'] = [[25, 112], self.x8]

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

doc = ezdxf.new()
msp = doc.modelspace()
ct_a = CT2('TTa')
ct_c = CT2('TTc')
xt = XT('XT1', 50)
xt1 = Connectors('XT1', 32)
yat_a = YA('YAA1')
yat_c = YA('YAC1')
xt1.n[13].rotate(180)
xt1.n[15].rotate(180)
kl1 = RP361('KL1')
kl2 = RP361('KL2')
a1 = MR5PO50('A1')
w1=Wire(ct_a,'1И1',ct_c,'1И1')
wa411 = Wire(ct_a, '1И2', xt, 6,  'A411')
wa412 = Wire(xt, 6, xt1, 's12', '')
wa413 = Wire(xt1, 'p12', yat_a, 1)
wa414 = Wire(yat_a, 2, xt1, 'p13')
wa415 = Wire(xt1, 's13', xt, 7)
wa416 = Wire(xt, 7, kl1, 2)
wa417 = Wire(kl1, 4, kl1, 8)
wa418 = Wire(kl1,14,a1,'X8:1')
wc411 = Wire(ct_c, '1И2', xt, 8,  'C411')
wc412 = Wire(xt, 8, xt1, 's14', '')
wc413 = Wire(xt1, 'p14', yat_c, 1)
wc414 = Wire(yat_c, 2, xt1, 'p15')
wc415 = Wire(xt1, 's15', xt, 9)
wc416 = Wire(xt, 9, kl2, 2)
wc417 = Wire(kl2, 4, kl2, 8)
wc418 = Wire(kl2,14,a1,'X8:7')
'''
rel_otc = MountingModule('Релейный отсек')
sh8.add(yat_a, yat_c, kl1, kl2, a1)
'''
cd = CircuitDiagram(ct_a.w1, wa411, xt.n[6], wa412, xt1.n[12], wa413, yat_a.w, wa414, xt1.n[13], wa415, xt.n[7], wa416, kl1.k2_4_6,wa417, kl1.w8_14,wa418,a1.x8,
                    w1,ct_c.w1, wc411, xt.n[8], wc412, xt1.n[14], wc413, yat_c.w, wc414, xt1.n[15], wc415, xt.n[9], wc416, kl2.k2_4_6,wc417, kl2.w8_14,wc418,)
cd.show(msp)

wd = WiringDiagram(ct_a)
wd.show(msp)

#cm = CableMagazine()
#cm.add(cab101, cab102, cab103)
#cm.show(ax)

#ci = CableInstallation()
#ci.add(cab101, cab102, cab103)
#ci.show(ax)
doc.saveas("RZAproject.dxf", encoding='cp1251')
print('Чертёж сформирован.')