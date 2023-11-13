from textengines.LaTeX import LaTeX

from Project import *
from Vlist import *


prj = (('Отходящая линия 10кВ ТП-897', 'OL_TP897'),
       ('ОБР ТП Сеом', 'OBR_SEOM'))
for n, p in enumerate(prj):
    print(f'{n+1}\t{p[0]}')
c = int(input('Введите номер проекта (0 - для нового)>'))
# c = 2
if c == 0:
    name = input('Введите имя проекта: ')
    file = input('Введите имя файла: ')
else:
    name = prj[c-1][0]
    file = prj[c-1][1]
    file_tex = prj[c-1][1] + '.tex'
w = Wires()

te = LaTeX(path=file_tex, static='static')
p = Project(name=name, storage=YamlStorage(file), te=te)
p.wires = w
if c:
    p.load()
elements = p.__dict__.copy()
for name in ('name', 'storage','cabinet','location','model','te','wires','docwires'):
    elements.pop(name)
globals().update(elements)
# p.replace('sqs1_1', SQ_VP15)
# p.save()
# w.get_all(p.kl3.n2)
# el = p.gefc('СР-1')
# p.l5.place(el)