from textengines.LaTeX import LaTeX

from Project import *
from Vlist import *
# from views.VA4 import VA4
# from views.VXT import VXT
# from views.Vradio_component import *
# from views.VSQ import VSQ
# from views.Vrelay_component import *


prj = (('Отходящая линия 10кВ ТП-897', 'OL_TP897'),
       ('ОБР ТП Сеом', 'OBR_SEOM', 'ТП заказ 814.tex'))
for n, p in enumerate(prj):
    print(f'{n+1}\t{p[0]}')
# c = int(input('Введите номер проекта (0 - для нового)>'))
c = 1
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

# p.draw()