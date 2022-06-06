from src.electroproject import *
import ezdxf
a1=BB_TEL10(name='A1')
a2=PS7('A2')
a3=BU_TEL('A3')
a4=BP_TEL('A4')
a5=MR500_V2('A5')
a6=PS3_old('A6')
a8=DUGA_O('A8')
a9=PS12('A9')
c1 = C('C1', highlight=True)
c2 = C('C2')
c3 = C('C3')
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
sx1=AC22('SX1')
sx2=AC22('SX2')
sx3=AC22('SX3')
sx4=AC22('SX4')
sx5=AC22('SX5')
sx6=AC22('SX6')
ct_a = CT2('TA-A')
ct_b = CT2('TA-B')
ct_c = CT2('TA-C')
x = Connectors('X', 30)
xt1 = XT('XT1', 120)
xt2 = XT('XT1', 70)
xt3 = XT('XT1', 32, 'СШР55-П30-ЗГ1')

w = []
w.append(Wire(a2, 1, xt2, 52))
w.append(Wire(a2, 2, xt2, 25))
w.append(Wire(a2, 3, xt1, 113))
w.append(Wire(a2, 4, xt1, 114))

'''
rel_otc = MountingModule('Релейный отсек')
sh8.add(yat_a, yat_c, kl1, kl2, a1)
'''
# doc1 = ezdxf.new()
# doc1.units = ezdxf.units.MM
# msp1 = doc1.modelspace()
# CircuitDiagram(w, msp1)
# doc1.saveas("Принципиальная схема.dxf", encoding='utf-8')

doc2 = ezdxf.new()
doc2.units = ezdxf.units.MM
msp2 = doc2.modelspace()
list_elements = [[a2,[0,0]],
                  [ct_a,[200,0]],
                [ct_b, [230,0]],
                 [a3,[0,-50]],
                 [a4, [60,-50]],
                 [a5, [-100,0]],
                 [a6, [130,-60]],
                 [a8, [0,-200]],
                 [a9, [30,-250]],
                 [pa,[70,-200]],
                 [pik, [ 0,-300]],
                 [sb1,[0,-350]],
                 [sb2,[30,-350]],]


WiringDiagram(list_elements, w, msp2)
doc2.saveas("Монтажная схема.dxf", encoding='utf-8')

# cm = CableMagazine()
# cm.add(cab101, cab102, cab103)
# cm.show(ax)

# ci = CableInstallation()
# ci.add(cab101, cab102, cab103)
# ci.show(ax)

print('Чертёжи сформированы.')
