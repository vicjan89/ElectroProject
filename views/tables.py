from classes import View, Element, Connection

class TableApparatus(View):

    def draw(self):
        row_num = 0
        names = set()
        for name, item in self.e.__dict__.items():
            if isinstance(item, Element) and not isinstance(item, Connection) and name not in ('wires','g','g1','g2', 'g3'):
                if item.name not in names:
                    model = item.model if item.model else ''
                    text = f'{row_num+1}. {item.name} {model}'
                    if item.location:
                        text += f' ({item.location})'
                    self.te.label(self.x, self.y - row_num * 6, text,'e')
                    row_num += 1
                    names.add(item.name)

    def get_coords(self, c: Connection):
        return None
