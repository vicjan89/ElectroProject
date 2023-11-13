from classes import View


class VSF(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.c:
            self.correspondence = {self.c[0]: (0, 0),
                                   self.c[1]: (0, -10)}

    def draw(self):
        self.te.lines((self.x-5, self.y), (self.x, self.y-10))
        self.te.lines((self.x+1, self.y+1), (self.x-1, self.y-1))
        self.te.lines((self.x+1, self.y-1), (self.x-1, self.y+1))
        self.te.lines((self.x-1.8, self.y-6.4), (self.x-3.1, self.y-7.1), (self.x-4.8, self.y-3.9),
                       (self.x-3.4, self.y-3.2))

        self.te.label(self.x, self.y, getattr(self.e, self.c[0]).name, 'e', 2)
        self.te.label(self.x, self.y-10, getattr(self.e, self.c[1]).name, 'e', 2)
        self.te.label(self.x+3, self.y-5, self.e.name, 'e')
        self.te.circle(self.x, self.y-10, 1)
