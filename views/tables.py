from classes import View, Element, Connection

class TableApparatus(View):

    def draw(self):
        row_num = 0
        for name, item in self.e.__dict__.items():
            if isinstance(item, Element) and not isinstance(item, Connection) and name not in ('wires','g','g1','g2'):
                model = item.model if item.model else ''
                self.te.label(self.x, self.y - row_num * 6,f'{row_num+1}. {item.name}\t{model}','e')
                row_num += 1

    def get_coords(self, c: Connection):
        return None
