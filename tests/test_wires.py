from src.Diagrams import *

doc = ezdxf.new()
doc.units = ezdxf.units.MM
msp = doc.modelspace()

angles = [0,90,180,270]
localisations = [[60,0],
                 [60,-60],
                 [0,-60],
                 [-60,-60],
                 [-60,0],
                 [-60,60],
                 [0,60],
                 [60,60],
                 ]
num_test = 1
for l in localisations:
    for angle1 in angles:
        r1 = R()
        r1.connections[1][1].rotate(angle1)
        for angle2 in angles:
            r2 = R()
            r2.connections[1][1].rotate(angle2)
            r2.connections[1][1].mov_to(1, 0, num_test*130)
            r2.connections[1][1].show(msp)
            r1.connections[1][1].mov_to(1, l[0], l[1] + num_test * 130)
            r1.connections[1][1].show(msp)
            # msp.add_lwpolyline(((0,num_test*130),(100,num_test*130),(100,num_test*130),))
            w = Wire(r1,1,r2,1, name=num_test)
            w.show(msp)
            num_test += 1
doc.saveas('Тест соединителей.dxf', encoding='utf-8')
print('Тест сохранён.')