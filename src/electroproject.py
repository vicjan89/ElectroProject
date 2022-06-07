'''Модуль прорисовки проектной документации.'''

from src.GraphWithConnection import *

class CircuitDiagram:
    '''Вывод принципиальной схемы в формат DXF.'''

    def __init__(self, wires_list: list, msp):
        '''Вывод принципиальной схемы в формат DXF.

        :param wires_list: список проводников.
        :param msp: пространство модели DXF.

        '''

        #Формирование групп соединённых элементов
        groups = []
        while len(wires_list) > 0:
            group = []
            connections = []
            connections.append([wires_list[0].a,wires_list[0].key_a])
            connections.append([wires_list[0].b, wires_list[0].key_b])
            group.append(wires_list.pop(0))
            run = True
            while run:
                run = False
                for i in wires_list:
                    if [i.a,i.key_a] in connections:
                        connections.append([i.b,i.key_b])
                        for key in i.a.connections[i.key_a][1].connections:
                            connections.append([i.a,key])
                        for key in i.b.connections[i.key_b][1].connections:
                            connections.append([i.b, key])
                        group.append(i)
                        wires_list.remove(i)
                        run = True
                    elif [i.b,i.key_b] in connections:
                        connections.append([i.a, i.key_a])
                        for key in i.b.connections[i.key_b][1].connections:
                            connections.append([i.b, key])
                        for key in i.a.connections[i.key_a][1].connections:
                            connections.append([i.a,key])
                        group.append(i)
                        wires_list.remove(i)
                        run = True
            groups.append(group)
        return groups


class WiringDiagram:
    '''Вывод монтажной схемы в формат DXF.'''
    def __init__(self, list_elements: list, wires: list, msp):
        for i in list_elements:
            i[0].mov_to(x=i[1][0], y=i[1][1])
            i[0].show(msp)
        coords = []
        for i in wires:
            coords += i.show_wd(msp, coords)


