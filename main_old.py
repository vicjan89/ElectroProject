from src.Diagrams import *

a1 = BB_TEL10(name='A1')
a1.em.mirror()
a1.bk.mirror()
a2=PS7('A2')
a3=BU_TEL('A3')
a4=BP_TEL('A4')
a5=MR500_V2('A5')
a6=PS3_old('A6')
a8=DUGA_O('A8')
a9=PS12('A9')
kv1=R3('KV1', highlight=True)
kv2=R3('KV2')
kv3=R3('KV3')
pa=CP8501_14('PA')
pik=CC301('PIK')
r1=R('R1', highlight=True)
r2=R('R2')
r3=R('R3')
r4=R('R4')
r5=R('R5')
r6=R('R6')
r7=R('R7')
r8=R('R8')
r9=R('R9')
r10=R('R10')
r11=R('R11')
r12=R('R12')
r13=R('R13')
r14=R('R14')
r15=R('R15')
r16=R('R16')
r17=R('R17')
r18=R('R18')
sb1=SB_F('SB1')
sb2=SB_F('SB2')
sf1=SF2('SF1')
sf2=SF2('SF2')
sg1=BI4('SG1')
sg2=BI6('SG2')
sg3=BI4('SG3')
sx1=AC22_old('SX1',highlight=True)
sx2=AC22_old('SX2')
sx3=AC22_old('SX3')
sx4=AC22_old('SX4')
sx5=AC22_old('SX5')
sx6=AC22_old('SX6')
ct_a = CT2('TA-A')
ct_a.w1.mirror()
ct_a.w2.mirror()
ct_b = CT2('TA-B')
ct_b.w1.mirror()
ct_b.w2.mirror()
ct_c = CT2('TA-C')
ct_c.w1.mirror()
ct_c.w2.mirror()
x = Connectors('X', 30)
x.n[8].mirror()
x.n[6].mirror()
x.n[13].mirror()
x.n[14].mirror()
x.n[15].mirror()
x.n[16].mirror()
x.n[20].mirror()
xt1 = XT('XT1', 120)
xt2 = XT('XT2', 70)
xt3 = XT('XT3', 32, 'СШР55-П30-ЗГ1')

#Выкатной элемент
v_e = [a1, x]
#Дверь релейного отсека
d_r_o = [a2,a5,a6,a8,a9,pa,pik,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,sb1,sb2,sx1,sx2,sx3,sx4,sx5,sx6,xt3]
#Шасси релейного отсека
sh_r_o = [a3,a4,kv1,kv2,kv3,r1,r2,sf1,sf2,sg1,sg2,sg3,xt2]
#Отсек трансформаторов тока
o_tt = [ct_a,ct_b,ct_c]
#Релейный отсек
r_o = [x,xt1]
all_list = v_e+d_r_o+sh_r_o+o_tt+r_o

elements = Elements('Элементы')
elements.add(all_list)
# elements.load_json()  #чтение координат элементов из файда

wires = Wires('Проводники',elements)
wires.load_json()   #чтение проводников из файла

cd = CircuitDiagram('Оперативные цепи', wires, elements)
# cd.make_dxf()
# cd.place_elements()
# cd.update_coord_from_dxf('Оперативные цепи.dxf')
cd.update_elements()
# elements.save_json()
print('Чертёжи сформированы.')

# WiringDiagram(list_elements, w, msp2)
# doc2.saveas("Монтажная схема шасси релейного отсека.dxf", encoding='utf-8')
#
# doc3 = ezdxf.new()
# doc3.units = ezdxf.units.MM
# msp3 = doc3.modelspace()
# list_elements = [ [a2,[30,70]],
#                   [a5, [-70,-140]],
#                   [a6, [80,0]],
#                   [a8, [0,0]],
#                   [a9, [-20,-100]],
#                   [pa,[0,-280]],
#                  [pik, [ 0,-160]],
#                 [sx1,[0,-200]],
#                 [sx3,[60,-200]],
#                 [sx5,[120,-200]],
#                 [sx2,[0,-230]],
#                 [sx4,[60,-230]],
#                 [sx6,[120,-230]],
#                  [sb1,[180,-180]],
#                  [sb2,[180,-230]],
#                   [r3,[150,30]],
#                   [r4, [150, 20]],
#                   [r5, [150, 10]],
#                   [r6, [150, 0]],
#                   [r7, [150, -10]],
#                   [r8, [150, -20]],
#                   [r9, [150, -30]],
#                   [r10, [150, -40]],
#                   [r11, [150, -50]],
#                   [r12, [150, -60]],
#                   [r13, [150, -70]],
#                   [r14, [150, -80]],
#                   [r15, [150, -90]],
#                   [r16, [150, -100]],
#                   [r17, [150, -110]],
#                   [r18, [150, -120]],
#                   ]
# WiringDiagram(list_elements, w, msp3)
# doc3.saveas("Монтажная схема двери.dxf", encoding='utf-8')

# doc4 = ezdxf.new()
# doc4.units = ezdxf.units.MM
# msp4 = doc4.modelspace()
# list_elements4 = [ [ct_a,[0,0]],
#                     [ct_b,[50,0]],
#                   [ct_c, [100, 0]],
#                   ]
#
# WiringDiagram(list_elements4, w, msp4)
# doc4.saveas("Монтажная схема отсека ТТ.dxf", encoding='utf-8')

# cm = CableMagazine()
# cm.add(cab101, cab102, cab103)
# cm.show(ax)

# ci = CableInstallation()
# ci.add(cab101, cab102, cab103)
# ci.show(ax)


