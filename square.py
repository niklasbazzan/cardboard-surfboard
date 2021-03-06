import cadquery as cq
import math

###PARAMETERS 1 = 1mm
#import surfboard model, make solid
obj = cq.importers.importStep('/home/nik/Documents/surfboards/68v2.stp')
f1,f2 = obj.faces().vals()
sb = cq.Solid.makeSolid(cq.Shell.makeShell((f1,f2)))
show_object(sb)

# auto board dimensions
sbbb = obj.val().BoundingBox()
bl = math.ceil(sbbb.xlen) #length
bw = math.ceil(sbbb.zlen) #width
bh = math.ceil(sbbb.ylen) #height

###INPUTS
###manual rocker profile heights
nh = math.ceil(bh*0.97)
ffh = math.ceil(bh*0.34)
tqh = math.ceil(bh*0.28)
hh = math.ceil(bh*0.23)
qh = math.ceil(bh*0.25)
th = math.ceil(bh*0.59)
###misc
L = 3.8 #thickness of cardboard
q = 26 #space between sections
U = 15 #shift sections forwards by

###calculations
t = L/2 #thickness of cutters
H = math.ceil(math.ceil((bw/2)/q)*q*-1) #stringer range start
HH = math.ceil(math.ceil((bw/2)/q)*q) #stringer range stop

###CUTTERS
###locations
a = [(U,0,0)] #stringers
for i in range (U, bl, q):
    a.append((i,0,0))
a = tuple(a)

b = [(0,0,H)] #crosses
for i in range (H, HH, q):
    b.append((0,0,i))
b = tuple(b)

###cuts stringers
cs = (
cq.Workplane("YZ")
.pushPoints(a)
.eachpoint(lambda loc: (cq.Workplane()
.rect(bh*2,bw)
.extrude(t, both = True)
.val().located(loc)
)
)
)
#show_object(cs)

###cuts crosses
cc = (
cq.Workplane("XY")
.pushPoints(b)
.eachpoint(lambda loc: (cq.Workplane()
.rect(bl,bh, centered = False)
.extrude(t, both = True)
.val().located(loc)
)
)
)
#show_object(cc)

###ROCKER PROFILE
r = cq.Workplane("XY")
sPnts = [
    (math.ceil(bl*0.80), ffh),
    (math.ceil(bl*0.75), tqh),
    (math.ceil(bl*0.5), hh),
    (math.ceil(bl*0.25), qh),
    (0, th)
]

rp = r.lineTo(bl, -100).lineTo(bl, nh).spline(sPnts, includeCurrent=True).close().extrude(bw+50/2, both=True)
#show_object(rp)

###STRINGERS
swp = cq.Workplane("XY").add(sb)
s = (swp - rp) + ((swp & rp)- cs)

# for i in range(0, math.ceil(bw/2), q):
#     show_object(s.section(i))

###CROSSES
# cwp = cq.Workplane("YZ").add(sb)
# c = (cwp - rp - cc) + ((cwp & rp))

# for i in range(U, bl, q):
#     show_object(c.section(i))

###DXF export

ls = list(range(0, math.ceil(bw/2), q))
#lc = list(range(U, bl, q))

from path import Path
from cadquery import exporters as exp

