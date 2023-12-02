from textengines.LaTeX import LaTeX
from textengines.DXF import DXF

from Project import *
from Vlist import *

path = 'projects'
files = os.listdir(path)
for n, name in enumerate(files):
    print(f'{n+1}\t{name}')

c = int(input('Введите номер проекта (0 - для нового)>'))
if c == 0:
    name = input('Введите имя проекта: ')
    file = input('Введите имя файла: ')
else:
    name = files[c-1]
    file = files[c-1].split('.')[0]
    file_out = os.path.join('out', file)
w = Wires()

te = LaTeX(path=file_out + '.tex', static='static')
# te = DXF(path=file_out + '.dxf')
p = Project(name=name, storage=YamlStorage(os.path.join(path, file)), te=te)
p.wires = w
if c:
    p.load()
# elements = p.__dict__.copy()
# for name in ('name', 'storage','cabinet','location','model','te','wires','docwires'):
#     elements.pop(name)
# globals().update(elements)
# p.de(p.yg2_3)
# p.draw(False)
# p.save()
# p.al(8)