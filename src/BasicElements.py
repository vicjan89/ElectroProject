'''Модуль описания базовых классов для создания элементов электрических схем.'''

import math

from ezdxf.lldxf.const import *


class Const:
    LEFT = 1
    RIGHT = 2
    ALL = 3
    UP = 4
    DOWN = 5



class Path:
    '''Описывает константы команд для рисования полилинии. Остались после перехода с MatPlotLib на ezdxf.'''
    MOVETO = 1
    LINETO = 2



class ElementCircuit:
    '''Базовый элемент схемы'''
    def __init__(self, name='', highlight=False):
        self.name = name
        self.__visible = False
        self.__highlight = highlight

    def show(self):
        '''При выводе в файл отмечает элемент как видимый.'''
        self.__visible = True

    @property
    def visible(self) -> bool:
        '''Свойство видимости объекта'''
        return self.__visible

    @visible.setter
    def visible(self,new):
        self.__visible = new

    @property
    def highlight(self) -> bool:
        '''Свойство выделенности элемента.'''
        return self.__highlight

    def __str__(self):
        return self.name

class ElementGraph(ElementCircuit):
    '''Базовый класс для графических элементов'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight)
        self.vertices = []
        self.codes = []
        self.centers = []
        self.radii = []
        self.labels_xy = []
        self.labels = []

    def mov_to(self, x, y):
        if len(self.vertices) > 0:
            dx = x - self.vertices[0][0]
            dy = y - self.vertices[0][1]
        else:
            dx = x - self.centers[0][0]
            dy = y - self.centers[0][1]
        self.mov(dx,dy)

    def mov(self, dx, dy):
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

    def mirror(self):
        for i in self.vertices:
            i[0] = -i[0]
        for i in self.centers:
            i[0] = -i[0]
        for i in self.labels_xy:
            i[0] = -i[0]


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
            lw = 50
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
            ax.add_mtext(self.labels[i],
                         dxfattribs={'style' : 'cyrillic_ii'}).set_location(insert=(self.labels_xy[i][0],
                                                                                    self.labels_xy[i][1]),
                                                                            attachment_point=MTEXT_MIDDLE_CENTER if len(self.labels_xy[i]) == 2 else self.labels_xy[i][2])
