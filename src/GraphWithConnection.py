'''Графические элементы с коннекторами.'''

import random
from src.GraphicsElements import *



class GraphWithConnection(ElementGraph):
    '''Базовый класс для графических элементов с коннекторами.'''
    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.connections = {}
        self.__x = 0
        self.__y = 0

    def mov_to(self, base_point_key=None, x=0, y=0):
        self.__x = x
        self.__y = y
        if base_point_key == None:
            base_point_key = list(self.connections.keys())[0]
        dx = x - self.connections[base_point_key][0][0]
        dy = y - self.connections[base_point_key][0][1]
        super().mov_to(dx, dy)
        for i in self.connections.values():
            i[0][0] += dx
            i[0][1] += dy
        return self

    def mov(self, dx=0, dy=0):
        self.__x += dx
        self.__y += dy
        for i in self.connections.values():
            i[0][0] += dx
            i[0][1] += dy
        return self

    def rotate(self, angle):

        def rotate90(num):
            for n in range(num):
                if i[1] == Const.LEFT:
                    i[1] = Const.DOWN
                elif i[1] == Const.UP:
                    i[1] = Const.LEFT
                elif i[1] == Const.RIGHT:
                    i[1] = Const.UP
                elif i[1] == Const.DOWN:
                    i[1] = Const.RIGHT

        super().rotate(angle)
        for i in self.connections.values():
            i[0][0] = math.cos(math.radians(angle)) * i[0][0] - math.sin(math.radians(angle)) * i[0][1]
            i[0][1] = math.sin(math.radians(angle)) * i[0][0] - math.cos(math.radians(angle)) * i[0][1]
            if 45 < angle <= 135:
                num = 1
            elif 135 < angle <= 225:
                num = 2
            elif 225 < angle <= 315:
                num = 3
            else:
                num = 0
            rotate90(num)

    def mirror(self):
        super().mirror()
        for i in self.connections.values():
            i[0][0] = -i[0][0]
            if i[1] == Const.LEFT:
                i[1] = Const.RIGHT
            elif i[1] == Const.RIGHT:
                i[1] = Const.LEFT

    def __str__(self):
        return str(self.name)

    @property
    def contains(self):
        list_elements = []
        for value in self.connections.values():
            if value[1] not in list_elements:
                list_elements.append(value[1])
        return list_elements

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

class Wire(ElementCircuit):
    '''Умный соединитель.'''
    NORMAL = 1
    ADD = 2
    DEL = 3

    def __init__(self, a=None, key_a=None, b=None, key_b=None, name='', style=NORMAL):
        super().__init__(name)
        self.__a = a
        self.__key_a = key_a
        self.__b = b
        self.__key_b = key_b
        self.style = style


    def encoder(self):
        return {'a':self.__a.name,
                'key_a':self.key_a,
                'b':self.__b.name,
                'key_b':self.__key_b,
                'name':self.name,
                'style':self.style}

    def decoder(self,dict_wire):
        if 'a' in dict_wire:
            return Wire(**dict_wire)
        else:
            return dict_wire

    def __str__(self):
        return 'Wire: '+ str(self.a) + '/' + str(self.__key_a) + ' - ' + str(self.b) + '/' + str(self.__key_b)

    def show(self, ax):
        new_element = False
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
        if visible_a and visible_b and xa > 360 and xb > 360:
            match side_a:
                case Const.LEFT:
                    dx_a = -5
                    dy_a = 0
                case Const.RIGHT:
                    dx_a = 5
                    dy_a = 0
                case Const.UP:
                    dx_a = 0
                    dy_a = 5
                case Const.DOWN:
                    dx_a = 0
                    dy_a = -5
                case Const.ALL:
                    dx_a = 0
                    dy_a = 0
            match side_b:
                case Const.LEFT:
                    dx_b = -5
                    dy_b = 0
                case Const.RIGHT:
                    dx_b = 5
                    dy_b = 0
                case Const.UP:
                    dx_b = 0
                    dy_b = 5
                case Const.DOWN:
                    dx_b = 0
                    dy_b = -5
                case Const.ALL:
                    dx_b = 0
                    dy_b = 0
            xa1 = xa + dx_a
            xa2 = xa1 #+ dx_a * random.random()
            ya1 = ya + dy_a
            ya2 = ya1 #+ dy_a * random.random()
            xb1 = xb + dx_b
            xb2 = xb1 #+ dx_b * random.random()
            yb1 = yb + dy_b
            yb2 = yb1 #+ dy_b * random.random()
            xa3 = xa2
            ya3 = ya2
            xb3 = xb2
            yb3 = yb2
            if side_a == Const.ALL:
                if ya2 == yb2:
                    if xa2 > xb2:
                        side_a = Const.LEFT
                    else:
                        side_a = Const.RIGHT
                elif ya2 > yb2:
                    side_a = Const.DOWN
                else:
                    side_a = Const.UP
            if side_b == Const.ALL:
                if ya2 == yb2:
                    if xa2 > xb2:
                        side_b = Const.RIGHT
                    else:
                        side_b = Const.LEFT
                elif ya2 > yb2:
                    side_b = Const.UP
                else:
                    side_b = Const.DOWN
            lu = side_a == Const.LEFT and side_b == Const.UP
            ld = side_a == Const.LEFT and side_b == Const.DOWN
            ru = side_a == Const.RIGHT and side_b == Const.UP
            rd = side_a == Const.RIGHT and side_b == Const.DOWN
            ul = side_b == Const.LEFT and side_a == Const.UP
            dl = side_b == Const.LEFT and side_a == Const.DOWN
            ur = side_b == Const.RIGHT and side_a == Const.UP
            dr = side_b == Const.RIGHT and side_a == Const.DOWN
            if (side_a == Const.RIGHT or side_a == Const.LEFT) and (side_b == Const.UP or side_b == Const.DOWN):
                if (ld and (xa2 > xb2) and (ya2 < yb2)) or (lu and (xa2 > xb2) and (ya2 > yb2)) or (rd and (xa2 < xb2) and (ya2 < yb2)) or (ru and (xa2 < xb2) and (ya2 > yb2)):
                    xa3 = xb3 = xb2
                    ya3 = yb3 = ya2
                else:
                    xa3 = xb3 = xa2
                    ya3 = yb3 = yb2
            if ((side_a == Const.UP or side_a == Const.DOWN) and (side_b == Const.RIGHT or side_b == Const.LEFT)):
                if (ul and (xa2 < xb2) and (ya2 < yb2)) or (ur and (xa2 > xb2) and (ya2 < yb2)) or (dl and (xa2 < xb2) and (ya2 > yb2)) or (dr and (xa2 > xb2) and (ya2 > yb2)):
                    xa3 = xb3 = xa2
                    ya3 = yb3 = yb2
                else:
                    xa3 = xb3 = xb2
                    ya3 = yb3 = ya2
            if side_a == Const.LEFT and side_b == Const.LEFT:
                if abs(ya2 - yb2) > 6:
                    xa3 = xb3 = min(xa2,xb2)
                    ya3 = ya2
                    yb3 = yb2
                else:
                    xa3 = xa2
                    xb3 = xb2
                    ya3 = yb3 = min(ya2,yb2)-6
            if side_a == Const.RIGHT and side_b == Const.RIGHT:
                if abs(ya2 - yb2) >6:
                    xa3 = xb3 = max(xa2,xb2)
                    ya3 = ya2
                    yb3 = yb2
                else:
                    xa3 = xa2
                    xb3 = xb2
                    ya3 = yb3 = min(ya2, yb2) - 6
            if side_a == Const.UP and side_b == Const.UP:
                if abs(xa2 - xb2) >6:
                    ya3 = yb3 = max(ya2,yb2)
                    xa3 = xa2
                    xb3 = xb2
                else:
                    ya3 = ya2
                    yb3 = yb2
                    xa3 = xb3 = max(xa2,xb2) + 6
            if side_a == Const.DOWN and side_b == Const.DOWN:
                if abs(xa2 - xb2) > 6:
                    ya3 = yb3 = min(ya2,yb2)
                    xa3 = xa2
                    xb3 = xb2
                else:
                    ya3 = ya2
                    yb3 = yb2
                    xa3 = xb3 = max(xa2, xb2) + 6
            if (side_a == Const.UP and side_b == Const.DOWN) or (side_b == Const.UP and side_a == Const.DOWN):
                if abs(xa2 - xb2) > 6:
                    xa3 =xb3 = xa2 + (xb2-xa2)//2
                elif (side_a == Const.UP and side_b == Const.DOWN and ya2 < yb2) or (side_b == Const.UP and side_a == Const.DOWN and ya2 > yb2):
                    xa3 = xb3 =xa2
                else:
                    xa3 = xb3 = max(xa2, xb2) + 6
                ya3 = ya2
                yb3 = yb2
            if (side_a == Const.LEFT and side_b == Const.RIGHT) or (side_b == Const.LEFT and side_a == Const.RIGHT):
                if abs(ya2 - yb2) > 6:
                    ya3 =yb3 = ya2 + (yb2-ya2)//2
                elif (side_a == Const.LEFT and side_b == Const.RIGHT and xa2 > xb2) or (side_b == Const.LEFT and side_a == Const.RIGHT and xa2 < xb2):
                    ya3 = yb3 = ya2
                else:
                    ya3 = yb3 = max(ya2, yb2) + 6
                xa3 = xa2
                xb3 = xb2
            match self.style:
                case Wire.NORMAL:
                    lw = 0
                    lt = 'continuous'
                case Wire.ADD:
                    lw = 50
                    lt = 'continuous'
                case Wire.DEL:
                    lw = 100
                    lt = 'DOT'
            ax.add_lwpolyline(((xa, ya), (xa1, ya1), (xa2, ya2),(xa3,ya3),(xb3,yb3), (xb2, yb2), (xb1, yb1), (xb, yb)),
                              dxfattribs={'lineweight':lw,'linetype':lt})
            ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa, ya))
        # elif visible_a and not visible_b:
        #     match side_a:
        #         case Const.LEFT:
        #             dx_a = -10
        #             dy_a = 0
        #         case Const.RIGHT:
        #             dx_a = 10
        #             dy_a = 0
        #         case Const.UP:
        #             dx_a = 0
        #             dy_a = 10
        #         case Const.DOWN:
        #             dx_a = 0
        #             dy_a = -10
        #         case Const.ALL:
        #             dx_a = 0
        #             dy_a = 0
        #     ax.add_line((xa, ya), (xa + dx_a, ya + dy_a), dxfattribs={'lineweight':lw})
        #     ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa + 5, ya + 5))
        #     self.__b.connections[key_b][1].mov_to(base_point_key=key_b, x=xa+dx_a, y=ya+dy_a)
        #     self.__b.connections[key_b][1].show(ax)
        #     new_element = True
        # elif visible_b and not visible_a:
        #     match side_b:
        #         case Const.LEFT:
        #             dx_b = -10
        #             dy_b = 0
        #         case Const.RIGHT:
        #             dx_b = 10
        #             dy_b = 0
        #         case Const.UP:
        #             dx_b = 0
        #             dy_b = 10
        #         case Const.DOWN:
        #             dx_b = 0
        #             dy_b = -10
        #         case Const.ALL:
        #             dx_b = 0
        #             dy_b = 0
        #     ax.add_line((xb, yb), (xb + dx_b, yb + dy_b), dxfattribs={'lineweight': lw})
        #     ax.add_text(self.name, dxfattribs={'style': 'cyrillic_ii'}).set_pos((xb + 5, yb + 5))
        #     self.__a.connections[key_a][1].mov_to(base_point_key=key_a, x=xb + dx_b, y=yb + dy_b)
        #     self.__a.connections[key_a][1].show(ax)
        #     new_element = True
        return new_element


    def show_wd(self, ax, coords):
        if self.highlight:
            lw = 50
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
            if side_a ==Const.LEFT or side_a ==Const.RIGHT:
                match coords.count((xa, ya)):
                    case 0:
                        dy = 0
                    case 1:
                        dy = -4
                    case 2:
                        dy = 4
            if side_a == Const.DOWN or side_a ==Const.UP:
                match coords.count((xa, ya)):
                    case 0:
                        dx = 0
                    case 1:
                        dx = -4
                    case 2:
                        dx = 4
            if side_a ==Const.LEFT:
                dx = -5
                d2x = -10
                d2y = 0
                a = MTEXT_BOTTOM_RIGHT
                f = 0
            elif side_a ==Const.RIGHT:
                dx = 5
                d2x = 10
                d2y = 0
                a = MTEXT_BOTTOM_LEFT
                f = 0
            elif side_a == Const.DOWN:
                dy = -5
                d2x = 0
                d2y = -10
                a = MTEXT_BOTTOM_RIGHT
                f = 90
            elif side_a ==Const.UP:
                dy = 5
                d2x = 0
                d2y = 10
                a = MTEXT_BOTTOM_LEFT
                f = 90
            ax.add_lwpolyline(((xa, ya), (xa + dx, ya + dy), (xa + dx + d2x, ya + dy + d2y)), dxfattribs={'lineweight':lw})
            ax.add_text(name_b, dxfattribs={'style' : 'cyrillic_ii', 'rotation':f}).set_pos((xa + dx, ya + dy), align=a)
            list_coords.append((xa, ya))
        if visible_b:
            if side_b ==Const.LEFT or side_b ==Const.RIGHT:
                match coords.count((xb, yb)):
                    case 0:
                        dy = 0
                    case 1:
                        dy = -4
                    case 2:
                        dy = 4
            if side_b == Const.DOWN or side_b ==Const.UP:
                match coords.count((xb, yb)):
                    case 0:
                        dx = 0
                    case 1:
                        dx = -4
                    case 2:
                        dx = 4
            if side_b ==Const.LEFT:
                dx = -5
                d2x = -10
                d2y = 0
                a = MTEXT_BOTTOM_RIGHT
                f = 0
            elif side_b ==Const.RIGHT:
                dx = 5
                d2x = 10
                d2y = 0
                a = MTEXT_BOTTOM_LEFT
                f = 0
            elif side_b == Const.DOWN:
                dy = -5
                d2x = 0
                d2y = -10
                a = MTEXT_BOTTOM_RIGHT
                f = 90
            elif side_b ==Const.UP:
                dy = 5
                d2x = 0
                d2y = 10
                a = MTEXT_BOTTOM_LEFT
                f = 90
            ax.add_lwpolyline(((xb, yb), (xb + dx, yb + dy), (xb + dx + d2x, yb + dy + d2y)), dxfattribs={'lineweight':lw})
            ax.add_text(name_a, dxfattribs={'style' : 'cyrillic_ii', 'rotation':f}).set_pos((xb + dx, yb + dy), align=a)
            list_coords.append((xb, yb))
        return list_coords

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def a_visible(self):
        return self.__a.connections[self.__key_a][1].visible

    @property
    def b_visible(self):
        return self.__b.connections[self.__key_b][1].visible

    @property
    def key_a(self):
        return self.__key_a

    @property
    def key_b(self):
        return self.__key_b


