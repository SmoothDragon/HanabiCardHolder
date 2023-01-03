#!/usr/bin/env python3

'''Hanabi single card holders.
The design is intended to be compact and fit within the Hanabi box.

Hanabi card sleeves are typically 57x89mm.

Philosophy:
-We wish to have 8 interlocking holders on each card half.
-Assume 6mm crossbar width.
-Max Y for holder = 89 - 7*6 = 47
-At 45 degree angle, triangle height would be 57/2=28.5
-At 60 degree angle, triangle height would be sqrt(3)/2*57=49
-At a height of 40.7, the hypotenuse (leg) would be 47.

Box inner dimensions 115x90mm
If we want a depth of 40mm per card holder, then (115-40)/15=5.
If we have two 115mm rows, then (115-40)/7 > 10.
This will support a width of 5mm at 60 degrees.
The width for the card holder would them be 45mm.
'''

from solid import *
import solid as sd
from solid.utils import *

import numpy as np


def base_rack(
    base_w=25,
    base_d=20,
    base_h=2,
    base_curve_r=3,
    dial_center_diff=15,
    dial_offset=5,
    ):
    corner = sd.cylinder(r=base_curve_r, h=base_h, center=False)
    high_corner = sd.cylinder(r=base_curve_r, h=1.5*base_h, center=False)
    high_corner = sd.translate([0,0,base_h])(high_corner)
    corner = sd.translate([.5*(-base_w+.0*base_curve_r),base_curve_r,0])(corner)
    high_corner = sd.translate([.5*(-base_w+.0*base_curve_r),base_curve_r,0])(high_corner)
    base = sd.hull()(
        corner,
        sd.translate([0,base_d+6,0])(corner),
        )
    base += sd.hull()(
        sd.translate([base_w,0,0])(corner),
        sd.translate([base_w,base_d+6,0])(corner),
        )
    base += sd.hull()(
        sd.translate([0,base_d,0])(high_corner),
        sd.translate([base_w,base_d,0])(high_corner),
        )
    base = sd.translate([0,-dial_offset,0])(base)
    return base

def beveled_box(XYZ, bevel, center=False):
    '''Box with beveled corners
    Ends are cut so that two rods can be joined at 90 degrees
    XYZ: [X-direction, Y-direction, Z-direction]
    bevel: length of non-hypotenuse sides
    Will be placed in the same location as cube([X,Y,Z])
    center: Positions beveled_box with respect to origin identically to cube()
    '''
    x,y,z = XYZ
    box = sd.hull()(
        sd.cube([x, y-2*bevel, z-2*bevel], center=True),
        sd.cube([x-2*bevel, y, z-2*bevel], center=True),
        sd.cube([x-2*bevel, y-2*bevel, z], center=True),
        )
    if not center:
        box = sd.translate([x/2, y/2, z/2])(box)
    return box

def card_notch(gap=.2, base_w=25, notch_r=6):
    notch = sd.cube([50,3,20],center=True)
    notch = sd.translate([0,0,10])(notch)
    notch -= sd.translate([0,notch_r+gap/2,0])(sd.rotate([0,90,0])(sd.cylinder(r=notch_r, h=2*base_w, center=True)))
    notch -= sd.translate([0,-notch_r,0])(sd.rotate([0,90,0])(sd.cylinder(r=notch_r, h=2*base_w, center=True)))
    notch = sd.rotate([5,0,0])(notch)
    notch = sd.translate([0,27,2.01])(notch)
    return notch

lr_offset = 10
top_d=18
gap = .3
bevel=.4

leg_x = 5
leg_y = 45
leg_z = 2
leg = beveled_box(XYZ=[leg_x, leg_y, leg_z], bevel=bevel, center=True)
leg = sd.translate([0,leg_y/2,leg_z/2])(leg)

leghole_x = 6+gap
leghole_y = 36
leghole_z = 2+gap
leghole = beveled_box(XYZ=[leghole_x, leghole_y, leghole_z], bevel=bevel, center=True)
leghole = sd.translate([-9-gap,leghole_y/2,leghole_z/2])(leghole)

cross_x = 36
cross_y = 10
cross_z = 3
cross = beveled_box(XYZ=[cross_x, cross_y, cross_z], bevel=bevel, center=True)
cross = sd.translate([0, 10, cross_z/2+leg_z])(cross)

post = beveled_box(XYZ=[leg_x, cross_y, cross_z+leg_z], bevel=bevel, center=True)
post = sd.translate([0,0,(cross_z+leg_z)/2])(post)

nub = beveled_box(XYZ=[leg_x, cross_y, cross_z+2*bevel-.2], bevel=bevel, center=True)
nub = sd.translate([0,0,(cross_z+2*bevel)/2+leg_z-bevel-gap/2])(nub)

leg1 = sd.translate([leg_y/2-leg_x*3**.5/2,0,0])(sd.rotate([0,0,30])(leg))
leg2 = sd.translate([-(leg_y/2-leg_x*3**.5/2),0,0])(sd.rotate([0,0,-30])(leg))
tip = sd.intersection()(leg1,leg2)

sleg_x = 5
sleg_y = 36
sleg_z = 2
sleg = beveled_box(XYZ=[sleg_x, sleg_y, sleg_z], bevel=bevel, center=True)
sleg = sd.translate([0,sleg_y/2,sleg_z/2])(sleg)

total = sd.union()(
    sd.translate([leg_y/2-leg_x*3**.5/2,0,0])(sd.rotate([0,0,30])(sleg)),
    sd.translate([-(leg_y/2-leg_x*3**.5/2),0,0])(sd.rotate([0,0,-30])(sleg)),
    tip,
    cross,
    # sd.translate([-(cross_x-leg_x)/2,0,0])(leg),
    # sd.translate([(cross_x-leg_x)/2,0,0])(leg),
    # cross,
    # sd.translate([(cross_x-leg_x)/2,27,0])(post),
    # sd.translate([-(cross_x-leg_x)/2,27,0])(post),
    # sd.translate([0,27,0])(post),
    # sd.translate([(leg_x+2*gap)/2,27,0])(post),
    # sd.translate([-(leg_x+2*gap)/2,27,0])(post),
    # sd.translate([(cross_x-leg_x+2)/2,27,0])(nub),
    # sd.translate([-(cross_x-leg_x+2)/2,27,0])(nub),
    )

total += sd.translate([0,-10,0])(total)
# total = base_rack() 

# notch = sd.cube([50,1,20],center=True)
# notch = sd.translate([0,0,10])(notch)
# notch = sd.rotate([0,0,0])(notch)
# notch = sd.translate([0,18,2])(notch)

# total += leghole
total -= card_notch(gap=gap)
# total = beveled_box([10,20,30],1)


fn = 256
fa = 6
print(scad_render(total,file_header=f'$fn={fn};$fa={fa};'))
