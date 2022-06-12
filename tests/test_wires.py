from src.Diagrams import *

doc = ezdxf.new()
doc.units = ezdxf.units.MM
msp = doc.modelspace()

angles = [0,90,180,270]
localisations = [[60,0],
                 [60,-30],
                 [60,-60],
                 [30,-60],
                 [0,-60],
                 [-30,-60],
                 [-60,-60],
                 [-60,-30],
                 [-60,0],
                 [-60,30],
                 [-60,60],
                 [-30,60],
                 [0,60],
                 [30,30],
                 [60,60],
                 ]
num_col = 0
num_str = 0
for l in localisations:
    for angle1 in angles:
        r1 = R()
        r1.connections[1][1].rotate(angle1)
        for angle2 in angles:
            r2 = R()
            r2.connections[1][1].rotate(angle2)
            r2.connections[1][1].mov_to(1, num_col*130, -num_str*130)
            r2.connections[1][1].show(msp)
            r1.connections[1][1].mov_to(1, l[0] + num_col*130, -l[1] - num_str * 130)
            r1.connections[1][1].show(msp)
            w = Wire(r1,1,r2,1, name=str(num_str)+str(num_col))
            w.show(msp)
            if num_col == 9:
                num_col = 0
                num_str += 1
            else:
                num_col += 1
doc.saveas('Тест соединителей.dxf', encoding='utf-8')
print('Тест сохранён.')