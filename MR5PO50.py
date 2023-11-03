from classes import Element, Connection


class MR5PO50(Element):
    '''Класс для описания микропроцессорного реле МР5ПО50 производства ОАО "БЭМН" г.Минск.'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Ia: Connection = Connection(name='X7-1', parent=self)
        self.Ia4: Connection = Connection(name='X8-2', parent=self)
        self.Ia0: Connection = Connection(name='X8-3', parent=self)
        self.Ib: Connection = Connection(name='X7-4', parent=self)
        self.Ib4: Connection = Connection(name='X8-5', parent=self)
        self.Ib0: Connection = Connection(name='X8-6', parent=self)
        self.Ic: Connection = Connection(name='X7-7', parent=self)
        self.Ic4: Connection = Connection(name='X8-8', parent=self)
        self.Ic0: Connection = Connection(name='X8-9', parent=self)
        self.In: Connection = Connection(name='X7-10', parent=self)
        self.In4: Connection = Connection(name='X8-11', parent=self)
        self.In0: Connection = Connection(name='X8-12', parent=self)

    def encode(self):
        res = {'class': 'MR5PO50'}
        for key, value in self.__dict__.items():
            if isinstance(value, (int, float, str, dict)):
                res[key] = value
        return res

    '''
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
        '''