class ConnectionTerminal(GraphWithConnection):
    '''Клемма.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.centers = [[0, 0], [0, 0], [0, 0]]
        self.radii = [0.5, 0.3, 0.1]
        self.labels_xy = [[1, -1, MTEXT_TOP_LEFT]]
        self.labels = [name]
        self.connections[name] = [[0, 0], Const.ALL]


class Connector(GraphWithConnection):
    '''Разъёмное соединение.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self += ConnectionDetachable(name=name, highlight=highlight)
        self.connections['s' + str(name)] = [[0, 0],Const.LEFT]
        self.connections['p' + str(name)] = [[2, 0],Const.RIGHT]


class Connectors(GraphWithConnection):
    '''Разъём на много соединений.'''

    def __init__(self, name='', quantity=32, highlight=False):
        super().__init__(name, highlight=highlight)
        self.n = [None]
        for i in range(1, quantity + 1):
            self.n.append(Connector(i))
            c = ConnectionDetachable(i)
            c.mov_to(0, -i * 12 - 12)
            self += c
            self.connections['s' + str(i)] = [[0, -i * 12 - 12], self.n[-1],Const.LEFT]
            self.connections['p' + str(i)] = [[2, -i * 12 - 12], self.n[-1],Const.RIGHT]


class CT2(GraphWithConnection):
    '''Трансформатор тока с двумя вторичными обмотками.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.w1 = GraphWithConnection(highlight=highlight)
        self.w1 += CT_W(name + '-1')
        self.w1.connections['1И1'] = [[0, 0],Const.LEFT]
        self.w1.connections['1И2'] = [[4, 0],Const.RIGHT]
        self.w1.labels += ['1U1', '1U2']
        self.w1.labels_xy += [[-2, -5], [6, -5]]
        self.w2 = GraphWithConnection(highlight=highlight)
        self.w2 += CT_W(name + '-2')
        self.w2.connections['2И1'] = [[0, 0],Const.LEFT]
        self.w2.connections['2И2'] = [[4, 0],Const.RIGHT]
        self.vertices = [[0, 0], [15, 0], [15, -55], [0, -55], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[7, 5], [5, -5], [5, -20], [5, -35], [5, -50]]
        self.labels = [name, '1U1', '1U2', '2U1', '2U2']
        self.connections['1И1'] = [[0, -5], self.w1,Const.LEFT]
        self.connections['1И2'] = [[0, -20], self.w1,Const.LEFT]
        self.connections['2И1'] = [[0, -35], self.w2,Const.LEFT]
        self.connections['2И2'] = [[0, -50], self.w2,Const.LEFT]


class CT3(CT2):
    '''Трансформатор тока с тремя вторичными обмотками.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.w3 = GraphWithConnection(highlight=highlight)
        self.w3 += CT_W(name + '-3')
        self.w3.connections['3И1'] = [[0, 0],Const.LEFT]
        self.w3.connections['3И2'] = [[4, 0],Const.RIGHT]
        self.w3.labels += ['3И1', '3И2']
        self.w3.labels_xy += [[-2, -5], [6, -5]]
        self.vertices = [[0, 0], [15, 0], [15, -85], [0, -85], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy += [[5,-65],[5,-80]]
        self.labels += ['3И1', '3И2']
        self.connections['3И1'] = [[0, -65], self.w3,Const.LEFT]
        self.connections['3И2'] = [[0, -80], self.w3,Const.LEFT]


class YA(GraphWithConnection):
    '''Электромагнит управления коммутационным аппаратом.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.w = GraphWithConnection(highlight=highlight)
        self.w += Winding(name)
        self.w.connections[1] = [[0, 0],Const.LEFT]
        self.w.connections[2] = [[15, 0],Const.RIGHT]
        self += Winding(name)
        self.connections[1] = [[0, 0], self.w,Const.LEFT]
        self.connections[2] = [[15, 0], self.w,Const.RIGHT]


class RP23(GraphWithConnection):
    '''Реле промежуточное типа РП-23'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'РП-23'
        self.k1 = GraphWithConnection()
        self.k1 += ContactClose(name, highlight=highlight)
        self.k1.labels += [1, 2]
        self.k1.labels_xy += [[0, 0], [20, 0]]
        self.k1.connections[1] = [[0, 0],Const.LEFT]
        self.k1.connections[2] = [[20, 0],Const.RIGHT]
        self.k2 = GraphWithConnection()
        self.k2 += ContactOpen(name, highlight=highlight)
        self.k2.labels += [3, 4]
        self.k2.labels_xy += [[0, 0], [20, 0]]
        self.k2.connections[3] = [[0, 0],Const.LEFT]
        self.k2.connections[4] = [[20, 0],Const.RIGHT]
        self.k3 = GraphWithConnection()
        self.k3 += ContactOpen(name, highlight=highlight)
        self.k3.labels += [5, 6]
        self.k3.labels_xy += [[0, 0], [20, 0]]
        self.k3.connections[5] = [[0, 0],Const.LEFT]
        self.k3.connections[6] = [[20, 0],Const.RIGHT]
        self.k4 = GraphWithConnection()
        self.k4 += ContactOpen(name, highlight=highlight)
        self.k4.labels += [7, 8]
        self.k4.labels_xy += [[0, 0], [20, 0]]
        self.k4.connections[7] = [[0, 0],Const.LEFT]
        self.k4.connections[8] = [[20, 0],Const.RIGHT]
        self.k5 = GraphWithConnection()
        self.k5 += ContactOpen(name, highlight=highlight)
        self.k5.labels += [9, 10]
        self.k5.labels_xy += [[0, 0], [20, 0]]
        self.k5.connections[9] = [[0, 0],Const.LEFT]
        self.k5.connections[10] = [[20, 0],Const.RIGHT]
        self.w = GraphWithConnection()
        self.w += Winding(name, highlight=highlight)
        self.w.labels += [11, 12]
        self.w.labels_xy += [[0, 0], [15, 0]]
        self.w.connections[11] = [[0, 0],Const.LEFT]
        self.w.connections[12] = [[15, 0],Const.RIGHT]
        self.vertices += [[0, 0], [20, 0], [20, -75], [0, -75], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += [self.type, name]
        self.labels_xy += [[10, -4], [10, 0]]
        k = ContactClose(highlight=highlight)
        k.mov_to(0, -10)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -20)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -30)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -40)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -50)
        self += k
        w = Winding(highlight=highlight)
        w.mov_to(2.5, -60)
        self += w
        self.connections[1] = [[0, -10], self.k1,Const.LEFT]
        self.connections[2] = [[20, -10], self.k1,Const.RIGHT]
        self.connections[3] = [[20, -20], self.k2,Const.RIGHT]
        self.connections[4] = [[0, -20], self.k2,Const.LEFT]
        self.connections[5] = [[20, -30], self.k3,Const.RIGHT]
        self.connections[6] = [[20, -30], self.k3,Const.RIGHT]
        self.connections[7] = [[0, -40], self.k4,Const.LEFT]
        self.connections[8] = [[20, -40], self.k4,Const.RIGHT]
        self.connections[9] = [[20, -50], self.k5,Const.LEFT]
        self.connections[10] = [[20, -50], self.k5,Const.RIGHT]
        self.connections[11] = [[0, -60], self.w,Const.LEFT]
        self.connections[12] = [[20, -60], self.w,Const.RIGHT]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 3 if value[0][0] == 0 else -3
            self.labels_xy += [[value[0][0] + dx, value[0][1]]]