with Path('six-eight-funboard').mkdir_p():
    exp.export(s.section(ls[0]),'s0.dxf')
    exp.export(s.section(ls[1]),'s1.dxf')
    exp.export(s.section(ls[2]),'s2.dxf')
    exp.export(s.section(ls[3]),'s3.dxf')
    exp.export(s.section(ls[4]),'s4.dxf')
    exp.export(s.section(ls[5]),'s5.dxf')
    exp.export(s.section(ls[6]),'s6.dxf')
    exp.export(s.section(ls[7]),'s7.dxf')
    exp.export(s.section(ls[8]),'s8.dxf')
    exp.export(s.section(ls[9]),'s9.dxf')
    exp.export(s.section(ls[10]),'s10.dxf')

    # exp.export(c.section(lc[0]),'c0.dxf')
    # exp.export(c.section(lc[1]),'c1.dxf')
    # exp.export(c.section(lc[2]),'c2.dxf')
    # exp.export(c.section(lc[3]),'c3.dxf')
    # exp.export(c.section(lc[4]),'c4.dxf')
    # exp.export(c.section(lc[5]),'c5.dxf')
    # exp.export(c.section(lc[6]),'c6.dxf')
    # exp.export(c.section(lc[7]),'c7.dxf')
    # exp.export(c.section(lc[8]),'c8.dxf')
    # exp.export(c.section(lc[9]),'c9.dxf')
    # exp.export(c.section(lc[10]),'c10.dxf')
    # exp.export(c.section(lc[11]),'c11.dxf')
    # exp.export(c.section(lc[12]),'c12.dxf')
    # exp.export(c.section(lc[13]),'c13.dxf')
    # exp.export(c.section(lc[14]),'c14.dxf')
    # exp.export(c.section(lc[15]),'c15.dxf')
    # exp.export(c.section(lc[16]),'c16.dxf')
    # exp.export(c.section(lc[17]),'c17.dxf')
    # exp.export(c.section(lc[18]),'c18.dxf')
    # exp.export(c.section(lc[19]),'c19.dxf')
    # exp.export(c.section(lc[20]),'c20.dxf')
    # exp.export(c.section(lc[21]),'c21.dxf')
    # exp.export(c.section(lc[22]),'c22.dxf')
    # exp.export(c.section(lc[23]),'c23.dxf')
    # exp.export(c.section(lc[24]),'c24.dxf')
    # exp.export(c.section(lc[25]),'c25.dxf')
    # exp.export(c.section(lc[26]),'c26.dxf')
    # exp.export(c.section(lc[27]),'c27.dxf')
    # exp.export(c.section(lc[28]),'c28.dxf')
    # exp.export(c.section(lc[29]),'c29.dxf')
    # exp.export(c.section(lc[30]),'c30.dxf')
    # exp.export(c.section(lc[31]),'c31.dxf')
    # exp.export(c.section(lc[32]),'c32.dxf')
    # exp.export(c.section(lc[33]),'c33.dxf')
    # exp.export(c.section(lc[34]),'c34.dxf')
    # exp.export(c.section(lc[35]),'c35.dxf')
    # exp.export(c.section(lc[36]),'c36.dxf')
    # exp.export(c.section(lc[37]),'c37.dxf')
    # exp.export(c.section(lc[38]),'c38.dxf')
    # exp.export(c.section(lc[39]),'c39.dxf')
    # exp.export(c.section(lc[40]),'c40.dxf')
    # exp.export(c.section(lc[41]),'c41.dxf')
    # exp.export(c.section(lc[42]),'c42.dxf')
    # exp.export(c.section(lc[43]),'c43.dxf')
    # exp.export(c.section(lc[44]),'c44.dxf')
    # exp.export(c.section(lc[45]),'c45.dxf')
    # exp.export(c.section(lc[46]),'c46.dxf')
    # exp.export(c.section(lc[47]),'c47.dxf')
    # exp.export(c.section(lc[48]),'c48.dxf')
    # exp.export(c.section(lc[49]),'c49.dxf')
    # exp.export(c.section(lc[50]),'c50.dxf')
    # exp.export(c.section(lc[51]),'c51.dxf')
    # exp.export(c.section(lc[52]),'c52.dxf')
    # exp.export(c.section(lc[53]),'c53.dxf')
    # exp.export(c.section(lc[54]),'c54.dxf')
    # exp.export(c.section(lc[55]),'c55.dxf')
    # exp.export(c.section(lc[56]),'c56.dxf')
    # exp.export(c.section(lc[57]),'c57.dxf')
    # exp.export(c.section(lc[58]),'c58.dxf')
    # exp.export(c.section(lc[59]),'c59.dxf')
    # exp.export(c.section(lc[60]),'c60.dxf')
    # exp.export(c.section(lc[61]),'c61.dxf')
    # exp.export(c.section(lc[62]),'c62.dxf')
    # exp.export(c.section(lc[63]),'c63.dxf')
    # exp.export(c.section(lc[64]),'c64.dxf')
    # exp.export(c.section(lc[65]),'c65.dxf')
    # exp.export(c.section(lc[66]),'c66.dxf')
    # exp.export(c.section(lc[67]),'c67.dxf')
    # exp.export(c.section(lc[68]),'c68.dxf')
    # exp.export(c.section(lc[69]),'c69.dxf')
    # exp.export(c.section(lc[70]),'c70.dxf')
    # exp.export(c.section(lc[71]),'c71.dxf')
    # exp.export(c.section(lc[72]),'c72.dxf')
    # exp.export(c.section(lc[73]),'c73.dxf')
    # exp.export(c.section(lc[74]),'c74.dxf')
    # exp.export(c.section(lc[75]),'c75.dxf')
    # exp.export(c.section(lc[76]),'c76.dxf')
    # exp.export(c.section(lc[77]),'c77.dxf')


