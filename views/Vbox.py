from classes import View, Connection
from views.func_graph_elements import *


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

class VboxNo(Vbox):

    def __init__(self, labels: list | tuple, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.labels = labels

    def draw(self):
        super().draw()
        for i in range(len(self.c)//2):
            self.te.latex(contact_no(self.x+7, self.y - i * 15-2, name=self.labels[i]))

class VboxNc(Vbox):

    def __init__(self, labels: list | tuple, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.labels = labels

    def draw(self):
        super().draw()
        for i in range(len(self.c)//2):
            self.te.latex(contact_nc(self.x+7, self.y - i * 15+2, name=self.labels[i]))

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
            self.te.lines((x, self.y+5), (x+20, self.y+5), (x+20, y), (x, y), cycle=True)
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