class RP25(RP23):
    '''Реле промежуточное типа РП-25'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'РП-25'


class XT(GraphWithConnection):
    '''Клеммник'''

    def __init__(self, name='', quantity=50, type='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.__type = type
        self.n = [None]
        self.list_jampers = []
        h = 6
        for i in range(1, quantity + 1):
            self.n.append(ConnectionTerminal(i, highlight=highlight))
            self.n[-1].labels += [name]
            self.n[-1].labels_xy += [[-1,-1,MTEXT_TOP_RIGHT]]
            self.connections[i] = [[0, -i * h - 3], self.n[-1],Const.LEFT]
            self.connections[-i] = [[20, -i * h - 3], self.n[-1],Const.RIGHT]
            self.vertices += [[0, -i * h], [20, -i * h], [20, -i * h - h], [0, -i * h - h], [0, -i * h]]
            self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
            self.labels += [i]
            self.labels_xy += [[10, -i * h - h + 1]]
        self.labels += [name]
        self.labels_xy += [[10, 0]]

    def add_jumper(self, list_jampers):
        self.list_jampers += list_jampers

    @property
    def jampers(self):
        wires = []
        for j in self.list_jampers:
            wires.append(Wire(self,j[0],self,j[1]))
        return wires


class RP361(GraphWithConnection):
    '''Реле РП-361'''

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
        self.k2_4_6.connections[2] = [[0, 0],Const.LEFT]
        self.k2_4_6.connections[4] = [[20, 0],Const.RIGHT]
        self.k2_4_6.connections[6] = [[0, 20],Const.LEFT]
        self.k2_4_6.labels += [2, 4, 6]
        self.k2_4_6.labels_xy += [[0, -4], [20, -4], [0, 16]]
        self.w8_14 = GraphWithConnection(highlight=highlight)
        self.w8_14 += Winding(name)
        self.w8_14.connections[8] = [[0, 0],Const.LEFT]
        self.w8_14.connections[14] = [[15, 0],Const.RIGHT]
        self.w8_14.labels += [8, 14]
        self.w8_14.labels_xy += [[0, -4], [15, -4]]
        self.vertices = [[0, 0], [20, 0], [20, -70], [0, -70], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels = [name, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'РП-361']
        self.labels_xy = [[10, 0], [17, -7], [3, -7], [17, -17], [3, -17], [17, -27], [3, -27], [17, -37], [3, -37],
                          [17, -47], [3, -47],
                          [17, -57], [3, -57], [17, -67], [3, -67], [10, -5]]
        self.connections[1] = [[20, -5], self.k2_4_6,Const.RIGHT]
        self.connections[2] = [[0, -5], self.k2_4_6,Const.LEFT]
        self.connections[3] = [[20, -15], self.k2_4_6,Const.RIGHT]
        self.connections[4] = [[0, -15], self.k2_4_6,Const.LEFT]
        self.connections[5] = [[20, -25], self.k2_4_6,Const.RIGHT]
        self.connections[6] = [[0, -25], self.k2_4_6,Const.LEFT]
        self.connections[7] = [[30, -35], self.k2_4_6,Const.RIGHT]
        self.connections[8] = [[0, -35], self.w8_14,Const.LEFT]
        self.connections[9] = [[30, -45], self.k2_4_6,Const.RIGHT]
        self.connections[10] = [[0, -45], self.k2_4_6,Const.LEFT]
        self.connections[11] = [[30, -55], self.k2_4_6,Const.RIGHT]
        self.connections[12] = [[0, -55], self.k2_4_6,Const.LEFT]
        self.connections[13] = [[30, -65], self.k2_4_6,Const.RIGHT]
        self.connections[14] = [[0, -65], self.w8_14,Const.LEFT]


class BPT615(GraphWithConnection):
    '''Блок питания БПТ-615 производства ОАО "БЭМН" г.Минск.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k1_2 = GraphWithConnection(highlight=highlight)
        self.k1_2 += Winding(name)
        self.k1_2.connections[2] = [[0, 0],Const.LEFT]
        self.k1_2.connections[1] = [[15, 0],Const.RIGHT]
        self.k1_2.labels += [2, 1]
        self.k1_2.labels_xy += [[0, -4], [15, -4]]
        self.k3_4 = GraphWithConnection(highlight=highlight)
        self.k3_4 += Winding(name)
        self.k3_4.connections[4] = [[0, 0],Const.LEFT]
        self.k3_4.connections[3] = [[15, 0],Const.RIGHT]
        self.k3_4.labels += [4, 3]
        self.k3_4.labels_xy += [[0, -4], [15, -4]]
        self.vertices = [[0, 0], [20, 0], [20, -120], [0, -120], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels = [name, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 'БПТ-615']
        self.labels_xy = [[10, 0], [17, -65], [17, -55], [17, -45], [17, -35], [3, -115], [3, -105], [3, -95], [3, -85],
                          [3, -75], [3, -65], [3, -55], [3, -45], [3, -35], [3, -25], [3, -15], [3, -5], [15, -5]]
        self.connections[1] = [[20, -65], self.k1_2,Const.RIGHT]
        self.connections[2] = [[20, -55], self.k1_2,Const.RIGHT]
        self.connections[3] = [[20, -45], self.k3_4,Const.RIGHT]
        self.connections[4] = [[20, -35], self.k3_4,Const.RIGHT]
        self.connections[5] = [[0, -115], self.k1_2,Const.LEFT]
        self.connections[6] = [[0, -105], self.k1_2,Const.LEFT]
        self.connections[7] = [[0, -95], self.k3_4,Const.LEFT]
        self.connections[8] = [[0, -85], self.k3_4,Const.LEFT]
        self.connections[9] = [[0, -75], self.k1_2,Const.LEFT]
        self.connections[10] = [[0, -65], self.k1_2,Const.LEFT]
        self.connections[11] = [[0, -55], self.k3_4,Const.LEFT]
        self.connections[12] = [[0, -45], self.k3_4,Const.LEFT]
        self.connections[13] = [[0, -35], self.k1_2,Const.LEFT]
        self.connections[14] = [[0, -25], self.k1_2,Const.LEFT]
        self.connections[15] = [[0, -15], self.k3_4,Const.LEFT]
        self.connections[16] = [[0, -5], self.k3_4,Const.LEFT]


class MR5PO50(GraphWithConnection):
    '''Класс для описания микропроцессорного реле МР5ПО50 производства ОАО "БЭМН" г.Минск.'''

    def __init__(self, name='', highlight=False):
        '''Конструктор класса МР5ПО50.'''
        super().__init__(name, highlight)
        self.x8 = GraphWithConnection(highlight=highlight)
        self.x8.vertices += [[0, 0], [25, 0], [25, -150], [0, -150], [0, 0]]
        self.x8.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.x8.connections['X8:1'] = [[0, -12],Const.LEFT]
        self.x8.connections['X8:2'] = [[25, -12],Const.RIGHT]
        self.x8.connections['X8:4'] = [[0, -37],Const.LEFT]
        self.x8.connections['X8:5'] = [[25, -37],Const.RIGHT]
        self.x8.connections['X8:7'] = [[0, -62],Const.LEFT]
        self.x8.connections['X8:8'] = [[25, -62],Const.RIGHT]
        self.x8.connections['X8:10'] = [[0, -112],Const.LEFT]
        self.x8.connections['X8:11'] = [[0, -137],Const.LEFT]
        self.x8.connections['X8:12'] = [[25, -112],Const.RIGHT]
        self.x8.labels += [name, 'X8:1', 'X8:2', 'X8:4', 'X8:5', 'X8:7', 'X8:8', 'X8:10', 'X8:11', 'X8:12', 'Ia', 'Ib',
                           'Ic', 'In']
        self.x8.labels_xy += [[12, 5], [5, -14], [20, -14], [5, -39], [20, -39], [5, -64], [20, -64], [5, -114],
                              [20, -139], [20, -114],
                              [12, -10], [12, -35], [12, -60], [12, -110]]
        self.x2_1_2 = GraphWithConnection(highlight=highlight)
        self.x2_1_2 += ContactClose('Рн')
        self.x2_1_2.labels += ['X2:1', 'X2:2']
        self.x2_1_2.labels_xy += [[0, -4], [20, -4]]
        self.x2_1_2.connections['X2:1'] = [[0, 0],Const.LEFT]
        self.x2_1_2.connections['X2:2'] = [[20, 0],Const.RIGHT]
        self.x2_3_4 = GraphWithConnection(highlight=highlight)
        self.x2_3_4 += ContactOpen('Рвкл')
        self.x2_3_4.labels += ['X2:3', 'X2:4']
        self.x2_3_4.labels_xy += [[0, -4], [20, -4]]
        self.x2_3_4.connections['X2:3'] = [[0, 0],Const.LEFT]
        self.x2_3_4.connections['X2:4'] = [[20, 0],Const.RIGHT]
        self.x2_5_6 = GraphWithConnection(highlight=highlight)
        self.x2_5_6 += ContactOpen('Роткл1')
        self.x2_5_6.labels += ['X2:5', 'X2:6']
        self.x2_5_6.labels_xy += [[0, -4], [20, -4]]
        self.x2_5_6.connections['X2:5'] = [[0, 0],Const.LEFT]
        self.x2_5_6.connections['X2:6'] = [[20, 0],Const.RIGHT]
        self.x2_7_8 = GraphWithConnection(highlight=highlight)
        self.x2_7_8 += ContactOpen('Роткл2')
        self.x2_7_8.labels += ['X2:7', 'X2:8']
        self.x2_7_8.labels_xy += [[0, -4], [20, -4]]
        self.x2_7_8.connections['X2:7'] = [[0, 0],Const.LEFT]
        self.x2_7_8.connections['X2:8'] = [[20, 0],Const.RIGHT]
        self.x1_1_2 = GraphWithConnection(highlight=highlight)
        self.x1_1_2 += Power(name)
        self.x1_1_2.labels += ['Uп', 'X1:1', 'X1:2']
        self.x1_1_2.labels_xy += [[10, 0], [0, -4], [20, -4]]
        self.x1_1_2.connections['X1:1'] = [[0, 0],Const.LEFT]
        self.x1_1_2.connections['X1:2'] = [[20, 0],Const.RIGHT]
        self.x4 = []
        self.x5 = []
        self.x6 = []
        for i in range(8):
            self.x4.append(GraphWithConnection(highlight=highlight))
            self.x4[i] += ContactOpen(name + 'Р' + str(i + 1))
            self.x4[i].labels += ['X4:' + str(i * 2 + 1), 'X4:' + str(i * 2 + 2)]
            self.x4[i].labels_xy += [[0, -2],[20,-2]]
            self.x4[i].connections['X4:' + str(i * 2 + 1)] = [[0,0], Const.LEFT]
            self.x4[i].connections['X4:' + str(i * 2 + 2)] = [[20, 0],Const.RIGHT]
            self.connections['X4:' + str(i * 2 + 1)] = [[0, -225 - i * 20], self.x4[i],Const.LEFT]
            self.connections['X4:' + str(i * 2 + 2)] = [[0, -235 - i * 20], self.x4[i],Const.LEFT]
            self.x5.append(GraphWithConnection(highlight=highlight))
            self.x5[i] += Power(name + 'Д' + str(i + 1),highlight=highlight)
            self.x5[i].labels += ['X5:' + str(i * 2 + 1), 'X5:' + str(i * 2 + 2)]
            self.x5[i].labels_xy += [[0, -2],[20,-2]]
            self.x5[i].connections['X5:' + str(i * 2 + 1)] = [[0,0], Const.LEFT]
            self.x5[i].connections['X5:' + str(i * 2 + 2)] = [[20, 0],Const.RIGHT]
            self.connections['X5:' + str(i * 2 + 1)] = [[25, -225 - i * 20], self.x5[i],Const.RIGHT]
            self.connections['X5:' + str(i * 2 + 2)] = [[25, -235 - i * 20], self.x5[i],Const.RIGHT]
            self.x6.append(GraphWithConnection(highlight=highlight))
            self.x6[i] += Power(name + 'Д' + str(i + 9),highlight=highlight)
            self.x6[i].labels += ['X6:' + str(i * 2 + 9), 'X6:' + str(i * 2 + 10)]
            self.x6[i].labels_xy += [[0, -2],[20,-2]]
            self.x6[i].connections['X6:' + str(i * 2 + 9)] = [[0,0], Const.LEFT]
            self.x6[i].connections['X6:' + str(i * 2 + 10)] = [[20, 0],Const.RIGHT]
            self.connections['X6:' + str(i * 2 + 9)] = [[25, -5 - i * 20], self.x6[i],Const.RIGHT]
            self.connections['X6:' + str(i * 2 + 10)] = [[25, -15 - i * 20], self.x6[i],Const.RIGHT]
        self.connections['X1:1'] = [[0, -195], self.x1_1_2,Const.LEFT]
        self.connections['X1:2'] = [[0, -205], self.x1_1_2,Const.LEFT]
        self.connections['X2:1'] = [[0, -105], self.x2_1_2,Const.LEFT]
        self.connections['X2:2'] = [[0, -115], self.x2_1_2,Const.LEFT]
        self.connections['X2:3'] = [[0, -125], self.x2_3_4,Const.LEFT]
        self.connections['X2:4'] = [[0, -135], self.x2_3_4,Const.LEFT]
        self.connections['X2:5'] = [[0, -145], self.x2_5_6,Const.LEFT]
        self.connections['X2:6'] = [[0, -155], self.x2_5_6,Const.LEFT]
        self.connections['X2:7'] = [[0, -165], self.x2_7_8,Const.LEFT]
        self.connections['X2:8'] = [[0, -175], self.x2_7_8,Const.LEFT]
        self.connections['X8:1'] = [[0, -5], self.x8,Const.LEFT]
        self.connections['X8:2'] = [[0, -15], self.x8,Const.LEFT]
        self.connections['X8:4'] = [[0, -25], self.x8,Const.LEFT]
        self.connections['X8:5'] = [[0, -35], self.x8,Const.LEFT]
        self.connections['X8:7'] = [[0, -45], self.x8,Const.LEFT]
        self.connections['X8:8'] = [[0, -55], self.x8,Const.LEFT]
        self.connections['X8:10'] = [[0, -65], self.x8,Const.LEFT]
        self.connections['X8:11'] = [[0, -75], self.x8,Const.LEFT]
        self.connections['X8:12'] = [[0, -85], self.x8,Const.LEFT]
        self.vertices += [[0,5],[25,5],[25,-380],[0,-380],[0,5]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += [name, 'МР5ПО50']
        self.labels_xy += [[12,5], [12,0]]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 4 if value[0][0] == 0 else -4
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


class BB_TEL10(GraphWithConnection):
    '''Вакуумный выключатель BB/TEL-10'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.sf1 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name+'-SF1')
        self.sf1 += k
        self.sf1.labels += [1,2]
        self.sf1.labels_xy += [[0,-1,MTEXT_TOP_CENTER],[20,-1,MTEXT_TOP_CENTER]]
        self.sf1.connections[1] = [[0, 0],Const.LEFT]
        self.sf1.connections[2] = [[20, 0],Const.RIGHT]
        self.sf2 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name + '-SF2')
        self.sf2 += k
        self.sf2.labels += [3, 4]
        self.sf2.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf2.connections[3] = [[0, 0],Const.LEFT]
        self.sf2.connections[4] = [[20, 0],Const.RIGHT]
        self.sf3 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name + '-SF3')
        self.sf3 += k
        self.sf3.labels += [5, 6]
        self.sf3.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf3.connections[5] = [[0, 0],Const.LEFT]
        self.sf3.connections[6] = [[20, 0],Const.RIGHT]
        self.sf4 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name + '-SF4')
        self.sf4 += k
        self.sf4.labels += [7, 8]
        self.sf4.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf4.connections[7] = [[0, 0],Const.LEFT]
        self.sf4.connections[8] = [[20, 0],Const.RIGHT]
        self.sf5 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name + '-SF5')
        self.sf5 += k
        self.sf5.labels += [9, 10]
        self.sf5.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf5.connections[9] = [[0, 0],Const.LEFT]
        self.sf5.connections[10] = [[20, 0],Const.RIGHT]
        self.sf6 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name + '-SF6')
        self.sf6 += k
        self.sf6.labels += [11, 12]
        self.sf6.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf6.connections[11] = [[0, 0],Const.LEFT]
        self.sf6.connections[12] = [[20, 0],Const.RIGHT]
        self.em = GraphWithConnection(highlight=highlight)
        k = Winding(name + '-ЭМ1')
        self.em += k
        self.em.labels += [13,14]
        self.em.labels_xy += [[0,-1,MTEXT_TOP_CENTER], [15,-1,MTEXT_TOP_CENTER]]
        self.em.connections[13] = [[0, 0],Const.LEFT]
        self.em.connections[14] = [[15, 0],Const.RIGHT]
        self.bk = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-БК')
        self.bk += k
        self.bk.labels += [15, 16]
        self.bk.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.bk.connections[15] = [[0, 0],Const.LEFT]
        self.bk.connections[16] = [[20, 0],Const.RIGHT]
        self.sf7 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF7')
        self.sf7 += k
        self.sf7.labels += [17, 18]
        self.sf7.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf7.connections[17] = [[0, 0],Const.LEFT]
        self.sf7.connections[18] = [[20, 0],Const.RIGHT]
        self.sf8 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF8')
        self.sf8 += k
        self.sf8.labels += [19, 20]
        self.sf8.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf8.connections[19] = [[0, 0],Const.LEFT]
        self.sf8.connections[20] = [[20, 0],Const.RIGHT]
        self.sf9 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF9')
        self.sf9 += k
        self.sf9.labels += [21, 22]
        self.sf9.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf9.connections[21] = [[0, 0],Const.LEFT]
        self.sf9.connections[22] = [[20, 0],Const.RIGHT]
        self.sf10 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF10')
        self.sf10 += k
        self.sf10.labels += [23, 24]
        self.sf10.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf10.connections[23] = [[0, 0],Const.LEFT]
        self.sf10.connections[24] = [[20, 0],Const.RIGHT]
        self.sf11 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF11')
        self.sf11 += k
        self.sf11.labels += [25, 26]
        self.sf11.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf11.connections[25] = [[0, 0],Const.LEFT]
        self.sf11.connections[26] = [[20, 0],Const.RIGHT]
        self.sf12 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF12')
        self.sf12 += k
        self.sf12.labels += [27, 28]
        self.sf12.labels_xy += [[0, -1, MTEXT_TOP_CENTER], [20, -1, MTEXT_TOP_CENTER]]
        self.sf12.connections[27] = [[0, 0],Const.LEFT]
        self.sf12.connections[28] = [[20, 0],Const.RIGHT]
        self.connections[1] = [[0, -10], self.sf1,Const.LEFT]
        self.connections[2] = [[0, -20], self.sf1,Const.LEFT]
        self.connections[3] = [[0, -30], self.sf2,Const.LEFT]
        self.connections[4] = [[0, -40], self.sf2,Const.LEFT]
        self.connections[5] = [[0, -50], self.sf3,Const.LEFT]
        self.connections[6] = [[0, -60], self.sf3,Const.LEFT]
        self.connections[7] = [[0, -70], self.sf4,Const.LEFT]
        self.connections[8] = [[0, -80], self.sf4,Const.LEFT]
        self.connections[9] = [[0, -90], self.sf5,Const.LEFT]
        self.connections[10] = [[0, -100], self.sf5,Const.LEFT]
        self.connections[11] = [[0, -110], self.sf6,Const.LEFT]
        self.connections[12] = [[0, -120], self.sf6,Const.LEFT]
        self.connections[13] = [[0, -130], self.em,Const.LEFT]
        self.connections[14] = [[0, -140], self.em,Const.LEFT]
        self.connections[15] = [[20, -10], self.bk,Const.RIGHT]
        self.connections[16] = [[20, -20], self.bk,Const.RIGHT]
        self.connections[17] = [[20, -30], self.sf7,Const.RIGHT]
        self.connections[18] = [[20, -40], self.sf7,Const.RIGHT]
        self.connections[19] = [[20, -50], self.sf8,Const.RIGHT]
        self.connections[20] = [[20, -60], self.sf8,Const.RIGHT]
        self.connections[21] = [[20, -70], self.sf9,Const.RIGHT]
        self.connections[22] = [[20, -80], self.sf9,Const.RIGHT]
        self.connections[23] = [[20, -90], self.sf10,Const.RIGHT]
        self.connections[24] = [[20, -100], self.sf10,Const.RIGHT]
        self.connections[25] = [[20, -110], self.sf11,Const.RIGHT]
        self.connections[26] = [[20, -120], self.sf11,Const.RIGHT]
        self.connections[27] = [[20, -130], self.sf12,Const.RIGHT]
        self.connections[28] = [[20, -140], self.sf12,Const.RIGHT]
        self.vertices += [[0, 0], [20, 0], [20, -145], [0, -145], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += [name, 'BB/TEL-10']
        self.labels_xy += [[10, 0], [10, -5],]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 4 if value[0][0] == 0 else -4
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


class PS7(GraphWithConnection):
    '''Панель сигнальная ПС7 Сиинтез-Электро.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'ПС-7'
        self.vertices += [[5,0],[185,0],[185,-20],[5,-20],[5,0]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.l_bi = []
        for i in range(7):
            self.l_bi.append(GraphWithConnection(name, highlight=highlight))
            self.l_bi[-1] += BI('Вход ' + str(i+1), highlight=highlight)
            self.l_bi[-1].labels += [name, i * 2 + 5, i * 2 + 6]
            self.l_bi[-1].labels_xy += [[10,2],[0, -2],[20,-2]]
            self.l_bi[-1].connections[i * 2 + 5] = [[0,0], Const.LEFT]
            self.l_bi[-1].connections[i * 2 + 6] = [[20, 0],Const.RIGHT]
            self.connections[i * 2 + 5] = [[i*20 + 50,-20], self.l_bi[-1], Const.DOWN]
            self.connections[i * 2 + 6] = [[i*20 + 60,-20], self.l_bi[-1], Const.DOWN]
            self.labels += ['Вход ' + str(i+1), i * 2 + 5, i * 2 + 6]
            self.labels_xy += [[i*20 + 55,-12],[i*20 + 50,-18],[i*20 + 60,-18]]
        self.p = GraphWithConnection(highlight=highlight)
        self.p += Power('Сеть',highlight=highlight)
        self.p.labels += [name, 1, 2]
        self.p.labels_xy += [[10,6], [0,0],[20,0]]
        self.p.connections[1] = [[0,0], Const.LEFT]
        self.p.connections[2] = [[20, 0],Const.RIGHT]
        self.connections[1] = [[10,-20],self.p,Const.DOWN]
        self.connections[2] = [[20, -20], self.p, Const.DOWN]
        self.labels += ['Сеть',1,2]
        self.labels_xy += [[15,-12],[10,-18],[20,-18]]
        self.r = GraphWithConnection()
        self.r += ContactOpen('Реле', highlight=highlight)
        self.r.labels += [name, 3, 4]
        self.r.labels_xy += [[10, 6,MTEXT_BOTTOM_CENTER], [0, -1,MTEXT_TOP_CENTER], [20, -1,MTEXT_TOP_CENTER]]
        self.r.connections[3] = [[0, 0],Const.LEFT]
        self.r.connections[4] = [[20, 0],Const.RIGHT]
        self.connections[3] = [[30, -20], self.r, Const.DOWN]
        self.connections[4] = [[40, -20], self.r, Const.DOWN]
        self.labels += [self.type,name,'Реле',3, 4]
        self.labels_xy += [[95,-5],[95,0],[35,-12],[30, -18], [40, -18]]


class BU_TEL(GraphWithConnection):
    '''Блок управления BU/TEL-220-05A выключателем BB/TEL-10'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Блок управления BU/TEL-220-05A выключателем BB/TEL-10'
        self.xt1_9 = GraphWithConnection(highlight=highlight)
        self.xt1_9.vertices += [[0,0], [20,0],[20,-100],[0,-100],[0,0]]
        self.xt1_9.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.xt1_9.labels += [name,'1 +220','2 -220', '3 ЭМ1','4 ЭМ2','5 БК1','6 БК2','7 ВО',
                              '8 ВКЛ','9 ОТКЛ']
        self.xt1_9.labels_xy += [[10,1,MTEXT_BOTTOM_CENTER],[3,-10,MTEXT_MIDDLE_LEFT],[3,-20,MTEXT_MIDDLE_LEFT],[3,-30,MTEXT_MIDDLE_LEFT],
                                 [3,-40,MTEXT_MIDDLE_LEFT],[3,-50,MTEXT_MIDDLE_LEFT],[3,-60,MTEXT_MIDDLE_LEFT],[3,-70,MTEXT_MIDDLE_LEFT],
                                 [3,-80,MTEXT_MIDDLE_LEFT],[3,-90,MTEXT_MIDDLE_LEFT]]
        self.xt1_9.connections[1] = [[0,-10], Const.LEFT]
        self.xt1_9.connections[2] = [[0, -20],Const.LEFT]
        self.xt1_9.connections[3] = [[0, -30],Const.LEFT]
        self.xt1_9.connections[4] = [[0, -40],Const.LEFT]
        self.xt1_9.connections[5] = [[0, -50],Const.LEFT]
        self.xt1_9.connections[6] = [[0, -60],Const.LEFT]
        self.xt1_9.connections[7] = [[0, -70],Const.LEFT]
        self.xt1_9.connections[8] = [[0, -80],Const.LEFT]
        self.xt1_9.connections[9] = [[0, -90],Const.LEFT]
        self.tta = GraphWithConnection(highlight=highlight)
        self.tta += BI('TTA')
        self.tta.labels += [name, 10,11]
        self.tta.labels_xy += [[10,6,MTEXT_BOTTOM_CENTER],[0,-1,MTEXT_TOP_RIGHT],[20,-1,MTEXT_TOP_LEFT]]
        self.tta.connections[10] = [[0,0],Const.LEFT]
        self.tta.connections[11] = [[20, 0],Const.RIGHT]
        self.ttc = GraphWithConnection(highlight=highlight)
        self.ttc += BI('TTC')
        self.ttc.labels += [name, 12, 13]
        self.ttc.labels_xy += [[10,6,MTEXT_BOTTOM_CENTER],[0,-1,MTEXT_TOP_RIGHT],[20,-1,MTEXT_TOP_LEFT]]
        self.ttc.connections[12] = [[0, 0],Const.LEFT]
        self.ttc.connections[13] = [[20, 0],Const.RIGHT]
        self.connections[1] = [[0,-10],self.xt1_9,Const.LEFT]
        self.connections[2] = [[0, -20], self.xt1_9,Const.LEFT]
        self.connections[3] = [[0, -30], self.xt1_9,Const.LEFT]
        self.connections[4] = [[0, -40], self.xt1_9,Const.LEFT]
        self.connections[5] = [[0, -50], self.xt1_9,Const.LEFT]
        self.connections[6] = [[0, -60], self.xt1_9,Const.LEFT]
        self.connections[7] = [[0, -70], self.xt1_9,Const.LEFT]
        self.connections[8] = [[0, -80], self.xt1_9,Const.LEFT]
        self.connections[9] = [[0, -90], self.xt1_9,Const.LEFT]
        self.connections[10] = [[0, -100], self.tta,Const.LEFT]
        self.connections[11] = [[0, -110], self.tta,Const.LEFT]
        self.connections[12] = [[0, -120], self.ttc,Const.LEFT]
        self.connections[13] = [[0, -130], self.ttc,Const.LEFT]
        self.vertices += [[0,0],[35,0],[35,-135],[0,-135],[0,0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += [name, 'BU/TEL-220-05A',' 1 +220', ' 2 -220', ' 3 ЭМ1 ', ' 4 ЭМ2 ', ' 5 БК1 ', ' 6 БК2 ',
                        ' 7 ВО   ', ' 8 ВКЛ ', ' 9 ОТКЛ', '10 TTA1','11 TTA2','12 TTC1','13 TTC2']
        self.labels_xy += [[17, 1,MTEXT_BOTTOM_CENTER], [17,-5],[1, -10, MTEXT_BOTTOM_LEFT], [1, -20, MTEXT_BOTTOM_LEFT], [1, -30, MTEXT_BOTTOM_LEFT],
                           [1, -40, MTEXT_BOTTOM_LEFT], [1, -50, MTEXT_BOTTOM_LEFT], [1, -60, MTEXT_BOTTOM_LEFT], [1, -70, MTEXT_BOTTOM_LEFT],
                [1, -80, MTEXT_BOTTOM_LEFT], [1, -90, MTEXT_BOTTOM_LEFT],[1,-100, MTEXT_BOTTOM_LEFT],[1,-110, MTEXT_BOTTOM_LEFT],[1,-120, MTEXT_BOTTOM_LEFT],[1,-130, MTEXT_BOTTOM_LEFT]]


class BP_TEL(GraphWithConnection):
    '''Блок питания BP/TEL-220-02A выключателя BB/TEL-10'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.description = 'Блок питания BP/TEL-220-02A выключателя BB/TEL-10'
        self.type = 'BP/TEL-220-02A'
        self.bp = GraphWithConnection(highlight=highlight)
        self.bp.vertices += [[0, 0], [20, 0], [20, -65], [0, -65], [0, 0]]
        self.bp.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.bp.labels += [name, '14 ~220', '15 ~220', '+220 8', '+220 9', '-220 5', '-220 6']
        self.bp.labels_xy += [[10, 1,MTEXT_BOTTOM_CENTER], [2, -12,MTEXT_BOTTOM_LEFT], [2, -22,MTEXT_BOTTOM_LEFT], [18, -32,MTEXT_BOTTOM_RIGHT],
                                 [18, -42,MTEXT_BOTTOM_RIGHT], [18, -52,MTEXT_BOTTOM_RIGHT], [18, -62,MTEXT_BOTTOM_RIGHT]]
        self.bp.connections[14] = [[0, -10],Const.LEFT]
        self.bp.connections[15] = [[0, -20],Const.LEFT]
        self.bp.connections[8] = [[20, -30],Const.RIGHT]
        self.bp.connections[9] = [[20, -40],Const.RIGHT]
        self.bp.connections[5] = [[20, -50],Const.RIGHT]
        self.bp.connections[6] = [[20, -60],Const.RIGHT]
        self.bp12 = GraphWithConnection(highlight=highlight)
        self.bp12.vertices += [[0, 0], [20, 0], [20, -25], [0, -25], [0, 0]]
        self.bp12.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.bp12.labels += [name, '-12В 11', '+12В 12']
        self.bp12.labels_xy += [[10, 1,MTEXT_BOTTOM_CENTER], [19, -10,MTEXT_MIDDLE_RIGHT], [19, -20,MTEXT_MIDDLE_RIGHT]]
        self.bp12.connections[11] = [[20, -10],Const.RIGHT]
        self.bp12.connections[12] = [[20, -20],Const.RIGHT]
        self.k = GraphWithConnection()
        self.k += ContactOpenClose(name, highlight=highlight)
        self.k.labels += [18, 17, 16]
        self.k.labels_xy += [[0, 0], [20, 7], [20, 0]]
        self.k.connections[18] = [[0, 0],Const.LEFT]
        self.k.connections[17] = [[20, 10],Const.RIGHT]
        self.k.connections[16] = [[20, 0],Const.RIGHT]
        self.connections[5] = [[0, -10], self.bp,Const.LEFT]
        self.connections[6] = [[0, -20], self.bp,Const.LEFT]
        self.connections[8] = [[0, -30], self.bp,Const.LEFT]
        self.connections[9] = [[0, -40], self.bp,Const.LEFT]
        self.connections[11] = [[0, -50], self.bp12,Const.LEFT]
        self.connections[12] = [[0, -60], self.bp12,Const.LEFT]
        self.connections[14] = [[0, -70], self.bp,Const.LEFT]
        self.connections[15] = [[0, -80], self.bp,Const.LEFT]
        self.connections[16] = [[0, -90], self.k,Const.LEFT]
        self.connections[17] = [[0, -100], self.k,Const.LEFT]
        self.connections[18] = [[0, -110], self.k,Const.LEFT]
        self.vertices += [[0, 0], [35, 0], [35, -115], [0, -115], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += [name, 'BP/TEL-220-02A', ' 5 -220', ' 6 -220', ' 8 +220', ' 9 +220', '11 -12В', '12 +12В',
                        '14 ~220В', '15 ~220В', '16 Конт.Uвых 3', '17 Конт.Uвых 1', '18 Конт.Uвых 2']
        self.labels_xy += [[17, 0], [17, -5], [1, -10, MTEXT_BOTTOM_LEFT], [1, -20, MTEXT_BOTTOM_LEFT], [1, -30, MTEXT_BOTTOM_LEFT],
                           [1, -40, MTEXT_BOTTOM_LEFT], [1, -50, MTEXT_BOTTOM_LEFT], [1, -60, MTEXT_BOTTOM_LEFT], [1, -70, MTEXT_BOTTOM_LEFT],
                           [1, -80, MTEXT_BOTTOM_LEFT], [1, -90, MTEXT_BOTTOM_LEFT], [1, -100, MTEXT_BOTTOM_LEFT], [1, -110, MTEXT_BOTTOM_LEFT]]


class MR500_V2(GraphWithConnection):
    '''Класс для описания микропроцессорного реле МР500 версии до 3.0 производства ОАО "БЭМН" г.Минск.'''

    def __init__(self, name='', highlight=False):
        '''Конструктор класса МР5О0 версии до 3.0.'''
        super().__init__(name, highlight)
        self.type = 'МР500 v.2'
        self.x6 = GraphWithConnection(highlight=highlight)
        self.x6.vertices += [[0, 0], [25, 0], [25, -70], [0, -70], [0, 0]]
        self.x6.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.x6.connections['X6:1'] = [[0, -12],Const.LEFT]
        self.x6.connections['X6:2'] = [[25, -12],Const.RIGHT]
        self.x6.connections['X6:4'] = [[0, -37],Const.LEFT]
        self.x6.connections['X6:5'] = [[25, -37],Const.RIGHT]
        self.x6.connections['X6:7'] = [[0, -62],Const.LEFT]
        self.x6.connections['X6:8'] = [[25, -62],Const.RIGHT]
        self.x6.labels += [name, self.type, 'X6:1', 'X6:2', 'X6:4', 'X6:5', 'X6:7', 'X6:8', 'Ia', 'Ib', 'Ic']
        self.x6.labels_xy += [[12, 5], [12,-1,MTEXT_TOP_CENTER], [5, -14], [20, -14], [5, -39], [20, -39], [5, -64], [20, -64], [12, -12],
                              [12, -37], [12, -62]]
        self.x2_1_2 = GraphWithConnection(highlight=highlight)
        self.x2_1_2 += ContactClose('Рн')
        self.x2_1_2.labels += ['X2:1', 'X2:2']
        self.x2_1_2.labels_xy += [[0, -4], [20, -4]]
        self.x2_1_2.connections['X2:1'] = [[0, 0],Const.LEFT]
        self.x2_1_2.connections['X2:2'] = [[20, 0],Const.RIGHT]
        self.x2_3_4 = GraphWithConnection(highlight=highlight)
        self.x2_3_4 += ContactOpen('Рвкл')
        self.x2_3_4.labels += ['X2:3', 'X2:4']
        self.x2_3_4.labels_xy += [[0, -4], [20, -4]]
        self.x2_3_4.connections['X2:3'] = [[0, 0],Const.LEFT]
        self.x2_3_4.connections['X2:4'] = [[20, 0],Const.RIGHT]
        self.x2_5_6 = GraphWithConnection(highlight=highlight)
        self.x2_5_6 += ContactOpen('Роткл1')
        self.x2_5_6.labels += ['X2:5', 'X2:6']
        self.x2_5_6.labels_xy += [[0, -4], [20, -4]]
        self.x2_5_6.connections['X2:5'] = [[0, 0],Const.LEFT]
        self.x2_5_6.connections['X2:6'] = [[20, 0],Const.RIGHT]
        self.x1 = GraphWithConnection(highlight=highlight)
        self.x1 += Power('Uп',highlight=highlight)
        self.x1.labels += [name, 'X1:2', 'X1:3']
        self.x1.labels_xy += [[10, 6,MTEXT_BOTTOM_CENTER], [0, -1,MTEXT_TOP_CENTER], [20, -1,MTEXT_TOP_CENTER]]
        self.x1.connections['X1:2'] = [[0, 0],Const.LEFT]
        self.x1.connections['X1:3'] = [[20, 0],Const.RIGHT]
        self.x7 = []
        self.x8 = []
        self.x9 = []
        for i in range(8):
            self.x7.append(GraphWithConnection(highlight=highlight))
            self.x7[i] += ContactOpen(name + '-Р' + str(i + 1))
            self.x7[i].labels += ['X7:' + str(i * 2 + 1), 'X7:' + str(i * 2 + 2)]
            self.x7[i].labels_xy += [[0, -1,MTEXT_TOP_CENTER],[20,-1,MTEXT_TOP_CENTER]]
            self.x7[i].connections['X7:' + str(i * 2 + 1)] = [[0,0], Const.LEFT]
            self.x7[i].connections['X7:' + str(i * 2 + 2)] = [[20, 0],Const.RIGHT]
            self.connections['X7:' + str(i * 2 + 1)] = [[0, -225 - i * 20], self.x7[i],Const.LEFT]
            self.connections['X7:' + str(i * 2 + 2)] = [[0, -235 - i * 20], self.x7[i],Const.LEFT]
            self.x8.append(GraphWithConnection(highlight=highlight))
            self.x8[i] += Power('Д' + str(i + 1),highlight=highlight)
            self.x8[i].labels += ['X8:' + str(i * 2 + 1), 'X8:' + str(i * 2 + 2),name]
            self.x8[i].labels_xy += [[-1, -1,MTEXT_TOP_CENTER],[21,-1,MTEXT_TOP_CENTER],[10,6,MTEXT_BOTTOM_CENTER]]
            self.x8[i].connections['X8:' + str(i * 2 + 1)] = [[0,0], Const.LEFT]
            self.x8[i].connections['X8:' + str(i * 2 + 2)] = [[20, 0],Const.RIGHT]
            self.connections['X8:' + str(i * 2 + 1)] = [[25, -225 - i * 20], self.x8[i],Const.RIGHT]
            self.connections['X8:' + str(i * 2 + 2)] = [[25, -235 - i * 20], self.x8[i],Const.RIGHT]
            self.x9.append(GraphWithConnection(highlight=highlight))
            self.x9[i] += Power('Д' + str(i + 9),highlight=highlight)
            self.x9[i].labels += ['X9:' + str(i * 2 + 1), 'X9:' + str(i * 2 + 2), name]
            self.x9[i].labels_xy += [[-1, -1,MTEXT_TOP_CENTER],[21,-1,MTEXT_TOP_CENTER],[10,6,MTEXT_BOTTOM_CENTER]]
            self.x9[i].connections['X9:' + str(i * 2 + 1)] = [[0,0], Const.LEFT]
            self.x9[i].connections['X9:' + str(i * 2 + 2)] = [[20, 0],Const.RIGHT]
            self.connections['X9:' + str(i * 2 + 1)] = [[25, -5 - i * 20], self.x9[i],Const.RIGHT]
            self.connections['X9:' + str(i * 2 + 2)] = [[25, -15 - i * 20], self.x9[i],Const.RIGHT]
        self.connections['X1:2'] = [[0, -195], self.x1,Const.LEFT]
        self.connections['X1:3'] = [[0, -205], self.x1,Const.LEFT]
        self.connections['X2:1'] = [[0, -105], self.x2_1_2,Const.LEFT]
        self.connections['X2:2'] = [[0, -115], self.x2_1_2,Const.LEFT]
        self.connections['X2:3'] = [[0, -125], self.x2_3_4,Const.LEFT]
        self.connections['X2:4'] = [[0, -135], self.x2_3_4,Const.LEFT]
        self.connections['X2:5'] = [[0, -145], self.x2_5_6,Const.LEFT]
        self.connections['X2:6'] = [[0, -155], self.x2_5_6,Const.LEFT]
        self.connections['X6:1'] = [[0, -5], self.x6,Const.LEFT]
        self.connections['X6:2'] = [[0, -15], self.x6,Const.LEFT]
        self.connections['X6:4'] = [[0, -25], self.x6,Const.LEFT]
        self.connections['X6:5'] = [[0, -35], self.x6,Const.LEFT]
        self.connections['X6:7'] = [[0, -45], self.x6,Const.LEFT]
        self.connections['X6:8'] = [[0, -55], self.x6,Const.LEFT]
        self.vertices += [[0,5],[25,5],[25,-380],[0,-380],[0,5]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += [name, self.type]
        self.labels_xy += [[12,5], [12,0]]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 4 if value[0][0] == 0 else -4
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


class PS3_old(GraphWithConnection):
    '''Индикатор фаз ПС-3 Синтез-Электро'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Индикатор фаз ПС-3 Синтез-Электро'
        self.k1 = GraphWithConnection()
        self.k1 += ContactOpenClose('K1',highlight=highlight)
        self.k1.labels += [8,7,9]
        self.k1.labels_xy += [[0,0],[20,7],[20,0]]
        self.k1.connections[8] = [[0,0], Const.LEFT]
        self.k1.connections[7] = [[20, 10],Const.RIGHT]
        self.k1.connections[9] = [[20, 0],Const.RIGHT]
        self.k1_1 = GraphWithConnection()
        self.k1_1 += ContactOpenClose('K1',highlight=highlight)
        self.k1_1.labels += [11,12,10]
        self.k1_1.labels_xy += [[0,0],[20,7],[20,0]]
        self.k1_1.connections[11] = [[0,0], Const.LEFT]
        self.k1_1.connections[12] = [[20, 10],Const.RIGHT]
        self.k1_1.connections[10] = [[20, 0],Const.RIGHT]
        self.k2 = GraphWithConnection()
        self.k2 += ContactOpenClose('K2',highlight=highlight)
        self.k2.labels += [14,13,15]
        self.k2.labels_xy += [[0,0],[20,7],[20,0]]
        self.k2.connections[14] = [[0,0], Const.LEFT]
        self.k2.connections[13] = [[20, 10],Const.RIGHT]
        self.k2.connections[15] = [[20, 0],Const.RIGHT]
        self.p = GraphWithConnection()
        self.p += Power('Пит.', highlight=highlight)
        self.p.labels += [5,6]
        self.p.labels_xy += [[0,0],[20,0]]
        self.p.connections[5] = [[0,0], Const.LEFT]
        self.p.connections[6] = [[20, 0],Const.RIGHT]
        self.vertices += [[0,0],[20,0],[20,-105],[0,-105],[0,0],[20,-102],[25,-102]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.MOVETO,Path.LINETO]
        self.labels += ['ПС-3', name, 1,2,3,4]
        self.labels_xy += [[10,-4], [10,0],[2,-81],[2,-92],[2,-103],[18,-103]]
        k = ContactOpenClose('K1', highlight=highlight)
        k.mov_to(0,-30)
        self += k
        k = ContactOpenClose('K1', highlight=highlight)
        k.mov_to(0, -50)
        self += k
        k = ContactOpenClose('K2', highlight=highlight)
        k.mov_to(0, -70)
        self += k
        w= Power('Пит.', highlight=highlight)
        w.mov_to(0, -10)
        self +=w
        c = Capacitor('C1', highlight=highlight)
        c.mov_to(-11,-80)
        self += c
        c = Capacitor('C2', highlight=highlight)
        c.mov_to(-11, -91)
        self += c
        c = Capacitor('C3', highlight=highlight)
        c.mov_to(-11, -102)
        self += c
        g = Ground(highlight=highlight)
        g.mov_to(25,-102)
        self += g
        self.connections[8] = [[0,-30],self.k1, Const.LEFT]
        self.connections[7] = [[20, -20], self.k1,Const.RIGHT]
        self.connections[9] = [[20, -30], self.k1,Const.RIGHT]
        self.connections[11] = [[0, -50], self.k1_1,Const.LEFT]
        self.connections[12] = [[20, -40], self.k1_1,Const.RIGHT]
        self.connections[10] = [[20, -50], self.k1_1,Const.RIGHT]
        self.connections[14] = [[0, -70], self.k2,Const.LEFT]
        self.connections[13] = [[20, -60], self.k2,Const.RIGHT]
        self.connections[15] = [[20, -70], self.k2,Const.RIGHT]
        self.connections[5] = [[0, -10], self.p,Const.LEFT]
        self.connections[6] = [[20, -10], self.p,Const.RIGHT]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 3 if value[0][0] == 0 else -3
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


class DUGA_O(GraphWithConnection):
    '''Регистратор дуговых замыканий ДУГА-О.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Регистратор дуговых замыканий ДУГА-О.'
        self.k1 = GraphWithConnection()
        self.k1 += ContactOpen(name+' Вых.1', highlight=highlight)
        self.k1.labels += [1, 2]
        self.k1.labels_xy += [[0, 0], [20, 0]]
        self.k1.connections[1] = [[0, 0],Const.LEFT]
        self.k1.connections[2] = [[20, 0],Const.RIGHT]
        self.k2 = GraphWithConnection()
        self.k2 += ContactOpen(name+' Вых.2', highlight=highlight)
        self.k2.labels += [3, 4]
        self.k2.labels_xy += [[0, 0], [20, 0]]
        self.k2.connections[3] = [[0, 0],Const.LEFT]
        self.k2.connections[4] = [[20, 0],Const.RIGHT]
        self.k3 = GraphWithConnection()
        self.k3 += ContactOpen(name+' Вых.3', highlight=highlight)
        self.k3.labels += [5, 6]
        self.k3.labels_xy += [[0, 0], [20, 0]]
        self.k3.connections[5] = [[0, 0],Const.LEFT]
        self.k3.connections[6] = [[20, 0],Const.RIGHT]
        self.k4 = GraphWithConnection()
        self.k4 += ContactOpen(name+' Вых.4', highlight=highlight)
        self.k4.labels += [7, 8]
        self.k4.labels_xy += [[0, 0], [20, 0]]
        self.k4.connections[7] = [[0, 0],Const.LEFT]
        self.k4.connections[8] = [[20, 0],Const.RIGHT]
        self.k5 = GraphWithConnection()
        self.k5 += ContactOpen(name+' Вых.5', highlight=highlight)
        self.k5.labels += [9, 10]
        self.k5.labels_xy += [[0, 0], [20, 0]]
        self.k5.connections[9] = [[0, 0],Const.LEFT]
        self.k5.connections[10] = [[20, 0],Const.RIGHT]
        self.k = GraphWithConnection()
        self.k += ContactClose(name + ' Отказ', highlight=highlight)
        self.k.labels += [9, 10]
        self.k.labels_xy += [[0, 0], [20, 0]]
        self.k.connections[11] = [[0, 0],Const.LEFT]
        self.k.connections[12] = [[20, 0],Const.RIGHT]
        self.w = GraphWithConnection()
        self.w += Power(name+' Uн', highlight=highlight)
        self.w.labels += [13, 14]
        self.w.labels_xy += [[0, 0], [20, 0]]
        self.w.connections[13] = [[0, 0],Const.LEFT]
        self.w.connections[14] = [[20, 0],Const.RIGHT]
        self.vertices += [[0, 1], [20, 1], [20, -77], [0, -77], [0, 1]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += ['ДУГА-О', name, 'Вых.1','Вых.2','Вых.3','Вых.4','Вых.5','Отказ']
        self.labels_xy += [[10, -3], [10, 1],[8,-7],[9,-16],[9,-26],[9,-36],[9,-46],[10,-56]]
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -10)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -20)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -30)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -40)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -50)
        self += k
        k = ContactClose(highlight=highlight)
        k.mov_to(0, -60)
        self += k
        w = Power(name='220В',highlight=highlight)
        w.mov_to(0, -71)
        self += w
        self.connections[1] = [[0, -10], self.k1,Const.LEFT]
        self.connections[2] = [[20, -10], self.k1,Const.RIGHT]
        self.connections[3] = [[20, -20], self.k2,Const.RIGHT]
        self.connections[4] = [[0, -20], self.k2,Const.LEFT]
        self.connections[5] = [[20, -30], self.k3,Const.RIGHT]
        self.connections[6] = [[20, -30], self.k3,Const.RIGHT]
        self.connections[7] = [[0, -40], self.k4,Const.LEFT]
        self.connections[8] = [[20, -40], self.k4,Const.RIGHT]
        self.connections[9] = [[0, -50], self.k5,Const.LEFT]
        self.connections[10] = [[20, -50], self.k5,Const.RIGHT]
        self.connections[11] = [[0, -60], self.k,Const.LEFT]
        self.connections[12] = [[20, -60], self.k,Const.RIGHT]
        self.connections[13] = [[0, -70], self.w,Const.LEFT]
        self.connections[14] = [[20, -70], self.w,Const.RIGHT]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 3 if value[0][0] == 0 else -3
            self.labels_xy += [[value[0][0] + dx, value[0][1]]]


class PS12(GraphWithConnection):
    '''Панель сигнальная ПС-12 Сиинтез-Электро.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Панель сигнальная ПС-12 Сиинтез-Электро.'
        self.vertices += [[0, 0], [145, 0], [145, -20], [0, -20], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.l_bi = []
        for i in range(12):
            self.l_bi.append(GraphWithConnection(name, highlight=highlight))
            self.l_bi[-1] += BI('Вход ' + str(i + 1), highlight=highlight)
            self.l_bi[-1].labels += [name, str(i + 1)+'h', str(i + 1)]
            self.l_bi[-1].labels_xy += [[10, 2], [0, -2], [20, -2]]
            self.l_bi[-1].connections[str(i + 1)+'h'] = [[0, 0],Const.LEFT]
            self.l_bi[-1].connections[str(i + 1)] = [[20, 0],Const.RIGHT]
            self.connections[str(i + 1)+'h'] = [[i * 10 + 5, 0], self.l_bi[-1],Const.UP]
            self.connections[str(i + 1)] = [[i * 10 + 5, -20], self.l_bi[-1], Const.DOWN]
            self.labels += ['Вход' + str(i + 1), str(i + 1)+'h', str(i + 1)]
            self.labels_xy += [[i * 10 + 6, -12 if i%2 == 0 else -16], [i * 10 + 6, -4], [i * 10 + 6, -20]]
        self.p = GraphWithConnection(highlight=highlight)
        self.p += Power('Сеть', highlight=highlight)
        self.p.labels += [name, '14h', '14']
        self.p.labels_xy += [[10, 6], [0, 0], [20, 0]]
        self.p.connections['14h'] = [[0, 0],Const.LEFT]
        self.p.connections['14'] = [[20, 0],Const.RIGHT]
        self.connections['14h'] = [[140, 0], self.p,Const.UP]
        self.connections['14'] = [[140, -20], self.p, Const.DOWN]
        self.labels += ['Сеть', '14h', '14']
        self.labels_xy += [[140, -16], [140, -4], [140, -20]]
        self.r = GraphWithConnection()
        self.r += Power('Подсвет', highlight=highlight)
        self.r.labels += [name, '13h', '13']
        self.r.labels_xy += [[5, 6], [0, 0], [20, 0]]
        self.r.connections['13h'] = [[0, 0],Const.LEFT]
        self.r.connections['13'] = [[20, 0],Const.RIGHT]
        self.connections['13h'] = [[130, 0], self.r,Const.UP]
        self.connections['13'] = [[130, -20], self.r, Const.DOWN]
        self.labels += ['ПС-12', name, 'Подсвет', '13h', '13']
        self.labels_xy += [[70, -8], [70, 0], [130, -12], [130, -4], [130, -20]]


class C(GraphWithConnection):
    '''Конденсатор'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.c = GraphWithConnection()
        self.c += Capacitor(name=name, highlight=highlight)
        self.c.connections[1] = [[0,0], Const.LEFT]
        self.c.connections[2] = [[20, 0],Const.RIGHT]
        self += Capacitor(name, highlight=highlight)
        self.connections[1] = [[0, 0], self.c,Const.LEFT]
        self.connections[2] = [[15, 0], self.c,Const.RIGHT]


class R3(GraphWithConnection):
    '''Реле R3N RELPOL'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k1 = GraphWithConnection()
        self.k1 += ContactOpenClose(name,highlight=highlight)
        self.k1.labels += [11,12,14]
        self.k1.labels_xy += [[0,0],[20,7],[20,0]]
        self.k1.connections[11] = [[0,0], Const.LEFT]
        self.k1.connections[12] = [[20, 10],Const.RIGHT]
        self.k1.connections[14] = [[20, 0],Const.RIGHT]
        self.k2 = GraphWithConnection()
        self.k2 += ContactOpenClose(name,highlight=highlight)
        self.k2.labels += [21,22,24]
        self.k2.labels_xy += [[0,0],[20,7],[20,0]]
        self.k2.connections[21] = [[0,0], Const.LEFT]
        self.k2.connections[22] = [[20, 10],Const.RIGHT]
        self.k2.connections[24] = [[20, 0],Const.RIGHT]
        self.k3 = GraphWithConnection()
        self.k3 += ContactOpenClose(name,highlight=highlight)
        self.k3.labels += [31,32,34]
        self.k3.labels_xy += [[0,0],[20,7],[20,0]]
        self.k3.connections[31] = [[0,0], Const.LEFT]
        self.k3.connections[32] = [[20, 10],Const.RIGHT]
        self.k3.connections[34] = [[20, 0],Const.RIGHT]
        self.w = GraphWithConnection()
        self.w += Winding(name, highlight=highlight)
        self.w.labels += ['A','B']
        self.w.labels_xy += [[0,0],[15,0]]
        self.w.connections['A'] = [[0,0], Const.LEFT]
        self.w.connections['B'] = [[15, 0],Const.RIGHT]
        self.vertices += [[0,0],[20,0],[20,-75],[0,-75],[0,0]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += ['R3N', name]
        self.labels_xy += [[10,-4], [10,0]]
        k = ContactOpenClose(highlight=highlight)
        k.mov_to(0,-30)
        self += k
        k = ContactOpenClose(highlight=highlight)
        k.mov_to(0, -50)
        self += k
        k = ContactOpenClose(highlight=highlight)
        k.mov_to(0, -70)
        self += k
        w= Winding(highlight=highlight)
        w.mov_to(2.5,-10)
        self +=w
        self.connections[11] = [[0,-30],self.k1, Const.LEFT]
        self.connections[12] = [[20, -20], self.k1,Const.RIGHT]
        self.connections[14] = [[20, -30], self.k1,Const.RIGHT]
        self.connections[21] = [[0, -50], self.k2,Const.LEFT]
        self.connections[22] = [[20, -40], self.k2,Const.RIGHT]
        self.connections[24] = [[20, -50], self.k2,Const.RIGHT]
        self.connections[31] = [[0, -70], self.k3,Const.LEFT]
        self.connections[32] = [[20, -60], self.k3,Const.RIGHT]
        self.connections[34] = [[20, -70], self.k3,Const.RIGHT]
        self.connections['A'] = [[0, -10], self.w,Const.LEFT]
        self.connections['B'] = [[20, -10], self.w,Const.RIGHT]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 3 if value[0][0] == 0 else -3
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


class CP8501_14(GraphWithConnection):
    '''Измерительный преобразователь ЦП8501/14 ООО “МНПП “Электроприбор”.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Измерительный преобразователь ЦП8501/14 ООО “МНПП “Электроприбор”.'
        self.vertices += [[0, 0], [80, 0], [80, -20], [0, -20], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.m = GraphWithConnection()
        self.m += Measurement('PA', highlight=highlight)
        self.m.connections[1] = [[0,0], Const.LEFT]
        self.m.connections[2] = [[8, 0],Const.RIGHT]
        self.p = GraphWithConnection(highlight=highlight)
        self.p += Power('Пит.', highlight=highlight)
        self.p.labels += [name, 4, 5]
        self.p.labels_xy += [[10, 6], [0, 0], [20, 0]]
        self.p.connections[4] = [[0, 0],Const.LEFT]
        self.p.connections[5] = [[20, 0],Const.RIGHT]
        self.o = GraphWithConnection(highlight=highlight)
        self.o += Power('Вых.', highlight=highlight)
        self.o.labels += [name, 13, 14]
        self.o.labels_xy += [[10, 6], [0, 0], [20, 0]]
        self.o.connections[13] = [[0, 0],Const.LEFT]
        self.o.connections[14] = [[20, 0],Const.RIGHT]
        self.connections[1] = [[5, -20], self.m, Const.DOWN]
        self.connections[2] = [[15, -20], self.m, Const.DOWN]
        self.connections[4] = [[35, -20], self.p, Const.DOWN]
        self.connections[5] = [[45, -20], self.p, Const.DOWN]
        self.connections[13] = [[65, -20], self.o, Const.DOWN]
        self.connections[14] = [[75, -20], self.o, Const.DOWN]
        self.labels += [self.name, 'ЦП8501/14','PA', 'Пит.', 'Вых.', 1,2,4,5,13,14]
        self.labels_xy += [[40,0], [40,-4],[10, -14], [40, -14], [70, -14],[5,-18],[15,-18],[35,-18],[45,-18],[65,-18],[75,-18]]


class CC301(GraphWithConnection):
    '''Счётчик электроэнергии СС-301.'''

    def __init__(self, name='', highlight=False):
        '''Конструктор класса СС301.'''
        super().__init__(name, highlight)
        self.type = 'Счётчик электроэнергии СС-301.'
        self.i = GraphWithConnection(highlight=highlight)
        self.i.vertices += [[0, 0], [25, 0], [25, -70], [0, -70], [0, 0]]
        self.i.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.i.connections[1] = [[0, -12],Const.LEFT]
        self.i.connections[3] = [[25, -12],Const.RIGHT]
        self.i.connections[4] = [[0, -37],Const.LEFT]
        self.i.connections[6] = [[25, -37],Const.RIGHT]
        self.i.connections[7] = [[0, -62],Const.LEFT]
        self.i.connections[9] = [[25, -62],Const.RIGHT]
        self.i.labels += [name, 1, 3, 4, 6, 7, 9]
        self.i.labels_xy += [[12, 5], [5, -14], [20, -14], [5, -39], [20, -39], [5, -64], [20, -64]]
        self.u = GraphWithConnection(highlight=highlight)
        self.u.vertices += [[0, 0], [90, 0], [90, -15], [0, -15], [0, 0]]
        self.u.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.u.connections[2] = [[5, 0],Const.UP]
        self.u.connections[5] = [[25, 0],Const.UP]
        self.u.connections[8] = [[45, 0],Const.UP]
        self.u.connections[10] = [[65, 0],Const.UP]
        self.u.connections[11] = [[85, 0],Const.UP]
        self.u.labels += [name, 2, 5, 8, 10, 11]
        self.u.labels_xy += [[-5, -15], [5, -2], [25, -2], [45, -2], [65, -2], [85, -2]]
        self.connections[1] = [[5, -15], self.i, Const.DOWN]
        self.connections[2] = [[15, -15], self.u, Const.DOWN]
        self.connections[3] = [[25, -15], self.i, Const.DOWN]
        self.connections[4] = [[35, -15], self.i, Const.DOWN]
        self.connections[5] = [[45, -15], self.u, Const.DOWN]
        self.connections[6] = [[55, -15], self.i, Const.DOWN]
        self.connections[7] = [[65, -15], self.i, Const.DOWN]
        self.connections[8] = [[75, -15], self.u, Const.DOWN]
        self.connections[9] = [[85, -15], self.i, Const.DOWN]
        self.connections[10] = [[95, -15], self.u, Const.DOWN]
        self.connections[11] = [[105, -15], self.u, Const.DOWN]
        self.vertices += [[0,0],[110,0],[110,-15],[0,-15],[0,0]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += [name, 'CC-301']
        self.labels_xy += [[55,0], [55,-5]]
        for key, value in self.connections.items():
            self.labels += [key]
            self.labels_xy += [[value[0][0],value[0][1]+1]]


class R(GraphWithConnection):
    '''Резистор'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.r = GraphWithConnection()
        self.r += Resistor(name=name, highlight=highlight)
        self.r.connections[1] = [[0,0],Const.LEFT]
        self.r.connections[2] = [[20, 0],Const.RIGHT]
        self += Resistor(name, highlight=highlight)
        self.connections[1] = [[0, 0], self.r,Const.LEFT]
        self.connections[2] = [[15, 0], self.r,Const.RIGHT]


class SB_F(GraphWithConnection):
    '''Кнопка управления с подсветкой ABLFS-22'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k1 = GraphWithConnection()
        self.k1 += ButtonOpen(name, highlight=highlight)
        self.k1.connections[13] = [[0,0], Const.LEFT]
        self.k1.connections[14] = [[20, 0],Const.RIGHT]
        self.connections[13] = [[0,0],self.k1, Const.LEFT]
        self.connections[14] = [[20, 0], self.k1,Const.RIGHT]
        self.k2 = GraphWithConnection()
        self.k2 += ButtonClose(name, highlight=highlight)
        self.k2.connections[21] = [[0, 0],Const.LEFT]
        self.k2.connections[22] = [[20, 0],Const.RIGHT]
        self.connections[21] = [[0, -10], self.k2,Const.LEFT]
        self.connections[22] = [[20, -10], self.k2,Const.RIGHT]
        self.l = GraphWithConnection()
        self.l += Bulb(name, highlight=highlight)
        self.l.connections['X1'] = [[0, 0],Const.LEFT]
        self.l.connections['X2'] = [[20, 0],Const.RIGHT]
        self.connections['X1'] = [[0, -20], self.l,Const.LEFT]
        self.connections['X2'] = [[20, -20], self.l,Const.RIGHT]
        self.vertices += [[0,10],[20,10],[20,-25],[0,-25],[0,10]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self += ButtonOpen(highlight=highlight)
        b = ContactClose(highlight=highlight)
        b.mov_to(0,-10)
        self += b
        l = Bulb(highlight=highlight)
        l.mov_to(0,-20)
        self += l
        self.vertices += [[10,-11.5],[10,-10.5],[10,-9.5],[10,-8.5],[10, -7.5], [10, -6.5], [10, -5.5],
                          [10, -4.5],[10,-3.5],[10,-2.5],[10,-1.5],[10,-0.5],[10,0.5],[10,1.5]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.MOVETO,
                       Path.LINETO, Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.labels += [name, 13,14,21,22,'X1','X2']
        self.labels_xy += [[10,10],[2,0],[17,0],[2,-10],[17,-10],[2,-20],[17,-20]]


class SF(GraphWithConnection):
    '''Однополюсный автомат'''

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
        self.k1_2.connections[1] = [[0, 0],Const.UP]
        self.k1_2.connections[2] = [[0, -20], Const.DOWN]
        self.k1_2.labels += [1, 2]
        self.k1_2.labels_xy += [[1, -2], [1, -22]]
        k = ContactOpen(name)
        k.rotate(90)
        k.labels_xy[0][0] += 10
        k.mov_to(0, -20)
        k.vertices += [[-1.5, -12], [-2.9, -12.7], [-4.6, -9.3], [-3.2, -8.6]]
        k.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self += k
        self.connections[1] = [[0, 0], self.k1_2,Const.UP]
        self.connections[2] = [[0, -20], self.k1_2, Const.DOWN]


class SF2(SF):
    '''Двухполюсный автомат'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k3_4 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name)
        k.rotate(90)
        k.labels_xy[0][0] += 10
        k.mov_to(0, -20)
        k.vertices += [[-1.5, -12], [-2.9, -12.7], [-4.6, -9.3], [-3.2, -8.6]]
        k.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.k3_4 += k
        self.k3_4.connections[3] = [[0, 0],Const.UP]
        self.k3_4.connections[4] = [[0, -20], Const.DOWN]
        self.k3_4.labels += [3, 4]
        self.k3_4.labels_xy += [[1, -2], [1, -22]]
        k = ContactOpen(name)
        k.rotate(90)
        k.labels_xy[0][0] += 10
        k.mov_to(0, -20)
        k.vertices += [[-1.5, -12], [-2.9, -12.7], [-4.6, -9.3], [-3.2, -8.6]]
        k.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        k.mov_to(20, 0)
        self += k
        self.connections[3] = [[20, 0], self.k3_4,Const.UP]
        self.connections[4] = [[20, -20], self.k3_4, Const.DOWN]


class BI4(GraphWithConnection):
    '''Блок испытательный БИ-4.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Блок испытательный БИ-4.'
        self.n = []
        for i in range(4):
            self.n.append(GraphWithConnection())
            self.n[-1] += ConnectionDetachable(name,highlight=highlight)
            self.n[-1].labels += [i*2+1,i*2+2]
            self.n[-1].labels_xy += [[-1,-1,MTEXT_TOP_RIGHT],[6,-1,MTEXT_TOP_LEFT]]
            self.n[-1].connections[i*2+1] = [[0,0], Const.LEFT]
            self.n[-1].connections[i * 2 + 2] = [[2, 0],Const.RIGHT]
            c = ConnectionDetachable()
            c.rotate(90)
            c.mov_to(i*11+8, -13)
            self += c
            self.connections[i*2+1] = [[i * 11 +8,0], self.n[-1],Const.UP]
            self.connections[i*2+2] = [[i * 11 +8,-20], self.n[-1], Const.DOWN]
            self.labels += [i*2+1,i*2+2]
            self.labels_xy += [[i * 11 +8,-4],[i * 11 +8,-20]]
        self.vertices += [[0,0],[56,0],[56,-20],[0,-20],[0,0]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += [name, 'БИ-4']
        self.labels_xy += [[-5,-12],[50,-4]]

class BI6(GraphWithConnection):
    '''Блок испытательный БИ-6.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Блок испытательный БИ-6.'
        self.n = []
        for i in range(6):
            self.n.append(GraphWithConnection())
            self.n[-1] += ConnectionDetachable(name, highlight=highlight)
            self.n[-1].labels += [i * 2 + 1, i * 2 + 2]
            self.n[-1].labels_xy += [[-1,-1,MTEXT_TOP_RIGHT],[6,-1,MTEXT_TOP_LEFT]]
            self.n[-1].connections[i * 2 + 1] = [[0, 0],Const.LEFT]
            self.n[-1].connections[i * 2 + 2] = [[2, 0],Const.RIGHT]
            c = ConnectionDetachable()
            c.rotate(90)
            c.mov_to(i * 11 + 8, -13)
            self += c
            self.connections[i * 2 + 1] = [[i * 11 + 8, 0], self.n[-1],Const.UP]
            self.connections[i * 2 + 2] = [[i * 11 + 8, -20], self.n[-1], Const.DOWN]
            self.labels += [i * 2 + 1, i * 2 + 2]
            self.labels_xy += [[i * 11 + 8, -4], [i * 11 + 8, -20]]
        self.vertices += [[0, 0], [76, 0], [76, -20], [0, -20], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += [name, 'БИ-6']
        self.labels_xy += [[-5, -12], [71, -4]]

class AC22_old(GraphWithConnection):
    '''Переключатель AC22 старого образца.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Переключатель AC22'
        self.k1 = GraphWithConnection()
        self.k1 += ContactOpen(name,highlight=highlight)
        self.k1.labels += [1,2]
        self.k1.labels_xy += [[0,-1,MTEXT_TOP_CENTER],[20,-1,MTEXT_TOP_CENTER]]
        self.k1.connections[1] = [[0,0], Const.LEFT]
        self.k1.connections[2] = [[20, 0],Const.RIGHT]
        self += ContactOpen(name,highlight=highlight)
        self.labels += [1, 2]
        self.labels_xy += [[2, 0], [18, 0]]
        self.connections[1] = [[0, 0], self.k1,Const.LEFT]
        self.connections[2] = [[20, 0], self.k1,Const.RIGHT]
        self.vertices += [[0, 6], [20, 6], [20, -3], [0, -3], [0, 6]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
