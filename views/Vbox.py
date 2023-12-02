from classes import View, Connection
from views.func_graph_elements import *
from views.Vrelay_component import VcontNo, VcontNc
from views.Vradio_component import VDiodeB
from views.VXT import VG


class Vbox(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            i = 0
            self.correspondence = dict()
            while i < len(self.c):
                self.correspondence[self.c[i]] = (i % 2 * 30, - int(i / 2) * 15)
                i += 1

    def draw(self):
        y = self.y - (len(self.c)+1) // 2 * 15 + 10
        self.te.lines((self.x, self.y+10), (self.x+30, self.y+10), (self.x+30, y), (self.x, y), cycle=True)
        i = 0
        while i < len(self.c):
            self.te.label(self.x + i % 2 * 30, self.y - i // 2 * 15, getattr(self.e, self.c[i]).name,
                          'w' if i%2 else 'e', 2)
            i += 1
        self.te.label(self.x + 15, self.y + 10, self.e.name, 'n')

class VboxCombo(Vbox):
    '''
    Класс для описания графического отображения устройства с разными парами контаков (текст, открытый контакт или закрытый контакт)
    '''

    def __init__(self, labels: list | tuple, contacts: list | tuple, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.labels = labels
        self.contacts = contacts

    def draw(self):
        super().draw()
        for i in range(len(self.c)//2):
            match self.contacts[i]:
                case 'no':
                    VcontNo.draw_no(self.te, self.x+7, self.y - i * 15-2, self.labels[i])
                case 'nc':
                    VcontNc.draw_nc(self.te, self.x + 7, self.y - i * 15 + 2, self.labels[i])
                case _:
                    self.te.label(self.x + 15, self.y - i * 15, self.labels[i], 'c')


class VboxNo(Vbox):

    def __init__(self, labels: list | tuple, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.labels = labels

    def draw(self):
        super().draw()
        for i in range(len(self.c)//2):
            VcontNo.draw_no(self.te, self.x+7, self.y - i * 15-2, self.labels[i])

class VboxNc(Vbox):

    def __init__(self, labels: list | tuple, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.labels = labels

    def draw(self):
        super().draw()
        for i in range(len(self.c)//2):
            VcontNc.draw_nc(self.te, self.x+7, self.y - i * 15+2, self.labels[i])

class VboxTxt(Vbox):

    def __init__(self, labels: list | tuple, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.labels = labels

    def draw(self):
        super().draw()
        for i in range(len(self.c)//2):
            self.te.label(self.x + 15, self.y - i * 15, self.labels[i], 'c')

class Vlbox(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            i = 0
            self.correspondence = dict()
            while i < len(self.c):
                self.correspondence[self.c[i]] = (0, - i * 15)
                i += 1

    def draw(self):
        y = self.y - len(self.c)  * 15 + 10
        self.te.lines((self.x, self.y+10), (self.x+20, self.y+10), (self.x+20, y), (self.x, y), cycle=True)
        i = 0
        while i < len(self.c):
            self.te.label(self.x, self.y - i * 15, getattr(self.e, self.c[i]).name, 'e', 2)
            i += 1
        self.te.label(self.x + 10, self.y + 10, self.e.name, 's')


class Vlbox_mount(View):

    @property
    def bottom(self):
        len_trans = len(self.e.trans)
        len_trans = len_trans if len_trans <= 45 else 45
        return self.y - len_trans  * 6 - 15

    def draw(self):
        begin = 0
        x = self.x
        while begin < len(self.e.trans):
            trans = self.e.trans[begin:begin+40]
            y = self.y - len(trans)  * 6
            self.te.lines((x, self.y+6), (x+23, self.y+6), (x+23, y), (x, y), cycle=True)
            for num, item in enumerate(trans):
                yc = self.y - num * 6
                self.te.label(x, yc, item[1], 'e', 2)
                my_con = getattr(self.e, item[0])
                connected, name = my_con.connected()
                for n, connect in enumerate(connected):
                    label = connect.label.replace('_','')
                    if 'XT' in label:
                        label = label.split(':')[1]
                    if n == 0:
                        self.te.lines((x, yc), (x - 5, yc))
                        self.te.label(x - 18, yc, name, 'w', 2, box=True)
                        self.te.label(x - 5, yc, label, 'w', 2)
                    elif n == 1:
                        self.te.lines((x, yc), (x - 5, yc + 3))
                        self.te.label(x - 5, yc+3, label, 'w', 2)
                    else:
                        assert False, f'На вывод {item[1]} аппарата {self.e.name} подключено более 2 проводов'
            self.te.label(x + 10, self.y + 5, self.e.name, 'n')
            begin += 40
            x += 60

    def get_coords(self, c: Connection):
        return None

class VSQ_mount(Vlbox_mount):

    def draw(self):
        super().draw()
        x = self.x
        y = self.y
        VcontNo.draw_no(self.te, x+5, y, '')
        VcontNc.draw_nc(self.te, x+5, y-12, '')
        self.te.lines((x+21, y), (x+21, y-6), (x+5, y-6))
        self.te.lines((x + 21, y-12), (x + 21, y - 18), (x + 5, y - 18))

class VVD_mount(Vlbox_mount):

    def draw(self):
        super().draw()
        x = self.x
        y = self.y
        VDiodeB.draw_(self.te, x+15, y+2,'')

class VDXN8_Q_mount(Vlbox_mount):

    def draw(self):
        super().draw()
        x = self.x
        y = self.y
        VcontNo.draw_no(self.te, x+5, y-12, '')
        self.te.lines((x+21, y-12), (x+21, y-18), (x+5, y-18))
        self.te.label(x+3, y, '-', 'e')
        self.te.label(x+3, y-6, '+', 'e')
        self.te.label(x+3, y-30, 'c', 'e')
        self.te.label(x+3, y-36, 'b', 'e')
        self.te.label(x+3, y-42, 'a', 'e')
        VG.draw_(self.te, x-17, y-24)
        self.te.lines((x, y-24), (x-17, y-24))
        self.te.lines((x, y-30), (x-5, y-30))
        self.te.lines((x, y-36), (x-5, y-36))
        self.te.lines((x, y-42), (x-5, y-42))

