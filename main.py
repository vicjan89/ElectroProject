import os


from textengines.LaTeX import LaTeX

from classes import *
from radio_component import *
from MR5PO50 import MR5PO50
from XT import XT
from SQ import *
from Project import Project
from VA4 import VA4
from VXT import VXT


prj = (('Отходящая линия 10кВ ТП-897', 'OL_TP897'),
       ('ОБР ТП Сеом', 'OBR_SEOM', 'ТП заказ 814.tex'))
for n, p in enumerate(prj):
    print(f'{n+1}\t{p[0]}')
# c = int(input('Введите номер проекта (0 - для нового)>'))
c = 2
if c == 0:
    name = input('Введите имя проекта: ')
    file = input('Введите имя файла: ')
else:
    name = prj[c-1][0]
    file = prj[c-1][1]
    file_tex = prj[c-1][2]
w = Wires()

te = LaTeX(path=file_tex, static='static')
p = Project(name=name, storage=YamlStorage(file), te=te)
p.wires = w
if c:
    p.load()

# p.av(VA4())
# p.av(VXT(x= 100, y=50, e=p.xt.k1))
for i in p.ge():
    print(i.slag)
# p.draw()
# os.system(f'pdflatex "{file_tex}"')