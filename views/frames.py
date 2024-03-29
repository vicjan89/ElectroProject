from classes import View, Connection


class Vcabinet(View):

    def draw(self):
        x = self.x
        y = self.y
        self.te.lines((x,y),(x+40,y),(x+40,y-20),(x,y-20), cycle=True, tl = 1)
        self.te.label(self.x+20, self.y, self.e.cabinet, 'n')

    def get_coords(self, c: Connection):
        return None

class VcabinetD(View):

    def draw(self):
        x = self.x
        y = self.y
        self.te.lines((x,y),(x+40,y),(x+40,y-40),(x,y-40), cycle=True, tl = 1)
        self.te.label(self.x+20, self.y, self.e.cabinet, 'n')

    def get_coords(self, c: Connection):
        return None

class Vlabel(View):

    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, text={self.text})'

    def draw(self):
        self.te.label(self.x, self.y, self.text, 'n')

class Ruler(View):

    def draw(self):
        for x in range(0, 180, 10):
            self.te.lines((x, 0), (x, 5))
            self.te.label(x=x, y=0, text=x)
        for y in range(0, 250, 10):
            self.te.lines((0, y), (5, y))
            self.te.label(x=0, y=y, text=y)

class Vexplanation(View):

    def __init__(self, t: str, h: int,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.t= t
        self.h= h

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, h={self.h}, t={self.t})'

    def draw(self):
        x = self.x
        y = self.y
        self.te.lines((x,y),(x+25,y),(x+25,y-self.h),(x,y-self.h), cycle=True)
        self.te.mtext(x+12.5, y-self.h/2, 25, self.t, 'c', 2)

class Vframe_cross(View):

    def __init__(self, w: int, h: int, num: int,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.w= w
        self.h= h
        self.num = num


    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y},  w={self.w}, h={self.h})'

    def draw(self):
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        self.te.lines((x,y),(x+w,y),(x+w,y-h),(x,y-h), cycle=True)
        self.te.lines((x, y - 10), (x + w, y - 10))
        self.te.lines((x, y - h + 10), (x + w, y - h + 10))
        self.te.label(x+ w/2, y - 5, self.num, 'c')
        self.te.latex(f'\\draw({x+w/2}, {y - h +5}) node [align=center]' +
                      r'{\parbox{' + str(w) + r'mm}{\begin{spacing}{0.6}\centering {\footnotesize ' + self.e.cabinet +
                      r'}\end{spacing}}};')

    def get_coords(self, c: Connection):
        return None
