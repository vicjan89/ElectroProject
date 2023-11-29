from dataclasses import dataclass


from classes import Connection, View


class VXT(View):
    '''Класс отображает одиночную клемму в виде кружка'''
    def draw(self):
        self.te.circle(self.x, self.y, 1, black=True)
        self.te.label(self.x, self.y, self.e.name, s=2)

class VXT1(View):
    '''Класс отображает одиночную клемму в виде перечёркнутого кружка'''

    def draw(self):
        d = 1.5
        self.te.circle(self.x, self.y, 1, black=True)
        self.te.lines((self.x - d, self.y -d), (self.x + d, self.y + d))
        self.te.label(self.x, self.y, self.e.name, s=2)

class VXTcross(View):
    '''Класс отображает одиночную кроссовую клемму'''

    def draw(self):
        self.te.lines((self.x - 4, self.y), (self.x + 4, self.y ))
        self.te.circle(self.x, self.y, 1.2, black=True)
        self.te.label(self.x, self.y, self.e.name, s=2)

class VXTm(View):
    '''Класс отображает одиночную испытательную клемму'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (4, 0)}

    def draw(self):
        self.te.lines((self.x, self.y), (self.x + 4, self.y))
        self.te.circle(self.x, self.y, 1, black=True)
        self.te.circle(self.x+4, self.y, 1, black=True)
        self.te.label(self.x, self.y, getattr(self.e, self.c[0]).name, s=2)


class VG(View):
    '''Класс для описания земли'''

    def draw(self):
        x, y = self.x, self.y
        self.te.lines((x, y), (x, y-5))
        self.te.lines((x-5, y-5), (x+5, y - 5))
        self.te.lines((x-3, y-6), (x+3, y - 6))
        self.te.lines((x-1, y-7), (x+1, y - 7))

class VXTmount(View):
    '''Класс для описания клеммника на монтажной схеме'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def bottom(self):
        return self.y - self.e.size * 6 - 17

    def draw(self):
        x, y = self.x, self.y
        self.te.label(x+10,y,self.e.name,'n')
        for c in range(self.e.size):
            yc = y-c*6
            self.te.lines((x,yc),(x+20,yc), (x+20,yc-6),(x,yc-6),cycle=True)
            self.te.lines((x+4,yc),(x+4,yc-6))
            self.te.lines((x+9.5,yc),(x+9.5,yc-6))
            self.te.label(x+4,yc-3,c+1,'e',2)
            if self.e.jumpers[c]:
                self.te.lines((x+2,yc-3),(x+2,yc+3))
                self.te.circle(x+2,yc-3,1,True)
                self.te.circle(x+2,yc+3,1,True)
            con = self.e.__dict__.get(f'k{c+1}')
            connected, name = con.connected()
            for num, connect in enumerate(connected):
                label = connect.label
                if 'XT' in label:
                    label = label.split(':')[1]
                    if self.e != connect.parent:
                        label = f'{connect.parent.cabinet}:{label}'
                if num == 0:
                    self.te.lines((x,yc-3), (x-5,yc-3))
                    self.te.label(x-5,yc-3,label,'w',2)
                    self.te.label(x+9,yc-3,name,'e',2)
                elif num == 1:
                    self.te.lines((x+20,yc-3), (x+25,yc-3))
                    self.te.label(x+25,yc-3,label,'e',2)
                if num == 2:
                    self.te.lines((x, yc - 3), (x - 5, yc))
                    self.te.label(x - 5, yc, label, 'w', 2)
                elif num == 3:
                    self.te.lines((x+20,yc-3), (x+25,yc))
                    self.te.label(x+25,yc,label,'e',2)


    def get_coords(self, c: Connection):
        return None


class VXTmountM(View):
    '''Класс для описания испытательного клеммника на монтажной схеме'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def bottom(self):
        return self.y - self.e.size * 6 - 17

    def draw(self):
        x, y = self.x, self.y
        self.te.label(x + 10, y, self.e.name, 'n')
        for c in range(self.e.size):
            yc = y - c * 6
            self.te.lines((x, yc), (x + 30, yc), (x + 30, yc - 6), (x, yc - 6), cycle=True)
            self.te.label(x + 10, yc - 3, c + 1, 'e', 2)
            if self.e.jumpers[c]:
                self.te.lines((x + 2, yc - 3), (x + 2, yc + 3))
                self.te.circle(x + 2, yc - 3, 1, True)
                self.te.circle(x + 2, yc + 3, 1, True)
            con = self.e.__dict__.get(f'k{c + 1}')
            con_ = self.e.__dict__.get(f'k{c + 1}_')
            connected, name = con.connected()
            for num, connect in enumerate(connected):
                if num == 0:
                    self.te.lines((x, yc - 3), (x - 5, yc - 3))
                    self.te.label(x - 5, yc - 3, connect.label, 'w', 2)
                elif num == 1:
                    self.te.lines((x, yc - 3), (x - 5, yc))
                    self.te.label(x - 5, yc, connect.label, 'w', 2)
                else:
                    assert False, f'На измерительную клемму {c+1} клеммника {self.e.name} подключено более 2 проводов'
            connected_, name_ = con_.connected()
            for num, connect in enumerate(connected_):
                if num == 0:
                    self.te.lines((x + 30, yc - 3), (x + 35, yc - 3))
                    self.te.label(x + 35, yc - 3, connect.label, 'e', 2)
                elif num == 1:
                    self.te.lines((x + 30, yc - 3), (x + 35, yc))
                    self.te.label(x + 35, yc, connect.label, 'e', 2)
                else:
                    assert False, f'На измерительную клемму {c+1} клеммника {self.e.name} подключено более 2 проводов'

    def get_coords(self, c: Connection):
        return None