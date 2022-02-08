import cadquery as cq
import math

###PARAMETERS 1 = 1mm
#import surfboard model, make solid
obj = cq.importers.importStep('/home/nik/Documents/surfboards/69v10.stp')
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
nh = math.ceil(bh*0.96)
ffh = math.ceil(bh*0.25)
tqh = math.ceil(bh*0.22)
hh = math.ceil(bh*0.17)
qh = math.ceil(bh*0.23)
th = math.ceil(bh*0.56)
###misc
L = 3.8 #thickness of cardboard
q = 30 #space between sections
U = 13 #shift sections forwards by

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

###STRINGERS
swp = cq.Workplane("XY").add(sb)
s = (swp - rp) + ((swp & rp)- cs)

#for i in range(0, math.ceil(bw/2), q):
#    show_object(s.section(i))

###CROSSES
# cwp = cq.Workplane("YZ").add(sb) #try ZY?
# c = (cwp - rp - cc) + ((cwp & rp))

# for i in range(U, bl, q):
#     show_object(c.section(i))

###DXF export

ls = list(range(0, math.ceil(bw/2), q))
#lc = list(range(U, bl, q))

from path import Path
from cadquery import exporters as exp

with Path('dxfs').mkdir_p():
    exp.export(s.section(0),'s0.dxf')
    #exp.export(c.section(lc[9]),'c9.dxf')
    # exp.export(c.section(lc[6]),'c6.dxf')
    # exp.export(c.section(lc[7]),'c7.dxf')
    # exp.export(c.section(lc[8]),'c8.dxf')
    #exp.export(s.section(0.000000001),'s00000.dxf')
#    exp.export(s.section(ls[1]),'s1.dxf')
#    exp.export(s.section(ls[2]),'s2.dxf')
#    exp.export(s.section(ls[3]),'s3.dxf')
#    exp.export(s.section(ls[4]),'s4.dxf')
    # exp.export(c.section(lc[0]),'c0.dxf')
    # exp.export(c.section(lc[1]),'c1.dxf')
    # exp.export(c.section(lc[2]),'c2.dxf')
    # exp.export(c.section(lc[3]),'c3.dxf')
    # exp.export(c.section(lc[4]),'c4.dxf')
    # exp.export(u.section(l[0]),'u0.dxf')
    # exp.export(u.section(l[1]),'u1.dxf')
    # exp.export(u.section(l[2]),'u2.dxf')
#    exp.export(d.section(l[3]),'d3.dxf')
#    exp.export(d.section(l[4]),'d4.dxf')
   # exp.export(stringers.section(ls[6]),'s6.dxf')
   # exp.export(stringers.section(ls[7]),'s7.dxf')
   # exp.export(stringers.section(ls[8]),'s8.dxf')
   # exp.export(stringers.section(ls[9]),'s9.dxf')

    # exp.export(u.section(l[0]),'u0.dxf')
    # exp.export(u.section(l[1]),'u1.dxf')
    # exp.export(u.section(l[2]),'u2.dxf')
    # exp.export(u.section(l[3]),'u3.dxf')
    # exp.export(u.section(l[4]),'u4.dxf')
    # exp.export(u.section(l[5]),'u5.dxf')
    #exp.export(d.section(l[0]),'d0.dxf')
    #exp.export(d.section(l[1]),'d1.dxf')
    #exp.export(d.section(l[2]),'d2.dxf')
    #exp.export(d.section(l[3]),'d3.dxf')
    #exp.export(d.section(l[4]),'d4.dxf')
#    exp.export(stringers.section(ls[2]),'s2.dxf')
#    exp.export(stringers.section(ls[3]),'s3.dxf')
#    exp.export(stringers.section(ls[10]),'s10.dxf')
#    exp.export(stringers.section(ls[11]),'s11.dxf')
#    exp.export(stringers.section(ls[12]),'s12.dxf')
#    exp.export(stringers.section(ls[13]),'s13.dxf')
